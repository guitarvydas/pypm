import container
import linkcollection
import linktofilename
import perfilelinkscraper
import looptrigger

class LoopbackScraper (container.Container):
    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)
        self.child1 = linkcollection.LinkCollection (self, 'link collection')
        self.child2 = linktofilename.LinkToFilename (self, 'link to filename')
        self.child3 = perfilelinkscraper.PerFileLinkScraper (self, 'per file link scraper')
        self.child4 = looptrigger.LoopTrigger (self, 'loop trigger')
        self.children = [self.child1, self.child2, self.child3, self.child4]
        self.connections = [
                { 'sender' : self, 'port' : 'filename', 'receivers' : [{'receiver' : self.child3, 'port':'filename' }]},
                { 'sender' : self, 'port' : 'base directory', 'receivers' : [{'receiver' : self.child2, 'port':'base directory' }]},
                { 'sender' : self, 'port' : 'suffix', 'receivers' : [{'receiver' : self.child2, 'port':'suffix' }]},
                { 'sender' : self, 'port' : 'start', 'receivers' : [{'receiver' : self.child4, 'port':'any' }]},

                { 'sender' : self.child1, 'port' : 'link', 'receivers' : [
                    {'receiver' : self.child2, 'port':'link' },
                    {'receiver' : self.child4, 'port':'any' }
                    ]},
                { 'sender' : self.child1, 'port' : 'no more', 'receivers' : [{'receiver' : self, 'port':'no more' }]},

                { 'sender' : self.child2, 'port' : 'filename', 'receivers' : [{'receiver' : self.child3, 'port':'filename'}]},

                { 'sender' : self.child3, 'port' : 'output', 
                  'receivers' : [
                      {'receiver' : self.child1, 'port':'[append list]'},
                      {'receiver' : self, 'port':'output'},
                  ]
                 },

                { 'sender':self.child4, 'port':'trigger', 'receivers':[{'receiver':self.child1,'port':'req next'}]}
            ]
    def handler (self, message):
        super ().handler (message)
        self.delegateMessage (message)
        self.route ()
        self.runToCompletion ()

