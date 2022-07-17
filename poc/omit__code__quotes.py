
#!/usr/bin/env python3
# omit__code__quotes.py
# cell_11
import mpos
import dispatcher
import re
class _omit__code__quotes (mpos.Leaf):
  def __init__ (self, dispatcher, parent, idInParent):
    super ().__init__ (dispatcher, parent, idInParent)
    self.inputs=['text']
    self.outputs=['[text]']
    
    
    def rmCodeQuotesState0 (textList):
        if (0 == len (textList)):
            return []
        else:
            first = textList [0];
            rest = textList [1:]
            if (first == '```'):
                return self.rmCodeQuotesState1 (rest)
            else:
                return [first] + self.rmCodeQuotesState0 (rest)
            
    def rmCodeQuotesState1 (textList):
        if (0 == len (textList)):
            return []
        else:
            first = textList [0];
            rest = textList [1:]
            if (first == '```'):
                return self.rmCodeQuotesState0 (rest)
            else:
                return self.rmCodeQuotesState1 (rest)
    
    
  def react (self, message):
    if (False):
      pass
    elif (message.tag == "text"):
      
          text = message.data.split ('\n')
          result = self.rmCodeQuotesState0 (text)
          self.send ('[text]', result)
      
    else:
      print (self.idInParent + ": internal error unrecognized message: " + message.tag)
    return super ().react (message)

