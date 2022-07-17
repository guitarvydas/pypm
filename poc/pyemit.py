#!/usr/bin/env python3

import sys
import json
import html
import re
import subprocess

with open(sys.argv[1]) as f:
  data = json.load(f)

def isContainer (component):
  if (0 < len (component["children"])):
      return True
  else:
      return False
       
def mkindent (n, file=""):
  s = ''
  while n > 0:
    s += ' '
    n -= 1
  return (s)

def mkLines (indent, str, file=""):
  s = ''
  for line in str.splitlines ():
    s += mkindent (indent)
    s += line
  return (s)

def js (commandlist, code):
  fname = "/tmp/temp.txt"
  with open (fname, "w") as outf:
    outf.write (code)
  r = subprocess.run (commandlist + [fname], capture_output=True, text=True)
  result = r.stdout
  if (r.stderr):
    print (r.stderr)
    return ''
  else:
    return result

def pythonifyname (s):
  r0 = re.sub (r' ', r'__', s)
  r = r0.lower ()
  return r

def indenter (s):
  r = js (["./indenter.bash"], s)
  return r

def filterinitsonly (s):
  r = js (["./parseinit.bash"], s)
  return r

def filteronsonly (s):
  r = js (["./parseon.bash"], s)
  return r

def filterrawsonly (s):
  r = js (["./parseraw.bash"], s)
  return r


def unescapeCode (s):
  if (0 >= len (s)):
    return ''
  
  code = html.unescape (s)
  # note that <p .../> and <span .../> and <pre .../> are not handled by the
  # code below (this probably needs a parser - e.g. Ohm-JS - to grok
  # It looks like we can get away, though, with the simplification below, because
  # draw.io creates paras and spans and pres in only very specific ways, if
  # we find a counter-example, it might be necessary to cut over to a
  # proper parse (e.g. using pfr and .ohm/.glue files))
  code0 = re.sub (r'%5C', "\\\\", code)
  code1a = re.sub (r'<pre([^>]*>)', '', code0)
  code1 = code1a.replace ("</pre>","")
#  code2 = re.sub (r'<div>([^<]*)</div>', r'\1\n', code1, re.MULTILINE)
  code2 = js (["./parsediv.bash"], code1)
  assert (None == re.search (r'<div>', code2)), "<div> not removed (internal error)"
  code3 = re.sub (r'<p ([^>]*)>', r'', code2)
  code4 = re.sub (r'</p>', "", code3)
  code5 = re.sub (r'<span ([^<]*)>', "", code4)
  code6 = re.sub (r'</span>', "\n", code5)
  code7a = re.sub (r'<br/>', "\n", code6)
  code7b = re.sub (r'<br>', "\n", code7a)
  code7 = re.sub (r'&nbsp;', " ", code7b)

  codefinal = html.unescape (code7)

  return codefinal
    

def mkCommonHeader (component):

  name = component["name"]
  idkey = component ["id"]
  inputs = component ["inputs"]
  outputs = component ["outputs"]
  sc = component ["synccode"]
  code = ''
  if (0 >= len (sc)):
    code = unescapeCode (sc)

  s = f'#!/usr/bin/env python3'
  s += f'\n# {fname}'
  s += f'\n# {idkey}'
  return (s)

def mkCommonImports (component):

  name = component["name"]
  idkey = component ["id"]
  inputs = component ["inputs"]
  outputs = component ["outputs"]
  code = unescapeCode (component["synccode"])

  s = "\nimport mpos"
  s += "\nimport dispatcher"
  s += "\nimport re"
  return (s)

def mkBeginCommonInit (component, cls):

  name = component["name"]
  # idkey = component ["id"]
  inputs = component ["inputs"]
  outputs = component ["outputs"]
  code = unescapeCode (component["synccode"])
  initcode = filterinitsonly (code)
  # rawcode = filterrawsonly (code)

  s = ''
  s += f'\nclass _{name} (mpos.{cls}):(.'
  s += f'\ndef __init__ (self, dispatcher, parent, idInParent):(.'
  s += f'\nsuper ().__init__ (dispatcher, parent, idInParent)'
  s += f'\nself.inputs={inputs}'
  s += f'\nself.outputs={outputs}'
  if (0 < len (initcode)):
    s += '\n' + initcode
  return (s)

def mkEndCommonInit (component, cls):
  return '.)'

def mkCommonRaw (component):

  # name = component["name"]
  # idkey = component ["id"]
  # inputs = component ["inputs"]
  # outputs = component ["outputs"]
  code = unescapeCode (component["synccode"])
  # initcode = filterinitsonly (code)
  rawcode = filterrawsonly (code)

  s = rawcode
  return (s)

def mkCommonBodyHead (component):

  name = component["name"]
  idkey = component ["id"]
  inputs = component ["inputs"]
  outputs = component ["outputs"]
  code = unescapeCode (component["synccode"])
  handlercode = filteronsonly (code)

  # for debugging bootstrap version
  badcode = (None != re.search ('FAILED', code))
  badhandler = (None != re.search ('FAILED', handlercode))
  if (badcode):
    raise Exception ('parse failure on code')
  if (badhandler):
    print (handlercode)
    raise Exception ('parse failure on handler')
  
  s = f'\ndef react (self, message):(.'
  s += '\nif (False):(.\npass.)'
  s += handlercode
  s += f'else:(.\nprint (self.idInParent + ": internal error unrecognized message: " + message.tag).)'
  return (s)

def mkCommonBodyTail (component):

  name = component["name"]
  idkey = component ["id"]
  inputs = component ["inputs"]
  outputs = component ["outputs"]
  code = unescapeCode (component["synccode"])

  s = f'\nreturn super ().react (message).)'
  return (s)
  

def mkLeafScript (component):
  if (component ["synccode"]):
    s = ''
    s += mkCommonHeader (component)
    s += mkCommonImports (component)
    s += mkBeginCommonInit (component, "Leaf")
    s += mkEndCommonInit (component, "Leaf")
    s += mkCommonRaw (component)
    s += mkCommonBodyHead (component)
    s += mkCommonBodyTail (component)
    return (s)
  else:
    print ("", file=sys.stderr)
    print (component)
    print ("*** Diagram Error - leaf contains no code", file=sys.stderr)
    print (component ["name"], file=sys.stderr)
    print ("", file=sys.stderr)
    assert False, "Diagram Error"

def formatMap (children):
  # print children surrounded by dq's (is there a better way to do this in Python?)
  mchildren = []
  i = 0
  for childname in children:
    mchildren.append ("'" + str (childname) + "'" + ":child" + str (i))
    i += 1
  return mchildren

def remapName (component, selfname):
  # current version of mpos expects self to be ''
  if (component == selfname):
    component = '';
  return component

def formatConnection (i, senderList, receiverList, selfname):
  senders = []
  for sender in senderList:
    component = f"{sender ['sender'] ['component']}"
    component = remapName (component, selfname)
    port = sender ['sender'] ['port']
    senders.append ("mpos.Sender ('" +  component + "', '" + port +  "')")
  receivers = []
  for receiver in receiverList:
    component = f"{receiver ['receiver'] ['component']}"
    component = remapName (component, selfname)
    port = receiver ['receiver'] ['port']
    receivers.append ("mpos.Receiver ('" +  component + "', '" + port +  "')")
  sstr = ", ".join(senders)
  rstr = ", ".join(receivers)
  retstr = f'\nconn{i} = mpos.Connector ([{sstr}], [{rstr}])'
  return retstr

def mkContainerScript (component):

  s = mkCommonHeader (component)

  name = component ["name"]
  idkey = component ["id"]
  inputs = component ["inputs"]
  outputs = component ["outputs"]
  code = ""  # no sync code for Containers

  children = component ["children"]
  connections = component ["connections"]

  s += mkCommonImports (component)
  for child in component ["children"]:
    name = pythonifyname (child)
    s += f'\nimport {name}'

  s += mkBeginCommonInit (component, "Container")

  # # uncomment to see json structure
  # # print (file)
  # # print (f'# {component}', file)
  # # print (file)
  
  j = 0
  for childname in children:
    name = pythonifyname (childname)
    s += f'\nchild{j} = {name}._{name} (dispatcher, self, \'{childname}\')'
    j += 1

  i = 0
  connectornames = []
  for conn in connections:
    receiverList = conn ["receivers"]
    senderList = conn ["senders"]

    cstr = formatConnection (i, senderList, receiverList, component["name"])
    s += f'        {cstr}'
    
    connectornames.append (f'conn{i}')
    i += 1
    
  mchildren = formatMap (children)
  
  s += f'\nself.connections = [ {", ".join (connectornames)} ]'
  s += '\nself.children = {' + f'{", ".join(mchildren)}' + '}'

  s += mkEndCommonInit (component, "Container")
  s += '\n' + mkCommonRaw (component)

  return (s)
  

def mkScript (component):
  s = ''
  if (isContainer (component)):
    s = mkContainerScript (component)
  else:
    s = mkLeafScript (component)
  s = indenter (s)
  return (s)
  
for componentArray in data:
  for component in componentArray:
    component['name'] = pythonifyname (component['name'])
    print (component['name'])
    fname = component["name"] + ".py"
    with open (fname, "w") as script:
      s = mkScript (component)
      print (s, file=script)

with open ('top.py', 'w') as top:
  print (f'#!/usr/bin/env python3', file=top)
  print (f'import dispatcher', file=top)
  print (f'import re', file=top)
  print (f'import {sys.argv [2]}', file=top)
  print (f'disp = dispatcher.Dispatcher ()', file=top)
  print (f"top = {sys.argv[2]}._{sys.argv [2]} (disp, None, '')", file=top)
  print (f'top.kickstart ()', file=top)
  print (f'disp.dispatch ()', file=top)




  
