
#!/usr/bin/env python3
# omit__comments3.py
# cell_42
import mpos
import dispatcher
import re
import omit__comments
class _omit__comments3 (mpos.Container):
  def __init__ (self, dispatcher, parent, idInParent):
    super ().__init__ (dispatcher, parent, idInParent)
    self.inputs=[]
    self.outputs=[]
    
    
    child0 = omit__comments._omit__comments (dispatcher, self, 'Omit Comments')
    self.connections = [  ]
    self.children = {'Omit Comments':child0}
  
  

