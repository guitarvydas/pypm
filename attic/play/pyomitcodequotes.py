#!/usr/bin/env python3
import message
import mpos
import dispatcher
class _Character__by__Character (mpos.Leaf):
  def __init__ (self, dispatcher, parent, idInParent):
    super ().__init__ (dispatcher, parent, idInParent)
    self.inputs=['text', 'req']
    self.outputs=['char', 'no more']
    self.text = ''
    self.state = exit__default
    self.enters = {'default':enter__default, 'outputting':enter__outputting}
    self.exits = {'default':exit__default, 'outputting':exit__outputting}

  def next (self, newstate):
      exitfunction = self.exits [self.state]
      exitfunction ();
      enterfunction = self.enters [newstate]
      enterfunction ();
      self.state = newstate
      
  def enter__default (self):
      pass
  def enter__outputting (self):
      pass
  def exit__default (self):
      pass
  def exit__outputting (self):
      pass

  def sendOneCharacterOrFinalize (self):
      if (0 >= len (self.text)):
          self.send (self, 'no more', True, message)
          self.next ('default')
      else:
          c = firstchar (self.text)
          self.text = allbutfirst (self.text)
          self.send (self, 'char', c, message)

  def react (self, inputMessage):
    if (False):
      pass
    elif (self.state == 'default'):
        if (message.port == "text"):
            self.text = message.data
        elif (message.port == "req"):
            sendOneCharacterOrFinalize (self)
    elif (self.state == 'outputting'):
        if (message.port == "req"):
            sendOneCharacterOrFinalize (self)
    return super ().react (inputMessage)
    
def test ():
    component = _Character__by__Character ()
    component.send (Message (component, 'text', "a", []))
    component.send (Message (component, 'req', True, []))
    print (component.outputs2dict ())
