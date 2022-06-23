from message import Message
import leaf
import re
import os

class LinkCollection (leaf.Leaf):
    def __init__ (self, parent, name): 
        super().__init__ (parent, name)
        self.links = []
        self.state = 'idle'
    def handler (self, message):
        super ().handler (message)
        print (f'link collection.[{self.state}]')
        if (self.state == 'idle'):
            if (message.port == '[append list]'):
                # data is a list of links, each item a string of the form '[[abc]]'
                self.links = self.links + message.data
                self.state = 'appending'
            else:
                raise Exception (f'unrecognized message in state idle /{message.port}/')
        elif (self.state == 'appending'):
            if (message.port == '[append list]'):
                self.links = self.links + message.data
            elif (message.port == 'req next'):
                if (0 >= len (self.links)):
                    self.send (self, 'no more', True)
                    self.send (self, 'link', '')
                    self.state = 'idle'
                else:
                    link = self.links.pop (0)
                    self.send (self, 'link', link)
            else:
                raise Exception (f'unrecognized message in state appending /{message.port}/')
            
# def testLinkCollection ():
#     tester = LinkCollection (None, 'link collection')
#     links = ['[[abc]]', '[[def]]']
#     links2 = ['[[ghi]]', '[[jkl]]', '[[mno]]']
#     tester.handler (self, '[append list]', links)
#     tester.handler (self, 'req next', True)
#     tester.handler (self, '[append list]', links2)
#     tester.handler (self, 'req next', True)
#     tester.handler (self, 'req next', True)
#     tester.handler (self, 'req next', True)
#     tester.handler (self, 'req next', True)
#     tester.handler (self, 'req next', True)
#     # -- one too many - raises error -- tester.handler (self, 'req next', True)
#     print (tester.outputs2dict ())

# testLinkCollection ()

