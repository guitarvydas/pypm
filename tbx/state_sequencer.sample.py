def in_idle (self, message):
    if (False):
        pass
    elif (message ['port'] == 'start'):
        self.a ()
	self.exit_idle ()
	self.enter_step1 ()
	self.state = 'step 1'
    else:
        raise f'unkown message in script_sequencer/idle {message ["port"]}'
        
def enter_idle (self):
    pass
def exit_idle (self):
    pass


def in_step1 (self, message):
    if (False):
        pass
    elif (message ['port'] == 'done₁'):
        self.b ()
	self.exit_step1 ()
	self.enter_step2 ()
	self.state = 'step 2'
    else:
        raise f'unkown message in script_sequencer/step1 {message ["port"]}'
        
def enter_step1 (self):
    pass
def exit_step1 (self):
    pass

def in_step2 (self, message):
    if (False):
        pass
    elif (message ['port'] == 'done₂'):
        self.c ()
	self.exit_step2 ()
	self.enter_step3 ()
	self.state = 'step 3'
    else:
        raise f'unkown message in script_sequencer/step2 {message ["port"]}'
        
def enter_step2 (self):
    pass
def exit_step2 (self):
    pass


def in_step3 (self, message):
    if (False):
        pass
    elif (message ['port'] == 'done₃'):
        self.d ()
	self.exit_step3 ()
	self.enter_step4 ()
	self.state = 'step 4'
    else:
        raise f'unkown message in script_sequencer/step3 {message ["port"]}'
        
def enter_step3 (self):
    pass
def exit_step3 (self):
    pass

def in_step4 (self, message):
    if (False):
        pass
    elif (message ['port'] == 'done₄'):
        self.e ()
	self.exit_step4 ()
	self.enter_idle ()
	self.state = 'idle'
    else:
        raise f'unkown message in script_sequencer/step4 {message ["port"]}'
        
def enter_step4 (self):
    pass
def exit_step4 (self):
    pass


def script_sequencer (self, message):
    if (self.state == 'idle'):
        self.in_idle (message)
    elif (self.state == 'step 1'):
        self.in_step1 (message)
    elif (self.state == 'step 2'):
        self.in_step2 (message)
    elif (self.state == 'step 3'):
        self.in_step3 (message)
    elif (self.state == 'step 4'):
        self.in_step4 (message)
    else:
        raise f'unknown state in script_sequencer {self.state}`
