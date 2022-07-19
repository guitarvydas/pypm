# signature ≈❲Omit Code Quotes❳ {
#   inputs {➢❲text❳}
#   outputs {◦❲[text]❳}
#   }
# }

# # implementation ≈❲Omit Code Quotes❳ leaf {
# #   proc č❲a❳ {
# #     ⟪result = re.sub (r'\#.*\n', '\n', message.data)⟫
# #     ⟪self.send (self, 'text', result, message)⟫
# #   }

# #   on ➢❲text❳ {callproc č❲a❳}

# # }



from message import Message
import leaf
import re
class Omit__Code__Quotes (leaf.Leaf):
    def __init__ (self, parent, name): super ().__init__ (parent, name)

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
            
    def proc_a (self):
        text = message.data.split ('\n')
        result = self.rmCodeQuotesState0 (text)
        self.send (self, '[text]', result, message)

    def handler (self, message):
        super ().handler (message)
        self.on (message, ['default', 'text', self.proc_a])
