import re

from porthandler import PortHandler
from filtercomponent import FilterComponent

class LinkScraper (FilterComponent):
    def __init__ (self, parent, name, data, instanceData):
        super ().__init__ (parent, name, self.handle)
        self.data = data
        self.instanceData = instanceData
        h1 = PortHandler ( '', self.f1)
        self.handlerFunctions = [h1]

        def f1 (self, message):                           
            result = []
            for line in message.data ['lines']:
                result += re.findall ('(\[\[[^\]]+\]\])',line)
            data ['[links]'] = result
