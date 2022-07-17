
#!/usr/bin/env python3
# link__scraper.py
# cell_22
import mpos
import dispatcher
import re
class _link__scraper (mpos.Leaf):
  def __init__ (self, dispatcher, parent, idInParent):
    super ().__init__ (dispatcher, parent, idInParent)
    self.inputs=['[text]']
    self.outputs=['[links]']
    result = []
    
    
  def react (self, message):
    if (False):
      pass
    elif (message.tag == "[text]"):
      
      for line in message.data:
          result += re.findall ('(\[\[[^\]]+\]\])',line)
      self.send ('[links]', result)
      
    else:
      print (self.idInParent + ": internal error unrecognized message: " + message.tag)
    return super ().react (message)

