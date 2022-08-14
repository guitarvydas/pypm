
#!/usr/bin/env python3
# omit__code__quotes.py
# cell_14
import mpos
import dispatcher
import re
import omit__code__quotes3
class _omit__code__quotes (mpos.Container):
  def __init__ (self, dispatcher, parent, idInParent):
    super ().__init__ (dispatcher, parent, idInParent)
    self.inputs=[]
    self.outputs=[]
    
    
    child0 = omit__code__quotes3._omit__code__quotes3 (dispatcher, self, 'Omit Code Quotes3')
    self.connections = [  ]
    self.children = {'Omit Code Quotes3':child0}
  
  

