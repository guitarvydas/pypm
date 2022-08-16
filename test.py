from message import Message

from helloworld import HelloWorld

data = {'out': []} 
hw = HelloWorld (None, 'hello world', data)
hw.inject (Message (None, '', data, None))
print ('injected')
hw.run ()
print ('done:')
print (data ['out'])
