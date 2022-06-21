import leaf
import re

class LinkScraper (leaf.Leaf):
    def __init__ (self, parent, name): super().__init__ (parent, name)
    def handler (self, port, data):
        result = []
        if (port == '[text]'):
            for line in data:
                result += re.findall ('(\[\[[^\]]+\]\])',line)
            self.send ('[links]', result)
    def call (self, textList):
        self.handler ('[text]', textList)
        return self.outputs2dict ()['[links]']

def testScraper ():
    tester = LinkScraper (None, 'link scraper')
    tester.handler ('[text]', ['abc', '[[hello]]', 'def ', '[[xyz]]', 'ghi'])
    print (tester.outputs2dict ()['[links]'])

# testScraper ()