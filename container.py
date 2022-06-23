import component
class Container (component.Component):
    def __init__ (self, parent, instanceName): 
        super ().__init__ (parent, instanceName)
        self.failOnNC = True
    def tick (self):
        super ().tick ()
        workDone = False
        for c in self.children:
            workDone = workDone or c.tick ()
        if ((not workDone) and self.ready ()):
            message = self.dequeueInputMessage ()
            self.delegateMessage ({'sender':self, 'port':message['port']}, message['data']) 
            workDone = True
        return workDone
    def busy (self):
        for c in self.children:
            if (c.inputQueueNotEmpty () or c.busy ()):
                return True
        return False
    def runToCompletion (self):
        while (self.busy ()):
            self.tick ()
            self.route ()
    def delegateMessage (self, message):
        self.propagateMessage (self, message.port, message)
    def propagateMessage (self, sender, senderPort, message):
        connection = self.findConnection (sender, senderPort)
        if (connection != None):
            self.beginAtomic (connection)
            for conn in connection['receivers']:
                receiver = conn['receiver']
                port = conn['port']
                if (receiver != self):
                    receiver.appendInputMessage (message)
                else:
                    receiver.appendOutputMessage (message)
            self.endAtomic (connection)
    def findConnection (self, sender, senderPort):
        for conn in self.connections:
            if (conn['port'] == senderPort and conn['sender'] == sender):
                return conn
        if (self.failOnNC):
            raise Exception (f"No Connection Found in {self.name} :: {sender.name} {senderPort}")
        else:   
            pass
        return None
    def route (self):
        super ().route ()
        for c in self.children:
            c.route ()
            if c.outputQueueNotEmpty ():
                self.routeChildOutputs (c)
                c.resetOutputQueue ()
            else:
                pass
    def routeChildOutputs (self, child):
        for outputMessage in child.outputQueueAsList ():
            assert child == outputMessage.sender, "internal error in routeChildOutputs"
            self.propagateMessage (child, outputMessage.port, outputMessage.data)
    def beginAtomic (self, connection): pass # non-pass for bare-metal               
    def endAtomic (self, connection): pass   # non-pass for bare-metal
    def handler (self, message):
        super ().handler (message)
    
                
