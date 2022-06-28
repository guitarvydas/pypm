from message import Message
import leaf
import shutil
import re


class FixupReferencesToPNGFiles (leaf.Leaf):
    def __init__ (self, parent, name): 
        super().__init__ (parent, name)
        self.filename = ''
    def handler (self, message):
        super ().handler (message)
        if (message.port == 'filename'):
            self.filename = message.data
        elif (message.port == 'start'):
            result = self.fixup(self.filename)
            print (result)
        else:
            raise Exception (f"unrecognized message in Fixup References to PNG Files '{message.port}'")

    def fixup (self, filename):
        f = open (filename, 'r')
        text = f.read ()
        subbed = re.sub (r'\[\[([^][]+\.png)\]\]', dosub, text)
        return subbed

def dosub (match):
    sub1 = match.group (1)
    sub2 = markua (sub1)
    sub = f'![resources/{sub2}]'
    return sub

def dosubmd (match):
    sub1 = match.group (1)
    sub2 = markua (sub1)
    sub = f'![{sub2}.md]'
    return sub


def markua (s):
    return s.replace ('\n', '').strip ().lower ().replace (' ', '--')

class FixupReferencesToMDFiles (leaf.Leaf):
    def __init__ (self, parent, name): 
        super().__init__ (parent, name)
        self.filename = ''
    def handler (self, message):
        super ().handler (message)
        if (message.port == 'filename'):
            self.filename = message.data
        elif (message.port == 'start'):
            result = self.fixupmd(self.filename)
            print (result)
        else:
            raise Exception (f"unrecognized message in Fixup References to MD Files '{message.port}'")
    def fixupmd (self, filename):
        f = open (filename, 'r')
        text = f.read ()
        subbed = re.sub (r'\[\[([^][]+)\]\]', dosubmd, text)
        return subbed




def testFixupReferencesToPNGFiles ():
    tester = FixupReferencesToPNGFiles (None, 'Fixup Reference To PNG Files')
    tester.handler (Message (tester, 'filename', 'test.md', []))
    tester.handler (Message (tester, 'start', True, []))

    
def testFixupReferencesToMDFiles ():
    tester = FixupReferencesToMDFiles (None, 'Fixup Reference To markdown Files')
    tester.handler (Message (tester, 'filename', 'test.md', []))
    tester.handler (Message (tester, 'start', True, []))

#testFixupReferencesToPNGFiles ()
testFixupReferencesToMDFiles ()
