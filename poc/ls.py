
#!/usr/bin/env python3
# ls.py
# cell_6
import mpos
import dispatcher
class _ls (mpos.Leaf):
  def __init__ (self, dispatcher, parent, idInParent):
    super ().__init__ (dispatcher, parent, idInParent)
    self.inputs=['iterate', 'directory']
    self.outputs=['filename']
    self.dirname = ''
    
  def react (self, inputMessage):
    if (False):
      pass
    elif (message.port == "directory"):
      self.dirname = message.data
    elif (message.port == "iterate"):
      
      
      
      files = os.listdir (self.dirname)
      for fname in files:
          name = self.dirname + '/' + fname
          if (os.path.isfile (name)):
              self.send (self, 'filename', name, message)
          else:
              pass
      
    
    return super ().react (inputMessage)

