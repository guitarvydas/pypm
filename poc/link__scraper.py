
#!/usr/bin/env python3
# link__scraper.py
# cell_22
import mpos
import dispatcher
class _link__scraper (mpos.Leaf):
  def __init__ (self, dispatcher, parent, idInParent):
    super ().__init__ (dispatcher, parent, idInParent)
    self.inputs=['[text]']
    self.outputs=['[links]']
    result = []
    
    
  def react (self, inputMessage):
    if (False):
      pass
    elif (message.port == "[text]"):
      
      for line in message.data:
          result += re.findall ('(\[\[[^\]]+\]\])',line)
      self.send (self, '[links]', result, message)
      
    
    return super ().react (inputMessage)

