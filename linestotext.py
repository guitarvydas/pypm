import Message from message
import leaf

class LinesToText (leaf.Leaf):
    def __init__ (self, parent, name): super().__init__ (parent, name)
    def handler (self, message):
        super ().handler (message)
        if (port == '[text]'):
            for line in data:
                self.send (self, 'text', line + '\n')

