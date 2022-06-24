from message import Message
import leaf
import container

class TestA (leaf.Leaf):
    def __init__ (self, parent, name): 
        super().__init__ (parent, name)
    def handler (self, message):
        super ().handler (message)
        if (message.port == 'inA'):
            self.send (self, 'outA', message.data + 'a')
        else:
            raise Exception (f'unrecognized message in TestA/{message.port}/')

class TestB (leaf.Leaf):
    def __init__ (self, parent, name): 
        super().__init__ (parent, name)
    def handler (self, message):
        super ().handler (message)
        if (message.port == 'inB'):
            self.send (self, 'outB', message.data + 'b')
        else:
            raise Exception (f'unrecognized message in TestB/{message.port}/')

class TestC (leaf.Leaf):
    def __init__ (self, parent, name): 
        super().__init__ (parent, name)
    def handler (self, message):
        super ().handler (message)
        if (message.port == 'inC'):
            self.send (self, 'outC', message.data + 'c')
        else:
            raise Exception (f'unrecognized message in TestC/{message.port}/')

class TestW (container.Container):
    def __init__ (self, parent, name): 
        super().__init__ (parent, name)
        self.childa = TestA (self, 'child a')
        self.children = [self.childa]
        self.connections = [
            { 'sender' : self, 'port' : 'inW', 'receivers' : [{'receiver' : self.childa, 'port':'inA'}]},
            { 'sender' : self.childa, 'port' : 'outA', 'receivers' : [{'receiver' : self, 'port':'outW'}]},
            ]
    def handler (self, message):
        super ().handler (message)
        self.delegateMessage (message)
        self.route ()
        self.runToCompletion ()

class TestX (container.Container):
    def __init__ (self, parent, name): 
        super().__init__ (parent, name)
        self.childa = TestA (self, 'child a')
        self.childb = TestB (self, 'child b')
        self.children = [self.childa, self.childb]
        self.connections = [
            { 'sender' : self, 'port' : 'inX', 'receivers' : [{'receiver' : self.childa, 'port':'inA'}]},
            { 'sender' : self.childa, 'port' : 'outA', 'receivers' : [{'receiver' : self.childb, 'port':'inB'}]},
            { 'sender' : self.childb, 'port' : 'outB', 'receivers' : [{'receiver' : self, 'port':'outX'}]},
            ]
    def handler (self, message):
        super ().handler (message)
        self.delegateMessage (message)
        self.route ()
        self.runToCompletion ()

class TestY (container.Container):
    def __init__ (self, parent, name): 
        super().__init__ (parent, name)
        self.childx = TestX (self, 'child x')
        self.children = [self.childx]
        self.connections = [
            { 'sender' : self, 'port' : 'inY', 'receivers' : [{'receiver' : self.childx, 'port':'inX'}]},
            { 'sender' : self.childx, 'port' : 'outX', 'receivers' : [{'receiver' : self, 'port':'outY'}]},
            ]
    def handler (self, message):
        super ().handler (message)
        self.delegateMessage (message)
        self.route ()
        self.runToCompletion ()
        
class TestZ (container.Container):
    def __init__ (self, parent, name): 
        super().__init__ (parent, name)
        self.childy = TestY (self, 'child y')
        self.childc = TestC (self, 'child c')
        self.children = [self.childy, self.childc]
        self.connections = [
            { 'sender' : self, 'port' : 'inZ', 'receivers' : [{'receiver' : self.childy, 'port':'inY'}]},
            { 'sender' : self.childy, 'port' : 'outY', 'receivers' : [{'receiver' : self.childc, 'port':'inC'}]},
            { 'sender' : self.childc, 'port' : 'outC', 'receivers' : [{'receiver' : self, 'port':'outZ'}]},
            ]
    def handler (self, message):
        super ().handler (message)
        self.delegateMessage (message)
        self.route ()
        self.runToCompletion ()
        

class TestP (container.Container):
    def __init__ (self, parent, name): 
        super().__init__ (parent, name)
        self.children = []
        self.connections = [
            { 'sender' : self, 'port' : 'inP', 'receivers' : [{'receiver' : self, 'port':'outP'}]}
            ]
    def handler (self, message):
        super ().handler (message)
        self.delegateMessage (message)
        self.route ()
        self.runToCompletion ()
        
        
class TestQ (container.Container):
    def __init__ (self, parent, name): 
        super().__init__ (parent, name)
        self.childa = TestA (self, 'child a')
        self.childb = TestB (self, 'child b')
        self.children = [self.childa, self.childb]
        self.connections = [
            { 'sender' : self, 'port' : 'inQ', 
              'receivers' : [
                  {'receiver' : self.childa, 'port':'inA'},
                  {'receiver' : self.childb, 'port':'inB'}
             ]
             },
            { 'sender' : self.childa, 'port' : 'outA', 'receivers' : []},
            { 'sender' : self.childb, 'port' : 'outB', 'receivers' : [{'receiver' : self, 'port':'outQ'}]},
            ]
    def handler (self, message):
        super ().handler (message)
        self.delegateMessage (message)
        self.route ()
        self.runToCompletion ()

def tester ():
    testa = TestA (None, 'test a')
    testb = TestB (None, 'test b')
    testc = TestC (None, 'test c')
    testw = TestW (None, 'test W')
    testx = TestX (None, 'test X')
    testy = TestY (None, 'test Y')
    testz = TestZ (None, 'test Z')
    testp = TestP (None, 'test P')
    testq = TestQ (None, 'test Q')
    testq.handler (Message (testp, 'inQ', 'q'))
    print (testq.outputs2dict ()['outQ'])

tester ()
