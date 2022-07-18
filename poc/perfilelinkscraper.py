
#!/usr/bin/env python3
# perfilelinkscraper.py
# cell_7
import mpos
import dispatcher
import re
class _perfilelinkscraper (mpos.Container):
  def __init__ (self, dispatcher, parent, idInParent):
    super ().__init__ (dispatcher, parent, idInParent)
    self.inputs=['filename']
    self.outputs=['[links]']
    
    
    self.connections = [  ]
    self.children = {}
  
  

