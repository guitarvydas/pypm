(.class Omit_Comments (Leaf):
 (.def __init__ (self, parent, name):
  (.super().__init__ (parent, name).).)
 (.def a ():
  result = re.sub (r'\#.*\n', '\n', message.data)
  self.send (self, 'text', result, message)
  .)
 (.def handler (self, message):
  if (False):
  (.pass.)
  elif (message.port == 'text'):
  (.self.a ().)
  .)
 
