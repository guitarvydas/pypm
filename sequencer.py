from message import Message
import leaf
class Sequencer (leaf.Leaf):
    def __init__ (self, parent, name):
        super ().__init__ (parent, name)
        self.state = 'idle'
    def handler (self, message):
        super ().handler (message)
        if (self.state == 'idle'):
            if (message.port == 'filename'):
                self.send (self, 'output filename', 'out.' + message.data, message)
                self.send (self, 'clear', True, message)
                self.enterStateFetching (message.data, message)
            else:
                pass
                raise Exception ('unknown message.port in idle')
        elif (self.state == 'fetching'):
            if (message.port == 'filename'):
                self.enterStateFetching (message.data, message)
            elif (message.port == 'no more'):
                self.send (self, 'done', True, message)
                self.state = 'idle'
            else:
                pass
                raise Exception ('unknown message.port in fetching')
        else:
            pass
            raise Exception ('unknown state')
    def enterStateFetching (self, fname, message):
        self.state = 'fetching'
        self.send (self, 'input filename', fname, message)
