from message import Message
import leaf
import re

class OmitComments (leaf.Leaf):
    def __init__ (self, parent, name): super().__init__ (parent, name)
    def handler (self, message):
        super ().handler (message)
        if (message.port == 'text'):
            result = re.sub (r'\#.*\n', '\n', message.data)
            self.send (self, 'text', result, message)
    def call (self, text):
        self.handler (Message (self, 'text', text))
        return self.outputs2dict ()['text']

def testOmitComments ():
    tester = OmitComments (None, 'omitcomments')
    tester.handler (Message (tester, 'text', 'abc\ndef #comment \n```\nthis\nis\ntest\ncode\n```\nghi', []))
    print (tester.outputs2dict ()['text'])

# testOmitComments ()