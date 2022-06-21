import leaf
import re
import os

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
            fname = self.basedirectory + name2 + self.suffix
            self.send ('filename', os.path.realpath (fname))
            
def testLinkToFilename ():
    tester = LinkToFilename (None, 'link 2 filename')
    bdir = 'xyz'
    suffix = '.md'
    s1 = '[[whyohm]]'
    s2 = '[[ww-book-Hamburger Workbench - A Gentle Introduction to Ohm-JS/Why You Need To Learn Ohm-JS]]'
    tester.handler ('base directory', bdir)
    tester.handler ('suffix', suffix)
    tester.handler ('link', s2)
    print (tester.outputs2dict ()['filename'])

testLinkToFilename ()

