import leaf

class LinesToText (leaf.Leaf):
    def __init__ (self, parent, name): super().__init__ (parent, name)
    def handler (self, port, data):
        super ().handler (port, data)
        if (port == '[text]'):
            for line in data:
                self.send ('text', line + '\n')

