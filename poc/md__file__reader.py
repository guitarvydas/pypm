
#!/usr/bin/env python3
# md__file__reader.py
# cell_7
import mpos
import dispatcher
class _md__file__reader (mpos.Leaf):
  def __init__ (self, dispatcher, parent, idInParent):
    super ().__init__ (dispatcher, parent, idInParent)
    self.inputs=['filename']
    self.outputs=['text']
    
    
  
  def react (self, inputMessage):
    if (False):
      pass
    elif (message.port == "[text]"):
      
      if (re.search (r'\.md$', message.data)):
          f = open (message.data, 'r')
          result = f.read ()
          self.send (self, 'text', result, message)
      else:
          self.send (self, 'text', '', message)
      
    
    return super ().react (inputMessage)

