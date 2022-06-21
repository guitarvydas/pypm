import container
import perfilelinkscraper

class Tester (container.Container):
    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)
        self.child1 = perfilelinkscraper.PerFileLinkScraper (self, 'file reader')
        self.children = [self.child1]
        self.connections = [
                { 'sender' : self, 'port' : 'filename', 'receivers' : [ { 'receiver' : self.child1, 'port' : 'filename' }]}
            ]
    def handler (self, port, data):
        super ().handler (port, data)
        if (port == 'filename'):
            self.delegateMessage ({'sender' : self, 'port' : 'filename'}, data)
            self.route ()
            self.runToCompletion ()
        else:
            raise Exception (f'Unrecognized Port for pm {port}')
    def call (self, text):
        self.handler ('text', text)
        return 'done'

tester = Tester (None, 'tester')
tester.handler ('filename', 'test.txt')
print ('done')

