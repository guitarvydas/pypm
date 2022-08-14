# signature ≈❲Link Scraper❳ {
#   inputs {➢❲text❳}
#   outputs {◦❲[links]❳}
#   }
# }

from fifo import FIFO
from message import Message
import leaf
import re

class LinkScraper (leaf.Leaf):
    def __init__ (self, parent, name): super().__init__ (parent, name)

    def proc_a (self, message):
        for line in message.data:
            result += re.findall ('(\[\[[^\]]+\]\])',line)
            self.send (self, '[links]', result, message)

    def step (self, message):
        super ().handler (message)
        result = []
        self.on (messge, ['default', '[text]', self.proc_a])

    def reset (self):
        pass
        
