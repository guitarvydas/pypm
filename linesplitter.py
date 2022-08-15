import re

from filtercomponent import FilterComponent

class LineSplitter (FilterComponent):
    def handle (self, message):
        data = message.data
        data ['lines'] = data ['md text'].split ('\n')

    def __init__ (self, parent, name, data):
        super ().__init__ (parent, name, self.handle)
        self.data = data
