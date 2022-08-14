
#!/usr/bin/env python3
# link__scraper3.py
# cell_50
import mpos
import dispatcher
import re
import link__scraper
class _link__scraper3 (mpos.Container):
  def __init__ (self, dispatcher, parent, idInParent):
    super ().__init__ (dispatcher, parent, idInParent)
    self.inputs=[]
    self.outputs=[]
    
    
    child0 = link__scraper._link__scraper (dispatcher, self, 'Link Scraper')
    self.connections = [  ]
    self.children = {'Link Scraper':child0}
  
  

