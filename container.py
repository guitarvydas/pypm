import component
class Container (component.Component):
    def __init__ (self, parent, instanceName): super ().__init__ (parent, instanceName)
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
    def delegateMessage (self, source, data):
        self.copyMessage (source, data)
    def copyMessage (self, source, data):
        connection = self.findConnection (source)
        if (connection != None):
            self.beginAtomic (connection)
            for conn in connection['receivers']:
                receiver = conn['receiver']
                port = conn['port']
                if (receiver != self):
                    receiver.appendInputMessage ({'port': port, 'data': data})
                else:
                    receiver.appendOutputMessage ({'port': port, 'data': data})
            self.endAtomic (connection)
    def findConnection (self, source):
        for conn in self.connections:
            if (conn['port'] == source['port'] and conn['sender'] == source['sender']):
                return conn
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
    def routeChildOutputs (self, child):
        for output in child.outputQueueAsList ():
            port = output['port']
            data = output['data']
            source = {'sender': child, 'port': port}
            self.copyMessage (source, data)
    def beginAtomic (self, connection): pass # non-pass for bare-metal               
    def endAtomic (self, connection): pass   # non-pass for bare-metal
    def handler (self, port, data):
        super ().handler (port, data)
    
                
