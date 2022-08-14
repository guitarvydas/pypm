
#!/usr/bin/env python3
# .py
# cell_9
import mpos
import dispatcher
import re
class _ (mpos.Container):
  def __init__ (self, dispatcher, parent, idInParent):
    super ().__init__ (dispatcher, parent, idInParent)
    self.inputs=[]
    self.outputs=[]
    
    
    self.connections = [  ]
    self.children = {}
  
  

