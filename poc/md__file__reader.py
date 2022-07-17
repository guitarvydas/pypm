
#!/usr/bin/env python3
# md__file__reader.py
# cell_7
import mpos
import dispatcher
import re
class _md__file__reader (mpos.Leaf):
  def __init__ (self, dispatcher, parent, idInParent):
    super ().__init__ (dispatcher, parent, idInParent)
    self.inputs=['filename']
    self.outputs=['text']
    
    
    
  def react (self, message):
    if (False):
      pass
    elif (message.tag == "filename"):
      
      if (re.search (r'\.md$', message.data)):
          f = open (message.data, 'r')
          result = f.read ()
          self.send ('text', result)
      else:
          self.send ('text', '')
      
    else:
      print (self.idInParent + ": internal error unrecognized message: " + message.tag)
    return super ().react (message)

