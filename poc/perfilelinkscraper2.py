
#!/usr/bin/env python3
# perfilelinkscraper2.py
# cell_35
import mpos
import dispatcher
import re
import md__file__reader2
import omit__code__quotes2
import omit__comments2
import link__scraper2
class _perfilelinkscraper2 (mpos.Container):
  def __init__ (self, dispatcher, parent, idInParent):
    super ().__init__ (dispatcher, parent, idInParent)
    self.inputs=['filename']
    self.outputs=['[links]']
    
    
    child0 = md__file__reader2._md__file__reader2 (dispatcher, self, 'MD File Reader2')
    child1 = omit__code__quotes2._omit__code__quotes2 (dispatcher, self, 'Omit Code Quotes2')
    child2 = omit__comments2._omit__comments2 (dispatcher, self, 'Omit Comments2')
    child3 = link__scraper2._link__scraper2 (dispatcher, self, 'Link Scraper2')        
    conn0 = mpos.Connector ([mpos.Sender ('Link Scraper2', '[links]')], [mpos.Receiver ('', '[links]')])        
    conn1 = mpos.Connector ([mpos.Sender ('Omit Code Quotes2', '[text]')], [mpos.Receiver ('Link Scraper2', '[text]')])        
    conn2 = mpos.Connector ([mpos.Sender ('', 'filename')], [mpos.Receiver ('MD File Reader2', 'filename')])        
    conn3 = mpos.Connector ([mpos.Sender ('MD File Reader2', 'text')], [mpos.Receiver ('Omit Comments2', 'text')])        
    conn4 = mpos.Connector ([mpos.Sender ('Omit Comments2', 'text')], [mpos.Receiver ('Omit Code Quotes2', 'text')])
    self.connections = [ conn0, conn1, conn2, conn3, conn4 ]
    self.children = {'MD File Reader2':child0, 'Omit Code Quotes2':child1, 'Omit Comments2':child2, 'Link Scraper2':child3}
  
  

