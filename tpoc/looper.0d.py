# signature ≈❲Looper❳ {
#   inputs {➢❲any❳}
#   outputs {◦❲trigger❳}
#   }
# }


from message import Message
import leaf

class Looper (leaf.Leaf):
    def __init__ (self, parent, name): 
        super().__init__ (parent, name)

    def proc_a (self, message):
        self.send (self, 'trigger', True, message)

    def handler (self, message):
        super ().handler (message)
        self.on (message, ['default', 'any', self.proc_a])
