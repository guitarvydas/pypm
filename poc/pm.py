
#!/usr/bin/env python3
# pm.py
# cell_6
import mpos
import dispatcher
import re
import perfilelinkscraper
class _pm (mpos.Container):
  def __init__ (self, dispatcher, parent, idInParent):
    super ().__init__ (dispatcher, parent, idInParent)
    self.inputs=['filename']
    self.outputs=['[links]']
    
    
    child0 = perfilelinkscraper._perfilelinkscraper (dispatcher, self, 'perfilelinkscraper')        
    conn0 = mpos.Connector ([mpos.Sender ('perfilelinkscraper', '[links]')], [mpos.Receiver ('', '[links]')])        
    conn1 = mpos.Connector ([mpos.Sender ('perfilelinkscraper', 'filename')], [mpos.Receiver ('MD File Reader', 'filename')])        
    conn2 = mpos.Connector ([mpos.Sender ('', 'filename')], [mpos.Receiver ('perfilelinkscraper', 'filename')])
    self.connections = [ conn0, conn1, conn2 ]
    self.children = {'perfilelinkscraper':child0}
  
  

