
#!/usr/bin/env python3
# link__scraper.py
# cell_25
import mpos
import dispatcher
import re
import link__scraper3
class _link__scraper (mpos.Container):
  def __init__ (self, dispatcher, parent, idInParent):
    super ().__init__ (dispatcher, parent, idInParent)
    self.inputs=[]
    self.outputs=[]
    
    
    child0 = link__scraper3._link__scraper3 (dispatcher, self, 'Link Scraper3')
    self.connections = [  ]
    self.children = {'Link Scraper3':child0}
  
  

