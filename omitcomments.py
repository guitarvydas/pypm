import leaf
import re

class OmitComments (leaf.Leaf):
    def __init__ (self, parent, name): super().__init__ (parent, name)
    def handler (self, port, data):
        super ().handler (port, data)
        if (port == 'text'):
            result = re.sub (r'\#.*\n', '\n', data)
            self.send ('text', result)
    def call (self, text):
        self.handler ('text', text)
        return self.outputs2dict ()['text']

def testOmitComments ():
    tester = OmitComments (None, 'omitcomments')
    tester.handler ('text', 'abc\ndef #comment \n```\nthis\nis\ntest\ncode\n```\nghi')
    print (tester.outputs2dict ()['text'])

