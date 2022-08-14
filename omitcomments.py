import re
from filtercomponent import FilterComponent

class OmitComments (FilterComponent):
    def handle (self, message):
        data = message.data
        result = re.sub (r'\#.*\n', '\n', data ["input text"])
        data ["text"] = result

    def __init__ (self, parent, name):
        super ().__init__ (parent, name, self.handle)
