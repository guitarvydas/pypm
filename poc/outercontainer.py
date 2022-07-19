
#!/usr/bin/env python3
# outercontainer.py
# cell_6
import mpos
import dispatcher
import re
import innercontainer
class _outercontainer (mpos.Container):
  def __init__ (self, dispatcher, parent, idInParent):
    super ().__init__ (dispatcher, parent, idInParent)
    self.inputs=['filename']
    self.outputs=['[links]', 'text']
    
    
    child0 = innercontainer._innercontainer (dispatcher, self, 'INNERCONTAINER')        
    conn0 = mpos.Connector ([mpos.Sender ('INNERCONTAINER', '[links]')], [mpos.Receiver ('OUTERCONTAINER', '[links]')])        
    conn1 = mpos.Connector ([mpos.Sender ('OUTERCONTAINER', 'filename')], [mpos.Receiver ('INNERCONTAINER', 'filename')])
    self.connections = [ conn0, conn1 ]
    self.children = {'INNERCONTAINER':child0}
  
  

