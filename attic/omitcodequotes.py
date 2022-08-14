from message import Message
import leaf
import re

def rmCodeQuotesState0 (textList):
    if (0 == len (textList)):
        return []
    else:
        first = textList [0];
        rest = textList [1:]
        if (first == '```'):
            return rmCodeQuotesState1 (rest)
        else:
            return [first] + rmCodeQuotesState0 (rest)
        
def rmCodeQuotesState1 (textList):
    if (0 == len (textList)):
        return []
    else:
        first = textList [0];
        rest = textList [1:]
        if (first == '```'):
            return rmCodeQuotesState0 (rest)
        else:
            return rmCodeQuotesState1 (rest)
        
class OmitCodeQuotes (leaf.Leaf):
    def __init__ (self, parent, name): super ().__init__ (parent, name)
    def handler (self, message):
        super ().handler (message)
        if (message.port == 'text'):
            text = message.data.split ('\n')
            result = rmCodeQuotesState0 (text)
            self.send (self, '[text]', result, message)
    def call (self, basename, link):
        self.handler (Message (self, 'basename', basename, []))
        self.handler (Message(self, 'link', link, []))
        return self.outputs2dict ()['[text]']

def testOmitCodeQuotes ():
    tester = OmitCodeQuotes (None, 'omit code quotes')
    tester.handler (Message (tester, 'text', 'abc\ndef\n```\nthis\nis\ntest\ncode\n```\nghi', []))
    print (tester.outputs2dict ()['[text]'])

# testOmitCodeQuotes ()
