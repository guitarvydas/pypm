
#!/usr/bin/env python3
# md__file__reader.py
# cell_11
import mpos
import dispatcher
import re
import md__file__reader3
class _md__file__reader (mpos.Container):
  def __init__ (self, dispatcher, parent, idInParent):
    super ().__init__ (dispatcher, parent, idInParent)
    self.inputs=[]
    self.outputs=[]
    
    
    child0 = md__file__reader3._md__file__reader3 (dispatcher, self, 'MD File Reader3')
    self.connections = [  ]
    self.children = {'MD File Reader3':child0}
  
  

