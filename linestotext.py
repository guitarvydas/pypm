from message import Message
import leaf

class LinesToText (leaf.Leaf):
    def __init__ (self, parent, name): super().__init__ (parent, name)
    def handler (self, message):
        super ().handler (message)
        if (message.port == '[text]'):
            for line in message.data:
                self.send (self, 'text', line + '\n')

