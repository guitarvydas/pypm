import container
import linkcollection
import linktofilename
import perfilelinkscraper
import looptrigger

class LoopbackScraper (container.Container):
    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)
        self.child1 = perfilelinkscraper.PerFileLinkScraper (self, 'first [per file link scraper]')
        self.child2 = linkcollection.LinkCollection (self, 'link collection')
        self.child3 = linktofilename.LinkToFilename (self, 'link to filename')
        self.child4 = perfilelinkscraper.PerFileLinkScraper (self, 'rest [per file link scraper]')
        self.child5 = looptrigger.LoopTrigger (self, 'loop trigger')
        self.children = [self.child1, self.child2, self.child3, self.child4, self.child5]
        self.connections = [
                { 'sender' : self, 'port' : 'filename', 'receivers' : [{'receiver' : self.child1, 'port':'filename' }]},
                { 'sender' : self, 'port' : 'base directory', 'receivers' : [{'receiver' : self.child3, 'port':'base directory' }]},
                { 'sender' : self, 'port' : 'suffix', 'receivers' : [{'receiver' : self.child3, 'port':'suffix' }]},

                { 'sender' : self.child1, 'port' : '[links]', 'receivers' : [
                    {'receiver':self,        'port':'[links]'},
                    {'receiver':self.child2, 'port':'[append list]' },
                    {'receiver':self.child5, 'port':'any' }
                    ]},

                { 'sender':self.child2, 'port':'link', 'receivers' : [{'receiver':self.child3, 'port':'link' }]},
                { 'sender':self.child2, 'port':'no more', 'receivers' : [{'receiver':self, 'port':'no more' }]},

                { 'sender' : self.child3, 'port' : 'filename', 'receivers' : [{'receiver':self.child4, 'port':'filename'}]},
                { 'sender' : self.child3, 'port' : 'error', 'receivers' : []},

                { 'sender' : self.child4, 'port' : '[links]', 
                  'receivers' : [
                      {'receiver' : self.child2, 'port':'[append list]'},
                      {'receiver':self, 'port':'[links]'},
                      {'receiver' : self.child5, 'port':'any'},
                  ]
                 },

                { 'sender':self.child5, 'port':'trigger', 'receivers':[{'receiver':self.child2,'port':'req next'}]}
            ]
    def handler (self, message):
        super ().handler (message)
        self.delegateMessage (message)
        self.route ()
        self.runToCompletion ()

