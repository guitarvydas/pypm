from message import Message
from leaf import Leaf

def markua (s):
    return s.replace ('\n', '').strip ().lower ().replace (' ', '--')

class CopyFile (Leaf):
    def __init__ (self, parent, name): 
        super().__init__ (parent, name)
        self.src = None
        self.dest = None
    def handler (self, message):
        super ().handler (message)
        if (message.port == 'name'):
            name = markua (message.data)
            self.send (self, 'name',  name, message)
        else:
            raise Exception (f"unrecognized message in mangleForMarkua '{message.port}'")
