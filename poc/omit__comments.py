
#!/usr/bin/env python3
# omit__comments.py
# cell_15
import mpos
import dispatcher
import re
class _omit__comments (mpos.Leaf):
  def __init__ (self, dispatcher, parent, idInParent):
    super ().__init__ (dispatcher, parent, idInParent)
    self.inputs=['text']
    self.outputs=['text']
    
    
    
  def react (self, message):
    if (False):
      pass
    elif (message.tag == "text"):
      
        result = re.sub (r'\#.*\n', '\n', message.data)
        self.send ('text', result)
      
    else:
      print (self.idInParent + ": internal error unrecognized message: " + message.tag)
    return super ().react (message)

