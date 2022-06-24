from message import Message
import leaf
import re
import os
import glob

class LinkToFilename (leaf.Leaf):
    def __init__ (self, parent, name): 
        super().__init__ (parent, name)
        self.basedirectory = ''
        self.suffix = ''
    def handler (self, message):
        super ().handler (message)
        if (message.port == 'base directory'):
            self.basedirectory = message.data + "/"
        elif (message.port == 'suffix'):
            self.suffix = message.data
        elif (message.port == 'link'):
            print (f"link to filname '{message.data}'")
            name1 = re.sub (r'\[\[', '', message.data)
            name2 = re.sub (r'\]\]', '', name1)
            if (None != re.search (r'\.png$', name2)):
                name3 = self.basedirectory + '**/' + name2 # leave .png filenames alone, don't add suffix
            else:
                name3 = self.basedirectory + '**/' + name2 + self.suffix
            fnames = glob.glob (name3, recursive=True)
            if (0 >= len (fnames)):
                errormessage = f'file not found /{name3}/'
                self.send (self, 'error', errormessage)
                # this is incomplete, need a StateChart to enclose all peer operations, that errors-out in this case
                raise Exception (f"LinkToFilename internal error '{errormessage}'")
            else:
                self.send (self, 'filename', fnames [0])
            
# def testLinkToFilename ():
#     tester = LinkToFilename (None, 'link 2 filename')
#     bdir = '/Users/tarvydas/Dropbox/ps'
#     suffix = '.md'
#     s1 = '[[whyohm]]'
#     s1a = '[[pm math]]'
#     s2 = '[[ww-book-Hamburger Workbench - A Gentle Introduction to Ohm-JS/Why You Need To Learn Ohm-JS]]'
#     tester.handler (Message (self, 'base directory', bdir))
#     tester.handler (Message (self, 'suffix', suffix))
#     tester.handler (Message (self, 'link', s2))
#     fname = tester.outputs2dict ()['filename']
#     exists = os.path.exists (fname)
#     print (fname)
#     print (exists)

# testLinkToFilename ()

