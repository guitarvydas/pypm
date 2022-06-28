from message import Message
import leaf
import shutil

class copier (leaf.Leaf):
    def __init__ (self, parent, name): 
        super().__init__ (parent, name)
        self.destdir = ''
    def handler (self, message):
        super ().handler (message)
        if (message.port == 'filename'):
            shutil.copy(message.data, self.destdir)            
        elif (message.port == 'destinationdirectory'):
           self.destdir = message.data
        else:
            raise Exception (f"unrecognized message in Copier '{message.port}'")

