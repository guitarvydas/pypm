# signature ≈❲MD File Reader❳ {
#   inputs {➢❲filename❳}
#   outputs {◦❲text❳}
#   }
# }

from message import Message
import leaf
import re

class MD__File__Reader (leaf.Leaf):
    def __init__ (self, parent, name): 
        super ().__init__ (parent, name)

    def handler (self, message):
        self.on (message, ['default', 'filename', self.proc_a])
        
    def proc_a (self, message):
        if (re.search (r'\.md$', message.data)):
            f = open (message.data, 'r')
            result = f.read ()
            self.send (self, 'text', result, message)
        else:
            self.send (self, 'text', '', message)
