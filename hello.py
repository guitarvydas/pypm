import re

from filtercomponent import FilterComponent

class Hello (FilterComponent):
    def handle (self, message):
        data = message.data
        data ['out'].append (self.instanceData)

    def __init__ (self, parent, name, data, instanceData):
        super ().__init__ (parent, name, self.handle)
        self.data = data
        self.instanceData = instanceData
