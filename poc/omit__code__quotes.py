
#!/usr/bin/env python3
# omit__code__quotes.py
# cell_11
import mpos
import dispatcher
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
              return rmCodeQuotesState1 (rest)
          else:
              return [first] + rmCodeQuotesState0 (rest)
          
  def rmCodeQuotesState1 (textList):
      if (0 == len (textList)):
          return []
      else:
          first = textList [0];
          rest = textList [1:]
          if (first == '```'):
              return rmCodeQuotesState0 (rest)
          else:
              return rmCodeQuotesState1 (rest)
  
  
  def react (self, inputMessage):
    if (False):
      pass
    elif (message.port == "text"):
      
          text = message.data.split ('\n')
          result = rmCodeQuotesState0 (text)
          self.send (self, '[text]', result, message)
      
    
    return super ().react (inputMessage)

