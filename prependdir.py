from message import Message
from leaf import Leaf

class PrependDir (Leaf):
    def __init__ (self, parent, name): 
        super().__init__ (parent, name)
        self.dir = None
    def handler (self, message):
        super ().handler (message)
        if (message.port == 'dirname'):
            self.dir = message.data
        elif (message.port == 'filename'):
            assert self.dir, 'internal error in PrependDir - self.dir has not yet been set'
            name = self.dirname + '/' + message.data
            self.send (self, 'name', name, message)
        else:
            raise Exception (f"unrecognized message in PrependDir '{message.port}'")
