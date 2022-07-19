from message import Message
from component import Component
class Leaf (Component):
    def __init__ (self, parent, instanceName): super ().__init__ (parent, instanceName)
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
    def reset (self):
        pass
