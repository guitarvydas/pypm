from message import Messag
import container
import testhelper
import perfilelinkscraper
import linestotext
import filewriter

class Tester (container.Container):
    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)
        self.child1 = testhelper.TestHelperStep1 (self, 'test help step 1')
        self.child2 = testhelper.TestHelperStep2 (self, 'test help step 2')
        self.child3 = perfilelinkscraper.PerFileLinkScraper (self, 'per file link scraper')
        self.child4 = linestotext.LinesToText (self, 'list to text')
        self.child5 = filewriter.FileWriter (self, 'file writer')
        self.children = [self.child1, self.child2, self.child3, self.child4, self.child5]
        self.connections = [
                { 'sender' : self, 'port' : 'filename', 'receivers' : [{'receiver' : self.child1, 'port':'filename' }]},
                { 'sender' : self.child1, 'port' : 'output filename', 'receivers' : [{'receiver' : self.child5, 'port':'filename'}]},
                { 'sender' : self.child1, 'port' : 'clear', 'receivers' : [ { 'receiver' : self.child5, 'port' : 'clear' }]},
                { 'sender' : self.child1, 'port' : 'input filename', 'receivers' : [{'receiver' : self.child2, 'port':'filename'}]},
                { 'sender' : self.child2, 'port' : 'filename', 'receivers' : [ { 'receiver' : self.child3, 'port' : 'filename' }]},
                { 'sender' : self.child3, 'port' : 'output', 'receivers' : [ { 'receiver' : self.child4, 'port' : '[text]' }]},
                { 'sender' : self.child4, 'port' : 'text', 'receivers' : [ { 'receiver' : self.child5, 'port' : 'append' }]}
            ]
    def handler (self, message):
        super ().handler (message)
        if (port == 'filename'):
            self.delegateMessage (message)
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

