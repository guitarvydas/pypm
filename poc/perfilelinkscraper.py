
#!/usr/bin/env python3
# perfilelinkscraper.py
# cell_7
import mpos
import dispatcher
import re
import md__file__reader
class _perfilelinkscraper (mpos.Container):
  def __init__ (self, dispatcher, parent, idInParent):
    super ().__init__ (dispatcher, parent, idInParent)
    self.inputs=['filename']
    self.outputs=['[links]']
    
    
    child0 = md__file__reader._md__file__reader (dispatcher, self, 'MD File Reader')        
    conn0 = mpos.Connector ([mpos.Sender ('', 'filename')], [mpos.Receiver ('MD File Reader', 'filename')])
    self.connections = [ conn0 ]
    self.children = {'MD File Reader':child0}
  
  

