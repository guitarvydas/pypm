
#!/usr/bin/env python3
# pm.py
# cell_6
import mpos
import dispatcher
import re
import 
import md__file__reader
import omit__code__quotes
import omit__comments
import link__scraper
class _pm (mpos.Container):
  def __init__ (self, dispatcher, parent, idInParent):
    super ().__init__ (dispatcher, parent, idInParent)
    self.inputs=['filename']
    self.outputs=['[links]']
    
    
    child0 = ._ (dispatcher, self, '')
    child1 = md__file__reader._md__file__reader (dispatcher, self, 'MD File Reader')
    child2 = omit__code__quotes._omit__code__quotes (dispatcher, self, 'Omit Code Quotes')
    child3 = omit__comments._omit__comments (dispatcher, self, 'Omit Comments')
    child4 = link__scraper._link__scraper (dispatcher, self, 'Link Scraper')        
    conn0 = mpos.Connector ([mpos.Sender ('', '[links]')], [mpos.Receiver ('', '[links]')])        
    conn1 = mpos.Connector ([mpos.Sender ('', '[links]')], [mpos.Receiver ('', '[links]')])        
    conn2 = mpos.Connector ([mpos.Sender ('Link Scraper', '[links]')], [mpos.Receiver ('', '[links]')])        
    conn3 = mpos.Connector ([mpos.Sender ('', '[text]')], [mpos.Receiver ('Link Scraper', '[text]')])        
    conn4 = mpos.Connector ([mpos.Sender ('Omit Code Quotes', '[text]')], [mpos.Receiver ('Link Scraper', '[text]')])        
    conn5 = mpos.Connector ([mpos.Sender ('', 'text')], [mpos.Receiver ('', 'text')])        
    conn6 = mpos.Connector ([mpos.Sender ('', 'text')], [mpos.Receiver ('Omit Code Quotes', 'text')])        
    conn7 = mpos.Connector ([mpos.Sender ('', 'text')], [mpos.Receiver ('Omit Comments', 'text')])        
    conn8 = mpos.Connector ([mpos.Sender ('MD File Reader', 'text')], [mpos.Receiver ('', 'text')])        
    conn9 = mpos.Connector ([mpos.Sender ('MD File Reader', 'text')], [mpos.Receiver ('Omit Comments', 'text')])        
    conn10 = mpos.Connector ([mpos.Sender ('Omit Comments', 'text')], [mpos.Receiver ('', 'text')])        
    conn11 = mpos.Connector ([mpos.Sender ('Omit Comments', 'text')], [mpos.Receiver ('Omit Code Quotes', 'text')])
    self.connections = [ conn0, conn1, conn2, conn3, conn4, conn5, conn6, conn7, conn8, conn9, conn10, conn11 ]
    self.children = {'':child0, 'MD File Reader':child1, 'Omit Code Quotes':child2, 'Omit Comments':child3, 'Link Scraper':child4}
  
  

