from message import Message

from echo import Echo

data = {'out': []} 
e = Echo (None, 'echo tester', data, 'instanceE')
e.inject (Message (None, '', data, None))
print ('injected')
outputs = e.run ()
print ('done:')
print (outputs)
