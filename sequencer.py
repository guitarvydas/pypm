import leaf
class Sequencer (leaf.Leaf):
    def __init__ (self, parent, name):
        super ().__init__ (parent, name)
        self.state = 'idle'
    def handler (self, port, data):
        super ().handler (port, data)
        print ('Sequencer.[' + self.state + ']')
        if (self.state == 'idle'):
            if (port == 'filename'):
                self.send ('output filename', 'out.' + data)
                self.send ('clear', True)
                self.enterStateFetching (data)
            else:
                # pass
                raise Exception ('unknown message.port in idle')
        elif (self.state == 'fetching'):
            if (port == 'filename'):
                self.enterStateFetching (data)
            elif (port == 'no more'):
                self.send ('done', True)
                self.state = 'idle'
            else:
                # pass
                raise Exception ('unknown message.port in fetching')
        else:
            # pass
            raise Exception ('unknown state')
    def enterStateFetching (self, fname):
        self.state = 'fetching'
        self.send ('input filename', fname)
        self.send ('req', True)
