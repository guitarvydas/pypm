# signature ≈❲Per File Link Scraper❳ {
#   inputs {➢❲filename❳}
#   outputs {◦❲links❳}
#   }
# }


from message import Message
from pairs import {Sender, Receiver}
import container
import re

import mdfilereader
import omitcomments
import omitcodequotes
import linkscraper

class Per_File_Link_Scraper (Container):
    def __init__ (self, parent, name):
        super ().__init__ (parent, name)
        md__file__reader = mdfilereader.MD__File__Reader (self, 'MD File Reader')
        omit__comments = omitcomments.Omit__Comments (self, 'MD File Reader')
        omit__code__quotes = omitcodequotes.Omit__Code__Quotes (self, 'MD File Reader')
        link__scraper = linkscraper.Link__Scraper (self, 'MD File Reader')
        self.children = [md__file__reader, omit__comments, omit__code__quotes, link__scraper]
        net1 = [Sink (md__file__reader, 'filename')]
        net2 = [Sink (omit__comments, 'text')]
        net3 = [Sink (omit__code__quotes, 'text')]
        net4 = [Sink (link__scraper, '[text]')]
        net5 = [Sink (self, '[links]')]
        self.nets = [net1, net2, net3, net4, net5]
        sourceA = Source (self, 'filename', net1)
        sourceB = Source (md__file__reader, 'text', net2)
        sourceC = Source (omit__comments, 'text', net3)
        sourceD = Source (omit__code__quotes, '[text]',net4)
        sourceE = Source (link__scraper, '[links]', net5)
        self.sources = [sourceA, sourceB, sourceC, sourceD, sourceE]
    def handler (self, message):
        super ().handler (message)
        self.handleSourceMessage (message)

            
