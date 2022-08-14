from message import Message
import leaf
import shutil
import re
from ls import LS
from container import Container

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


class FixupReferencesToMDFiles (leaf.Leaf):
    def __init__ (self, parent, name): 
        super().__init__ (parent, name)
    def handler (self, message):
        super ().handler (message)
        if (message.port == 'filename'):
            filename = message.data
            result = self.fixupmd(filename)
            print (result)
        else:
            raise Exception (f"unrecognized message in Fixup References to MD Files '{message.port}'")
    def fixupmd (self, filename):
        f = open (filename, 'r')
        text = f.read ()
        subbed = re.sub (r'\[\[([^][]+)\]\]', dosubmd, text)
        return subbed


class FixupMDWrapper (Container):
    def __init__ (self, parent, name): 
        super().__init__ (parent, name)
        self.dirname = ''
        self.child_ls = LS (self, 'ls')
        self.child_fixupMD = FixupReferencesToMDFiles (self, 'fixup MD')
        self.children = [self.child_ls, self.child_fixupMD]
        self.connections = [
                { 'sender' : self, 'port' : 'directory', 'receivers' : [{'receiver' : self.child_ls, 'port':'directory' }]},
                { 'sender' : self, 'port' : 'start', 'receivers' : [{'receiver' : self.child_ls, 'port':'iterate' }]},
                { 'sender' : self, 'port' : 'notify', 'receivers' : [{'receiver' : self, 'port':'done' }]},
                { 'sender' : self.child_ls, 'port' : 'filename', 'receivers' : [{'receiver' : self.child_fixupMD, 'port':'filename' }]}
        ]
    def handler (self, message):
        super ().handler (message)
        self.delegateMessage (message)
        self.route ()
        self.runToCompletion ()
    

def testFixupReferencesToPNGFiles ():
    tester = FixupReferencesToPNGFiles (None, 'Fixup Reference To PNG Files')
    tester.handler (Message (tester, 'filename', 'test.md', []))
    tester.handler (Message (tester, 'start', True, []))

    
def testFixupReferencesToMDFiles ():
    tester = FixupReferencesToMDFiles (None, 'Fixup Reference To markdown Files')
    tester.handler (Message (tester, 'filename', 'test.md', []))
    tester.handler (Message (tester, 'start', True, []))

def testFixupMDWrapper ():
    tester = FixupMDWrapper (None, 'fixup markdown wrapper')
    tester.handler (Message (tester, 'directory', 'manuscript', []))
    tester.handler (Message (tester, 'start', True, []))
    tester.handler (Message (tester, 'notify', True, []))

#testFixupReferencesToPNGFiles ()
#testFixupReferencesToMDFiles ()
testFixupMDWrapper ()
