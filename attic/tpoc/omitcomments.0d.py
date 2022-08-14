# signature ≈❲Omit Comments❳ {
#   inputs {➢❲text❳}
#   outputs {◦❲text❳}
#   }
# }

# implementation ≈❲Omit Comments❳ leaf {
#   proc č❲a❳ {
#     ⟪result = re.sub (r'\#.*\n', '\n', message.data)⟫
#     ⟪self.send (self, 'text', result, message)⟫
#   }

#   on ➢❲text❳ {callproc č❲a❳}

# }


from fifo import FIFO
from message import Message
import leaf
import re

class Omit__Comments (leaf.Leaf):
    def __init__ (self, parent, name): super().__init__ (parent, name)

    def proc_a (self):
        result = re.sub (r'\#.*\n', '\n', message.data)
        self.send (self, 'text', result, message)

    def step (self, message):
        super ().handler (message)
        self.on (message, ['default', 'text', self.proc_a])

    def reset (self):
        pass
