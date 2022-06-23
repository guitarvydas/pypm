import Message from message
import leaf

class LoopTrigger (leaf.Leaf):
    def __init__ (self, parent, name): 
        super().__init__ (parent, name)
    def handler (self, message):
        super ().handler (message)
        if (message.port == 'any'):
            self.send (self, 'trigger', True)
        else:
            raise Exception (f'unrecognized message in Loop/{message.port}/')
