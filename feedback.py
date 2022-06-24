from message import Message
import leaf
import container
import looptrigger

class Counter (leaf.Leaf):
    def __init__ (self, parent, name):
        super().__init__ (parent, name)
        self.count = 0
    def handler (self, message):
        super ().handler (message)
        if (message.port == 'count'):
            print (self.count)
            self.count = self.count + 1
            if (self.count < 5):
                self.send (self, 'trigger', True)
            else:
                self.send (self, 'final', self.count)
        else:
            raise "unknown port for Counter /{message.port}/"

class Feedback (container.Container):
    def __init__ (self, parent, instanceName):
        super ().__init__ (parent, instanceName)
        self.child1 = Counter (self, 'counter')
        self.child2 = looptrigger.LoopTrigger (self, 'loop trigger')
        self.children = [self.child1, self.child2]
        self.connections = [
            {'sender': self, 'port' : 'start', 'receivers' : [{'receiver' : self.child1, 'port':'count' }]},
            {'sender': self.child1, 'port':'trigger', 'receivers':[{'receiver':self.child2, 'port':'any'}]},
            {'sender': self.child1, 'port':'final', 'receivers':[{'receiver':self, 'port':'output'}]},
            {'sender': self.child2, 'port':'trigger', 'receivers':[{'receiver':self.child1, 'port':'count'}]}
        ]
    def handler (self, message):
        super ().handler (message)
        self.delegateMessage (message)
        self.route ()
        self.runToCompletion ()

def testFeedback ():
    tester = Feedback (None, 'feedback tester')
    tester.handler (Message (tester, 'start', True))
    print (f"final output: {tester.outputs2dict ()['output']}")

testFeedback ()

