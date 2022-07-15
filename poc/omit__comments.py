
#!/usr/bin/env python3
# omit__comments.py
# cell_6
import mpos
import dispatcher
class _omit__comments (mpos.Leaf):
  def __init__ (self, dispatcher, parent, idInParent):
    super ().__init__ (dispatcher, parent, idInParent)
    self.inputs=['text']
    self.outputs=['text']
    
    
  def react (self, inputMessage):
    if (False):
      pass
    elif (message.port == "text"):
      
      
      
      
      
      
        result = re.sub (r'#.*
      ', '
      ', message.data)
        self.send (self, 'text', result, message)
      
      
      
    
    return super ().react (inputMessage)

