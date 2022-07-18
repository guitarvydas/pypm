
#!/usr/bin/env python3
# md__file__reader.py
# cell_8
import mpos
import dispatcher
import re
class _md__file__reader (mpos.Container):
  def __init__ (self, dispatcher, parent, idInParent):
    super ().__init__ (dispatcher, parent, idInParent)
    self.inputs=['filename']
    self.outputs=['text']
    
    
    self.connections = [  ]
    self.children = {}
  
  

