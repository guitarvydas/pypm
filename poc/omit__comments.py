
#!/usr/bin/env python3
# omit__comments.py
# cell_17
import mpos
import dispatcher
import re
import omit__comments3
class _omit__comments (mpos.Container):
  def __init__ (self, dispatcher, parent, idInParent):
    super ().__init__ (dispatcher, parent, idInParent)
    self.inputs=[]
    self.outputs=[]
    
    
    child0 = omit__comments3._omit__comments3 (dispatcher, self, 'Omit Comments3')
    self.connections = [  ]
    self.children = {'Omit Comments3':child0}
  
  

