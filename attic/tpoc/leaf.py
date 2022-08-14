from message import Message
from component import Component
class Leaf (Component):
    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)

    def busy (self):
        return False

    def reset (self):
        pass

    def step (self):
        if (self.inputReadyP ()):
            message = self.dequeueInput ()
            self.handler (message)
