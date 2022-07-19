from message import Message
import component

class Container (Component):
    def __init__ (self, parent, instanceName): 
        super ().__init__ (parent, instanceName)
        self.failOnNC = True
    def step (self):
        super ().step ()
        workDone = False
        for c in self.children:
            workDone = workDone or c.step ()
        if ((not workDone) and self.ready ()):
            message = self.dequeueInputMessage ()
            self.delegateMessage (message) 
            workDone = True
        return workDone
    def busy (self):
        for c in self.children:
            if (c.inputQueueNotEmpty () or c.busy ()):
                return True
        return False
    def runToCompletion (self):
        while (self.busy ()):
            self.step ()
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
                trail = message.trail
                newm = Message (receiver, port, message.data, trail)
                if (receiver != self):
                    newm.status = 'routed to input'
                    receiver.appendInputMessage (newm)
                else:
                    newm.status = 'routed to output'
                    receiver.appendOutputMessage (newm)
            self.endAtomic (connection)
    def findConnection (self, sender, senderPort):
        for conn in self.connections:
            if (conn['port'] == senderPort and conn['sender'] == sender):
                return conn
        raise Exception (f"No Connection Found in '{self.name}' :: '{sender.name}' '{senderPort}'")
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
            self.propagateMessage (child, outputMessage.port, outputMessage)
    def beginAtomic (self, connection): pass # ignore unless in bare-metal               
    def endAtomic (self, connection): pass   # ignore unless in bare-metal
    def handler (self, message):
        super ().handler (message)
    
                
