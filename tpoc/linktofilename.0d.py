# signature ≈❲loop❳ {
#   inputs {➢❲base directory❳ ➢❲suffix❳ ➢❲link❳}
#   outputs {◦❲filename❳ ◦❲error❳}
#   }
# }

# convert an Obsidian link to an actual filename, in 'basedirectory' with suffix 'suffix'
# '[[abc]]' -> 'base/abc.suffix'
# '[[def.png]]' -> 'base/def.png' # do not add suffix for .png files

from message import Message
from event import On
import leaf
import re
import os
import glob

class LinkToFilename (Leaf):
    def __init__ (self, parent, name): 
        super().__init__ (parent, name)
        self.basedirectory = ''
        self.suffix = ''
    def proc_a (self, message):
        self.basedirectory = message.data + "/"
    def proc_b (self, message):
            self.suffix = message.data
    def proc_c (self, message):
        name1 = re.sub (r'\[\[', '', message.data)
        name2 = re.sub (r'\]\]', '', name1)
        if (None != re.search (r'\.png$', name2)):
            name3 = self.basedirectory + '**/' + name2 # leave .png filenames alone, don't add suffix
        else:
            name3 = self.basedirectory + '**/' + name2 + self.suffix
        fnames = glob.glob (name3, recursive=True)
        if (0 >= len (fnames)):
            errormessage = f'file not found /{name3}/'
            self.send (self, 'error', errormessage, message)
            # this is incomplete, need a StateChart to enclose all peer operations, that errors-out in this case
            raise Exception (f"LinkToFilename internal error '{errormessage}'")
        else:
            self.send (self, 'filename', fnames [0], message)

    def handler (self, message):
        super ().handler (message)
        self.switch (message, [On ('', 'base directory', self.proc_a),
                               On ('', 'suffix', self.proc_b)
                               On ('', 'link', self.proc_c)])
