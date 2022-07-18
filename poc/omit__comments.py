
#!/usr/bin/env python3
# omit__comments.py
# cell_19
import mpos
import dispatcher
import re
class _omit__comments (mpos.Container):
  def __init__ (self, dispatcher, parent, idInParent):
    super ().__init__ (dispatcher, parent, idInParent)
    self.inputs=['text']
    self.outputs=['text']
    
    
    self.connections = [  ]
    self.children = {}
  
  

