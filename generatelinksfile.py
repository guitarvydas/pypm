import container
import sequencer
import linkcollection
import linktofilename
import perfilelinkscraper
import linestotext
import filewriter

class GenerateLinksFile (container.Container):
    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)
        self.child1 = sequencer.Sequencer (self, 'sequencer')
        self.child2 = linkcollection.LinkCollection (self, 'link collection')
        self.child3 = linktofilename.LinkToFilename (self, 'link to filename')
        self.child4 = perfilelinkscraper.PerFileLinkScraper (self, 'per file link scraper')
        self.child5 = linestotext.LinesToText (self, 'lines to text')
        self.child6 = filewriter.FileWriter (self, 'file writer')
        self.children = [self.child1, self.child2, self.child3, self.child4, self.child5, self.child6]
        self.connections = [
                { 'sender' : self, 'port' : 'filename', 'receivers' : [{'receiver' : self.child1, 'port':'filename' }]},
                { 'sender' : self, 'port' : 'base directory', 'receivers' : [{'receiver' : self.child3, 'port':'base directory' }]},
                { 'sender' : self, 'port' : 'suffix', 'receivers' : [{'receiver' : self.child3, 'port':'suffix' }]},

                { 'sender' : self.child1, 'port' : 'output filename', 'receivers' : [{'receiver' : self.child6, 'port':'filename'}]},
                { 'sender' : self.child1, 'port' : 'clear', 'receivers' : [{'receiver' : self.child6, 'port':'clear'}]},
                { 'sender' : self.child1, 'port' : 'input filename', 'receivers' : [{'receiver' : self.child4, 'port':'filename'}]},
                { 'sender' : self.child1, 'port' : 'req', 'receivers' : [{'receiver' : self.child2, 'port':'req next'}]},
                { 'sender' : self.child1, 'port' : 'done', 'receivers' : [{'receiver' : self, 'port':'done'}]},

                { 'sender' : self.child2, 'port' : 'no more', 'receivers' : [{'receiver' : self.child1, 'port':'no more'}]},
                { 'sender' : self.child2, 'port' : 'link', 'receivers' : [{'receiver' : self.child3, 'port':'link'}]},

                { 'sender' : self.child3, 'port' : 'filename', 'receivers' : [ { 'receiver' : self.child4, 'port' : 'filename' }]},

                { 'sender' : self.child4, 'port' : 'output', 
                  'receivers' : [ {'receiver':self.child5, 'port':'[text]'},
                                  {'receiver':self.child2, 'port':'[append list]'}]},

                { 'sender' : self.child5, 'port' : 'text', 'receivers' : [ { 'receiver' : self.child6, 'port' : 'append' }]}
            ]
    def handler (self, port, data):
        super ().handler (port, data)
        print (f'generate {port} {data}')
        self.delegateMessage ({'sender' : self, 'port' : port}, data)
        self.route ()
        self.runToCompletion ()

tester = GenerateLinksFile (None, 'generate links file')
bdir = '/Users/tarvydas/Dropbox/ps'
suffix = '.md'
testfile = 'test.txt'
tester.handler ('base directory', bdir)
tester.handler ('suffix', suffix)
tester.handler ('filename', testfile)
done = tester.outputs2dict ()['done']
print (done)

