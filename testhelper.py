from message import Message
import leaf
class TestHelperStep1 (leaf.Leaf):
    def __init__ (self, parent, name):
        super ().__init__ (parent, name)
        self.filename = ''
    def handler (self, message):
        super ().handler (message)
        if (message.port == 'filename'):
            self.filename = message.data
            self.send (self, 'input filename', self.filename, message)
            self.send (self, 'output filename', "out." + self.filename, message)
            self.send (self, 'clear', True, message)
        else:
            raise Exception ('unkown port')

class TestHelperStep2 (leaf.Leaf):
    def __init__ (self, parent, name):
        super ().__init__ (parent, name)
    def handler (self, message):
        super ().handler (message)
        if (message.port == 'filename'):
            self.send (self, 'filename', message.data, message)
        else:
            raise Exception ('unkown port')

