
#!/usr/bin/env python3
# omit__code__quotes.py
# cell_16
import mpos
import dispatcher
import re
class _omit__code__quotes (mpos.Container):
  def __init__ (self, dispatcher, parent, idInParent):
    super ().__init__ (dispatcher, parent, idInParent)
    self.inputs=['text']
    self.outputs=['[text]']
    
    
    self.connections = [  ]
    self.children = {}
  
  def rmCodeQuotesState0 (self, textList):
      if (0 == len (textList)):
          return []
      else:
          first = textList [0];
          rest = textList [1:]
          if (first == '```'):
              return self.rmCodeQuotesState1 (rest)
          else:
              return [first] + self.rmCodeQuotesState0 (rest)
          
  def rmCodeQuotesState1 (self, textList):
      if (0 == len (textList)):
          return []
      else:
          first = textList [0];
          rest = textList [1:]
          if (first == '```'):
              return self.rmCodeQuotesState0 (rest)
          else:
              return self.rmCodeQuotesState1 (rest)
  
  

