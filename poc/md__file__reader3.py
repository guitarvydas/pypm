
#!/usr/bin/env python3
# md__file__reader3.py
# cell_36
import mpos
import dispatcher
import re
import md__file__reader
class _md__file__reader3 (mpos.Container):
  def __init__ (self, dispatcher, parent, idInParent):
    super ().__init__ (dispatcher, parent, idInParent)
    self.inputs=[]
    self.outputs=[]
    
    
    child0 = md__file__reader._md__file__reader (dispatcher, self, 'MD File Reader')
    self.connections = [  ]
    self.children = {'MD File Reader':child0}
  
  

