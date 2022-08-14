
#!/usr/bin/env python3
# md__file__reader2.py
# cell_38
import mpos
import dispatcher
import re
import &lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;on__➢❲filename❳__{⟪&lt;/div&gt;&lt;div&gt;if__(re.search__(r'%5c.md$',__message.data)):&lt;/div&gt;&lt;div&gt;&amp;nbsp;__&amp;nbsp;__f__=__open__(message.data,__'r')&lt;/div&gt;&lt;div&gt;&amp;nbsp;__&amp;nbsp;__result__=__f.read__()&lt;/div&gt;&lt;div&gt;&amp;nbsp;__&amp;nbsp;__self.send__('text',__result)&lt;/div&gt;&lt;div&gt;else:&lt;/div&gt;&lt;div&gt;&amp;nbsp;__&amp;nbsp;__self.send__('text',__'')&lt;/div&gt;&lt;div&gt;⟫}&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;div&gt;&lt;br&gt;&lt;/div&gt;
class _md__file__reader2 (mpos.Container):
  def __init__ (self, dispatcher, parent, idInParent):
    super ().__init__ (dispatcher, parent, idInParent)
    self.inputs=['filename', 'filename']
    self.outputs=['text']
    
    
    child0 = &lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;on__➢❲filename❳__{⟪&lt;/div&gt;&lt;div&gt;if__(re.search__(r'%5c.md$',__message.data)):&lt;/div&gt;&lt;div&gt;&amp;nbsp;__&amp;nbsp;__f__=__open__(message.data,__'r')&lt;/div&gt;&lt;div&gt;&amp;nbsp;__&amp;nbsp;__result__=__f.read__()&lt;/div&gt;&lt;div&gt;&amp;nbsp;__&amp;nbsp;__self.send__('text',__result)&lt;/div&gt;&lt;div&gt;else:&lt;/div&gt;&lt;div&gt;&amp;nbsp;__&amp;nbsp;__self.send__('text',__'')&lt;/div&gt;&lt;div&gt;⟫}&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;div&gt;&lt;br&gt;&lt;/div&gt;._&lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;on__➢❲filename❳__{⟪&lt;/div&gt;&lt;div&gt;if__(re.search__(r'%5c.md$',__message.data)):&lt;/div&gt;&lt;div&gt;&amp;nbsp;__&amp;nbsp;__f__=__open__(message.data,__'r')&lt;/div&gt;&lt;div&gt;&amp;nbsp;__&amp;nbsp;__result__=__f.read__()&lt;/div&gt;&lt;div&gt;&amp;nbsp;__&amp;nbsp;__self.send__('text',__result)&lt;/div&gt;&lt;div&gt;else:&lt;/div&gt;&lt;div&gt;&amp;nbsp;__&amp;nbsp;__self.send__('text',__'')&lt;/div&gt;&lt;div&gt;⟫}&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;div&gt;&lt;br&gt;&lt;/div&gt; (dispatcher, self, '&lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;on ➢❲filename❳ {⟪&lt;/div&gt;&lt;div&gt;if (re.search (r'%5C.md$', message.data)):&lt;/div&gt;&lt;div&gt;&amp;nbsp; &amp;nbsp; f = open (message.data, 'r')&lt;/div&gt;&lt;div&gt;&amp;nbsp; &amp;nbsp; result = f.read ()&lt;/div&gt;&lt;div&gt;&amp;nbsp; &amp;nbsp; self.send ('text', result)&lt;/div&gt;&lt;div&gt;else:&lt;/div&gt;&lt;div&gt;&amp;nbsp; &amp;nbsp; self.send ('text', '')&lt;/div&gt;&lt;div&gt;⟫}&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;div&gt;&lt;br&gt;&lt;/div&gt;')        
    conn0 = mpos.Connector ([mpos.Sender ('-', 'filename')], [mpos.Receiver ('MD File Reader', 'filename')])        
    conn1 = mpos.Connector ([mpos.Sender ('-', 'filename')], [mpos.Receiver ('MD File Reader2', 'filename')])        
    conn2 = mpos.Connector ([mpos.Sender ('perfilelinkscraper', 'filename')], [mpos.Receiver ('MD File Reader', 'filename')])        
    conn3 = mpos.Connector ([mpos.Sender ('perfilelinkscraper', 'filename')], [mpos.Receiver ('MD File Reader2', 'filename')])
    self.connections = [ conn0, conn1, conn2, conn3 ]
    self.children = {'&lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;&lt;div&gt;on ➢❲filename❳ {⟪&lt;/div&gt;&lt;div&gt;if (re.search (r'%5C.md$', message.data)):&lt;/div&gt;&lt;div&gt;&amp;nbsp; &amp;nbsp; f = open (message.data, 'r')&lt;/div&gt;&lt;div&gt;&amp;nbsp; &amp;nbsp; result = f.read ()&lt;/div&gt;&lt;div&gt;&amp;nbsp; &amp;nbsp; self.send ('text', result)&lt;/div&gt;&lt;div&gt;else:&lt;/div&gt;&lt;div&gt;&amp;nbsp; &amp;nbsp; self.send ('text', '')&lt;/div&gt;&lt;div&gt;⟫}&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;&lt;div&gt;&lt;br&gt;&lt;/div&gt;':child0}
  
  

