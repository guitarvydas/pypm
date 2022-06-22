import leaf
import re
import os

class LinkCollection (leaf.Leaf):
    def __init__ (self, parent, name): 
        super().__init__ (parent, name)
        self.links = []
        self.state = 'idle'
    def handler (self, port, data):
        super ().handler (port, data)
        if (self.state == 'idle'):
            if (port == '[append list]'):
                # data is a list of links, each item a string of the form '[[abc]]'
                self.links = self.links + data
                self.state = 'appending'
            else:
                raise Exception (f'unrecognized message in state idle /{port}/')
        elif (self.state == 'appending'):
            if (port == '[append list]'):
                self.links = self.links + data
            elif (port == 'req next'):
                if (0 >= len (self.links)):
                    self.send ('no more', True)
                    self.send ('link', '')
                    self.state = 'idle'
                else:
                    link = self.links.pop (0)
                    self.send ('link', link)
            else:
                raise Exception (f'unrecognized message in state appending /{port}/')
            
# def testLinkCollection ():
#     tester = LinkCollection (None, 'link collection')
#     links = ['[[abc]]', '[[def]]']
#     links2 = ['[[ghi]]', '[[jkl]]', '[[mno]]']
#     tester.handler ('[append list]', links)
#     tester.handler ('req next', True)
#     tester.handler ('[append list]', links2)
#     tester.handler ('req next', True)
#     tester.handler ('req next', True)
#     tester.handler ('req next', True)
#     tester.handler ('req next', True)
#     tester.handler ('req next', True)
#     # -- one too many - raises error -- tester.handler ('req next', True)
#     print (tester.outputs2dict ())

# testLinkCollection ()

