
#!/usr/bin/env python3
# link__scraper2.py
# cell_52
import mpos
import dispatcher
import re
class _link__scraper2 (mpos.Container):
  def __init__ (self, dispatcher, parent, idInParent):
    super ().__init__ (dispatcher, parent, idInParent)
    self.inputs=['[text]', '[text]']
    self.outputs=['[links]']
    self.result = []
    
    self.connections = [  ]
    self.children = {}
  
  

