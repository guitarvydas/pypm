import re

from filtercomponent import FilterComponent

class LinkScraper (FilterComponent):
    def handle (self, message):
        data = message.data
        result = []
        for line in data ['lines']:
            print (line)
            result += re.findall ('(\[\[[^\]]+\]\])',line)
        data ['[links]'] = result

    def __init__ (self, parent, name, data):
        super ().__init__ (parent, name, self.handle)
        self.data = data
