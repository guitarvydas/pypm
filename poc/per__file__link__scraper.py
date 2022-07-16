
#!/usr/bin/env python3
# per__file__link__scraper.py
# cell_6
import mpos
import dispatcherimport Omit Code Quotesimport Omit Commentsimport Link Scraperimport MD File Reader
class _per__file__link__scraper (mpos.Container):
  def __init__ (self, dispatcher, parent, idInParent):
    super ().__init__ (dispatcher, parent, idInParent)
    self.inputs=['filename']
    self.outputs=['[links]']
    FAILED 
    Line 1, col 1:
    > 1 | 
          ^
    Expected any character or "initially"
               ✗ text
                 ✗ macro+
                   ✗ macro
                       ✗ lex_InitClause
                         ✗ spaces "initially" spaces "{" verbatim "}"
                           ✓ spaces ⇒  ""
                             ✓ space* ⇒  ""
                               ✗ space
                                 ✗ "\u0000".." "
                           ✗ "initially"
                       ✗ other
                         ✗ ~"initially" any
                           ✓ ~"initially" ⇒  ""
                             ✗ "initially"
                           ✗ any
                             ✗ any
    
    FAILED 
  Line 1, col 1:
  > 1 | 
        ^
  Expected any character or "raw"
             ✗ text
               ✗ macro+
                 ✗ macro
                     ✗ lex_RawClause
                       ✗ spaces "raw" spaces "{" verbatim "}"
                         ✓ spaces ⇒  ""
                           ✓ space* ⇒  ""
                             ✗ space
                               ✗ "\u0000".." "
                         ✗ "raw"
                     ✗ other
                       ✗ ~"raw" any
                         ✓ ~"raw" ⇒  ""
                           ✗ "raw"
                         ✗ any
                           ✗ any
  
          child0 = Omit Code Quotes._Omit Code Quotes (dispatcher, self, 'Omit Code Quotes')        child1 = Omit Comments._Omit Comments (dispatcher, self, 'Omit Comments')        child2 = Link Scraper._Link Scraper (dispatcher, self, 'Link Scraper')        child3 = MD File Reader._MD File Reader (dispatcher, self, 'MD File Reader')        conn0 = mpos.Connector ([mpos.Sender ('Omit Code Quotes', '[text]')], [mpos.Receiver ('Link Scraper', '[text]')])        conn1 = mpos.Connector ([mpos.Sender ('Omit Comments', 'text')], [mpos.Receiver ('Omit Code Quotes', 'text')])        conn2 = mpos.Connector ([mpos.Sender ('per file link scraper', 'filename')], [mpos.Receiver ('MD File Reader', 'filename')])        conn3 = mpos.Connector ([mpos.Sender ('Link Scraper', '[links]')], [mpos.Receiver ('per file link scraper', '[links]')])        conn4 = mpos.Connector ([mpos.Sender ('MD File Reader', 'text')], [mpos.Receiver ('Omit Comments', 'text')])        self.connections = [ conn0, conn1, conn2, conn3, conn4 ]        self.children = {'Omit Code Quotes':child0, 'Omit Comments':child1, 'Link Scraper':child2, 'MD File Reader':child3}

