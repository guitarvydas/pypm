import re

from filtercomponent import FilterComponent

class World (FilterComponent):
    def handle (self, message):
        data = message.data
        data ['out'].append ('world')

    def __init__ (self, parent, name, data):
        super ().__init__ (parent, name, self.handle)
        self.data = data
