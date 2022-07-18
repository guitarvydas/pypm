
#!/usr/bin/env python3
# link__scraper.py
# cell_27
import mpos
import dispatcher
import re
class _link__scraper (mpos.Container):
  def __init__ (self, dispatcher, parent, idInParent):
    super ().__init__ (dispatcher, parent, idInParent)
    self.inputs=['[text]']
    self.outputs=['[links]']
    self.result = []
    
    self.connections = [  ]
    self.children = {}
  
  

