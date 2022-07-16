
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
    'init'
     
  print ('raw') 
  
  
  def react (self, inputMessage):
    if (False):
      pass
    elif (message.port == "text"):
      
      if (message.port == 'text'):
          text = message.data.split ('\n')
          result = rmCodeQuotesState0 (text)
          self.send (self, '[text]', result, message)
      
    
    return super ().react (inputMessage)

