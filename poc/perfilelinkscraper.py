
#!/usr/bin/env python3
# perfilelinkscraper.py
# cell_6
import mpos
import dispatcher
import re
import omit__code__quotes
import omit__comments
import link__scraper
import md__file__reader
class _perfilelinkscraper (mpos.Container):
  def __init__ (self, dispatcher, parent, idInParent):
    super ().__init__ (dispatcher, parent, idInParent)
    self.inputs=['filename']
    self.outputs=['[links]']
    
    
    child0 = omit__code__quotes._omit__code__quotes (dispatcher, self, 'Omit Code Quotes')
    child1 = omit__comments._omit__comments (dispatcher, self, 'Omit Comments')
    child2 = link__scraper._link__scraper (dispatcher, self, 'Link Scraper')
    child3 = md__file__reader._md__file__reader (dispatcher, self, 'MD File Reader')        
    conn0 = mpos.Connector ([mpos.Sender ('Omit Code Quotes', '[text]')], [mpos.Receiver ('Link Scraper', '[text]')])        
    conn1 = mpos.Connector ([mpos.Sender ('Omit Comments', 'text')], [mpos.Receiver ('Omit Code Quotes', 'text')])        
    conn2 = mpos.Connector ([mpos.Sender ('', 'filename')], [mpos.Receiver ('MD File Reader', 'filename')])        
    conn3 = mpos.Connector ([mpos.Sender ('Link Scraper', '[links]')], [mpos.Receiver ('', '[links]')])        
    conn4 = mpos.Connector ([mpos.Sender ('MD File Reader', 'text')], [mpos.Receiver ('Omit Comments', 'text')])
    self.connections = [ conn0, conn1, conn2, conn3, conn4 ]
    self.children = {'Omit Code Quotes':child0, 'Omit Comments':child1, 'Link Scraper':child2, 'MD File Reader':child3}
  
  

