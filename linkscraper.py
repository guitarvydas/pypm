from message import Message
import leaf
import re

class LinkScraper (leaf.Leaf):
    def __init__ (self, parent, name): super().__init__ (parent, name)
    def handler (self, message):
        result = []
        if (message.port == '[text]'):
            for line in message.data:
                result += re.findall ('(\[\[[^\]]+\]\])',line)
            self.send (self, '[links]', result)
    def call (self, textList):
        self.handler (Message ('[text]', textList))
        return self.outputs2dict ()['[links]']

def testScraper ():
    tester = LinkScraper (None, 'link scraper')
    tester.handler (Message (tester, '[text]', ['abc', '[[hello]]', 'def ', '[[xyz]]', 'ghi']))
    print (tester.outputs2dict ()['[links]'])

testScraper ()
