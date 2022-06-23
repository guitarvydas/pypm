from message import Message
import component
class Leaf (component.Component):
    def __init__ (self, parent, instanceName): super ().__init__ (parent, instanceName)
    def send (self, sender, portname, data):
        self.appendOutputMessage (Message (sender, portname, data))
    def tick (self):
        super ().tick ()
        if self.ready ():
            message = self.dequeueInputMessage ()
            self.handler (message)
            return True
        else:
            return False
    def ready (self):
        return len (self.inputq) > 0
    def busy (self):
        return False
    def outputs2dict (self):
        # this could be done more efficiently
        # map all output values into a single dict,
        #    overriding each key/value pair with the most recent value at that key
        # (TODO: should this return a stack of values (alist) for each key instead
        #    of 1 value for each key?)
        resultdict = {}
        for message in self.outputQueueAsList ():
            resultdict [message.port] = message.data
        pass
        return resultdict

