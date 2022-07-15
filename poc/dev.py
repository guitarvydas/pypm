
#!/usr/bin/env python3
# dev.py
# cell_6
import mpos
import dispatcher
class _dev (mpos.Leaf):
  def __init__ (self, dispatcher, parent, idInParent):
    super ().__init__ (dispatcher, parent, idInParent)
    self.inputs=['iterate', 'directory']
    self.outputs=['filename']
    self.dirname = ''
    
  def react (self, inputMessage):
    if (False):
      pass
    elif (message.port == "dev"):
      result = re.sub (r'\#.*\n', '\n', message.data)
    
    return super ().react (inputMessage)

