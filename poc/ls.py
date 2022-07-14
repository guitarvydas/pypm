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
        #inits
        self.dirname=''

    def react (self, inputMessage):
        initially{⟪self.dirname=''⟫}
        on➢❲directory❳{⟪self.dirname=message.data⟫}
        on➢❲iterate❳{⟪
          files=os.listdir(self.dirname)
          forfnameinfiles:
            name=self.dirname+'/'+fname
            if(os.path.isfile(name)):
              self.send(self,'filename',name,message)
            else:
              pass
        ⟫}
             
        
        
        
        
        
        return super ().react (inputMessage)
