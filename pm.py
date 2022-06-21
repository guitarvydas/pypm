import container
import filereader
import omitcomments
import omitcodequotes

class PM (container.Container):
    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)
        self.child1 = filereader.FileReader (self, 'file reader')
        self.child2 = omitcomments.OmitComments (self, 'omit comments')
        self.child3 = omitcodequotes.OmitCodeQuotes (self, 'omit code quotes')
        self.children = [ self.child1, self.child2, self.child3]
        self.connections = [
                { 'sender' : self, 'port' : 'filename', 'receivers' : [ { 'receiver' : self.child1, 'port' : 'filename' }]},
                { 'sender' : self.child1, 'port' : 'text', 'receivers' : [{'receiver' : self.child2, 'port' : 'text'}]},
                { 'sender' : self.child2, 'port' : 'text', 'receivers' : [{'receiver' : self.child3, 'port' : 'text'}]},
                { 'sender' : self.child3, 'port' : '[text]', 'receivers' : [{'receiver' : self, 'port' : 'output' }]}
            ]
    def handler (self, port, data):
        if (port == 'filename'):
            self.delegateMessage ({'sender' : self, 'port' : 'filename'}, data)
            self.route ()
            self.runToCompletion ()
        else:
            raise Exception (f'Unrecognized Port for pm {port}')
    def call (self, text):
        self.handler ('text', text)
        return self.outputs2dict ()['output']

tester = PM (None, 'pattern matching')
tester.handler ('filename', 'test.txt')
print (tester.outputs2dict ()['output'])

