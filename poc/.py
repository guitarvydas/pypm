
#!/usr/bin/env python3
# .py
# cell_11
import mpos
import dispatcher
import re
class _ (mpos.Container):
  def __init__ (self, dispatcher, parent, idInParent):
    super ().__init__ (dispatcher, parent, idInParent)
    self.inputs=['text', 'text']
    self.outputs=['text', '[text]', 'text', '[links]', '[links]']
    
            
    conn0 = mpos.Connector ([mpos.Sender ('', '[links]')], [mpos.Receiver ('', '[links]')])        
    conn1 = mpos.Connector ([mpos.Sender ('Link Scraper', '[links]')], [mpos.Receiver ('', '[links]')])
    self.connections = [ conn0, conn1 ]
    self.children = {}
  
  

