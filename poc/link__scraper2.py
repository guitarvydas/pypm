
#!/usr/bin/env python3
# link__scraper2.py
# cell_52
import mpos
import dispatcher
import re
class _link__scraper2 (mpos.Leaf):
  def __init__ (self, dispatcher, parent, idInParent):
    super ().__init__ (dispatcher, parent, idInParent)
    self.inputs=['[text]']
    self.outputs=['[links]']
    self.result = []
    
  
  def react (self, message):
    if (False):
      pass
    elif (message.tag == "[text]"):
      
      for line in message.data:
          self.result += re.findall ('(\[\[[^\]]+\]\])',line)
      self.send ('[links]', self.result)
      
    else:
      print (self.idInParent + ": internal error unrecognized message: " + message.tag)
    return super ().react (message)
