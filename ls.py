from message import Message
from leaf import Leaf
import os

class LS (Leaf):
    def __init__ (self, parent, name): 
        super().__init__ (parent, name)
        self.dirname = ''
    def handler (self, message):
        super ().handler (message)
        if (message.port == 'directory'):
            self.dirname = message.data
        elif (message.port == 'iterate'):
            files = os.listdir (self.dirname)
            for fname in files:
                name = self.dirname + '/' + fname
                if (os.path.isfile (name)):
                    self.send (self, 'filename', name, message)
                else:
                    pass
        else:
            raise Exception (f"unrecognized message in LS '{message.port}'")
            
