
#!/usr/bin/env python3
# omit__code__quotes3.py
# cell_39
import mpos
import dispatcher
import re
import omit__code__quotes
class _omit__code__quotes3 (mpos.Container):
  def __init__ (self, dispatcher, parent, idInParent):
    super ().__init__ (dispatcher, parent, idInParent)
    self.inputs=[]
    self.outputs=[]
    
    
    child0 = omit__code__quotes._omit__code__quotes (dispatcher, self, 'Omit Code Quotes')
    self.connections = [  ]
    self.children = {'Omit Code Quotes':child0}
  
  

