from message import Message
import leaf
import container

class TextToLines (leaf.Leaf):
    def __init__ (self, parent, name): 
        super().__init__ (parent, name)
    def handler (self, message):
        super ().handler (message)
        if (message.port == 'text'):
            lines = message.data.split ('\n')
            for line in lines:
                # this should really be done with an REQuest protocol, but,
                #  this is a one-of and I don't care if I fill memory with zillions of line messages...
                #  (doing it like this will generate all of the line messages at once and will queue them up)
                self.send (self, 'line', line, message)
        else:
            raise Exception (f"unrecognized message in TextToLines '{message.port}'")
