import leaf
import re
import os
import glob

class LinkToFilename (leaf.Leaf):
    def __init__ (self, parent, name): 
        super().__init__ (parent, name)
        self.basedirectory = ''
        self.suffix = ''
    def handler (self, port, data):
        super ().handler (port, data)
        if (port == 'base directory'):
            self.basedirectory = data + "/"
        elif (port == 'suffix'):
            self.suffix = data
        elif (port == 'link'):
            name1 = re.sub (r'\[\[', '', data)
            name2 = re.sub (r'\]\]', '', name1)
            name3 = self.basedirectory + '**/' + name2 + self.suffix
            fnames = glob.glob (name3, recursive=True)
            if (0 >= len (fnames)):
                errormessage = f'file not found /{name3}/'
                self.send ('error', )
            else:
                self.send ('filename', fnames [0])
            
# def testLinkToFilename ():
#     tester = LinkToFilename (None, 'link 2 filename')
#     bdir = '/Users/tarvydas/Dropbox/ps'
#     suffix = '.md'
#     s1 = '[[whyohm]]'
#     s1a = '[[pm math]]'
#     s2 = '[[ww-book-Hamburger Workbench - A Gentle Introduction to Ohm-JS/Why You Need To Learn Ohm-JS]]'
#     tester.handler ('base directory', bdir)
#     tester.handler ('suffix', suffix)
#     tester.handler ('link', s2)
#     fname = tester.outputs2dict ()['filename']
#     exists = os.path.exists (fname)
#     print (fname)
#     print (exists)

# testLinkToFilename ()

