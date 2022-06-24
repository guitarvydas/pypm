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
                self.send (self, 'output filename', 'out.' + message.data)
                self.send (self, 'clear', True)
                self.enterStateFetching (message.data)
            else:
                pass
                raise Exception ('unknown message.port in idle')
        elif (self.state == 'fetching'):
            if (message.port == 'filename'):
                self.enterStateFetching (message.data)
            elif (message.port == 'no more'):
                self.send (self, 'done', True)
                self.state = 'idle'
            else:
                pass
                raise Exception ('unknown message.port in fetching')
        else:
            pass
            raise Exception ('unknown state')
    def enterStateFetching (self, fname):
        self.state = 'fetching'
        self.send (self, 'input filename', fname)
