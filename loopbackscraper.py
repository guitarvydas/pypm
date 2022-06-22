import container
import linkcollection
import linktofilename
import perfilelinkscraper

class LoopbackScraper (container.Container):
    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)
        self.child1 = linkcollection (self, 'link collection')
        self.child2 = linktofilename.LinkToFilename (self, 'link to filename')
        self.child3 = perfilelinkscraper.PerFileLinkScraper (self, 'per file link scraper')
        self.children = [self.child1, self.child2, self.child3]
        self.connections = [
                { 'sender' : self, 'port' : 'filename', 'receivers' : [{'receiver' : self.child3, 'port':'filename' }]},
                { 'sender' : self, 'port' : 'base directory', 'receivers' : [{'receiver' : self.child2, 'port':'base directory' }]},
                { 'sender' : self, 'port' : 'suffix', 'receivers' : [{'receiver' : self.child2, 'port':'suffix' }]},
                { 'sender' : self, 'port' : 'next req', 'receivers' : [{'receiver' : self.child1, 'port':'next req' }]},

                { 'sender' : self.child1, 'port' : 'first time', 'receivers' : [{'receiver' : self.child1, 'port':'next req' }]},
                { 'sender' : self.child1, 'port' : 'link', 'receivers' : [{'receiver' : self.child2, 'port':'link' }]},
                { 'sender' : self.child1, 'port' : 'no more', 'receivers' : [{'receiver' : self, 'port':'no more' }]},

                { 'sender' : self.child2, 'port' : 'filename', 'receivers' : [{'receiver' : self.child3, 'port':'filename'}]},

                { 'sender' : self.child3, 'port' : 'ouput', 
                  'receivers' : [
                      {'receiver' : self.child1, 'port':'[append text]'},
                      {'receiver' : self, 'port':'output'},
                  ]
            ]
    def handler (self, port, data):
        super ().handler (port, data)
        print (f'generate {port} {data}')
        self.delegateMessage ({'sender' : self, 'port' : port}, data)
        self.route ()
        self.runToCompletion ()

