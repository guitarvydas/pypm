import leaf
class TestHelperStep1 (leaf.Leaf):
    def __init__ (self, parent, name):
        super ().__init__ (parent, name)
        self.filename = ''
    def handler (self, port, data):
        super ().handler (port, data)
        if (port == 'filename'):
            self.filename = data
            self.send ('input filename', self.filename)
            self.send ('output filename', "out." + self.filename)
            self.send ('clear', True)
        else:
            raise Exception ('unkown port')

class TestHelperStep2 (leaf.Leaf):
    def __init__ (self, parent, name):
        super ().__init__ (parent, name)
    def handler (self, port, data):
        super ().handler (port, data)
        if (port == 'filename'):
            self.send ('filename', data)
        else:
            raise Exception ('unkown port')

