from message import Message
import container
import filereader
import omitcomments
import omitcodequotes
import linkscraper

class PerFileLinkScraper (container.Container):
    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)
        self.child1 = filereader.FileReader (self, 'file reader')
        self.child2 = omitcomments.OmitComments (self, 'omit comments')
        self.child3 = omitcodequotes.OmitCodeQuotes (self, 'omit code quotes')
        self.child4 = linkscraper.LinkScraper (self, 'link scraper')
        self.children = [self.child1, self.child2, self.child3, self.child4]
        self.connections = [
                { 'sender' : self, 'port' : 'filename', 'receivers' : [ { 'receiver' : self.child1, 'port' : 'filename' }]},
                { 'sender' : self.child1, 'port' : 'text', 'receivers' : [{'receiver' : self.child2, 'port' : 'text'}]},
                { 'sender' : self.child2, 'port' : 'text', 'receivers' : [{'receiver' : self.child3, 'port' : 'text'}]},
                { 'sender' : self.child3, 'port' : '[text]', 'receivers' : [{'receiver' : self.child4, 'port' : '[text]'}]},
                { 'sender' : self.child4, 'port' : '[links]', 'receivers' : [{'receiver' : self, 'port' : 'output' }]}
            ]
    def handler (self, message):
        super ().handler (message)
        if (message.port == 'filename'):
            self.delegateMessage (message)
            self.route ()
            self.runToCompletion ()
        else:
            raise Exception (f'Unrecognized Port for pm {message.port}')
    def call (self, text):
        self.handler (Message (self, 'text', text))
        return self.outputs2dict ()['output']

def testPerFileLinkScraper ():
    tester = PerFileLinkScraper (None, 'per file link scraper')
    tester.handler (Message (tester, 'filename', 'test.txt'))
    print (tester.outputs2dict ()['output'])

# testPerFileLinkScraper ()