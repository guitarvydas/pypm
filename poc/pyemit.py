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
       
def printIndent (n, file=""):
  while n > 0:
    print (" ", end="", file=file)
    n -= 1
    
def printLines (indent, str, file=""):
  for line in str.splitlines ():
    printIndent (indent, file=file);
    print (line, file=file)


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

def indenter (s):
  r = js (["./indenter.bash"], s)
  return r

def filterinitsonly (s):
  r = js (["./parseinit.bash"], s)
  return r

def filteronsonly (s):
  r = js (["./parseon.bash"], s)
  return r


def unescapeCode (s):
  code = html.unescape (s)
  # note that <p .../> and <span .../> and <pre .../> are not handled by the
  # code below (this probably needs a parser - e.g. Ohm-JS - to grok
  # It looks like we can get away, though, with the simplification below, because
  # draw.io creates paras and spans and pres in only very specific ways, if
  # we find a counter-example, it might be necessary to cut over to a
  # proper parse (e.g. using pfr and .ohm/.glue files))
  code1a = re.sub (r'<pre([^>]*>)', '', code)
  code1 = code1a.replace ("</pre>","")
#  code2 = re.sub (r'<div>([^<]*)</div>', r'\1\n', code1, re.MULTILINE)
  code2 = js (["./parsediv.bash"], code1)
  assert (None == re.search (r'<div>', code2)), "<div> not removed (internal error)"
  code3 = re.sub (r'<p ([^>]*)>', r'', code2)
  code4 = re.sub (r'</p>', "", code3)
  code5 = re.sub (r'<span ([^<]*)>', "", code4)
  code6 = re.sub (r'</span>', "\n", code5)
  code7a = re.sub (r'<br/>', "\n", code6)
  code7 = re.sub (r'<br>', "\n", code7a)

  codefinal = html.unescape (code7)

  return codefinal
    

def printCommonHeader (component, outf):

  name = component["name"]
  idkey = component ["id"]
  inputs = component ["inputs"]
  outputs = component ["outputs"]
  code = unescapeCode (component["synccode"])

  print (f'#!/usr/bin/env python3', file=outf)
  print (f'# {fname}', file=outf)
  print (f'# {idkey}', file=outf)

def printCommonImports (component, outf):

  name = component["name"]
  idkey = component ["id"]
  inputs = component ["inputs"]
  outputs = component ["outputs"]
  code = unescapeCode (component["synccode"])

  print ("import mpos", file=outf)
  print ("import dispatcher", file=outf)

def printCommonInit (component, outf, cls):

  name = component["name"]
  idkey = component ["id"]
  inputs = component ["inputs"]
  outputs = component ["outputs"]
  code = unescapeCode (component["synccode"])
  initcode = filterinitsonly (code)

  s = ''
  s += f'class _{name} (mpos.{cls}):(.'
  s += f'\ndef __init__ (self, dispatcher, parent, idInParent):(.'
  s += f'\nsuper ().__init__ (dispatcher, parent, idInParent)'
  s += f'\nself.inputs={inputs}'
  s += f'\nself.outputs={outputs}'
  s +=  '\n' + initcode + '.).)'
  s = indenter (s)
  print (s, file=outf)

def printCommonBodyHead (component, outf):

  name = component["name"]
  idkey = component ["id"]
  inputs = component ["inputs"]
  outputs = component ["outputs"]
  code = unescapeCode (component["synccode"])
  handlercode = filteronsonly (code)

  s = f'def react (self, inputMessage):(.'
  s += '\nif (False):(.\npass.)'
  s += handlercode
  s = indenter (s)
  print (s, file=outf, end='')

def printCommonBodyTail (component, outf):

  name = component["name"]
  idkey = component ["id"]
  inputs = component ["inputs"]
  outputs = component ["outputs"]
  code = unescapeCode (component["synccode"])

  print (f'\nreturn super ().react (inputMessage).)', file=outf)
  s = f'\nreturn super ().react (inputMessage).)'
  print (s, file=outf)
  

def printLeafScript (component, outf):
  if (component ["synccode"]):
    printCommonHeader (component, outf)
    printCommonImports (component, outf)
    printCommonInit (component, outf, "Leaf")
    printCommonBodyHead (component, outf)
    printCommonBodyTail (component, outf)
  else:
    print ("", file=sys.stderr)
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
  retstr = f'conn{i} = mpos.Connector ([{sstr}], [{rstr}])'
  return retstr

def printContainerScript (component, outf):

  printCommonHeader (component, outf)

  name = component ["name"]
  idkey = component ["id"]
  inputs = component ["inputs"]
  outputs = component ["outputs"]
  code = ""  # no sync code for Containers

  children = component ["children"]
  connections = component ["connections"]

  printCommonImports (component, outf)
  for child in component ["children"]:
    print (f'import {child}', file=outf)

  printCommonInit (component, outf, "Container")

  # # uncomment to see json structure
  # # print (file=outf)
  # # print (f'# {component}', file=outf)
  # # print (file=outf)
  
  print (file=outf)

  j = 0
  for childname in children:
    print (f'        child{j} = {childname}._{childname} (dispatcher, self, \'{childname}\')', file=outf)
    j += 1

  i = 0
  connectornames = []
  for conn in connections:
    receiverList = conn ["receivers"]
    senderList = conn ["senders"]

    cstr = formatConnection (i, senderList, receiverList, component["name"])
    print (f'        {cstr}', file=outf)
    
    connectornames.append (f'conn{i}')
    i += 1
    
  mchildren = formatMap (children)
  
  print (f'        self.connections = [ {", ".join (connectornames)} ]', file=outf)
  print ('        self.children = {' + f'{", ".join(mchildren)}' + '}', file=outf)

  

def printScript (component, outf):
  if (isContainer (component)):
    printContainerScript (component, outf)
  else:
    printLeafScript (component, outf)

for componentArray in data:
  for component in componentArray:
    fname = component["name"] + ".py"
    with open (fname, "w") as script:
      printScript (component, script)

with open ('top.py', 'w') as top:
  print (f'#!/usr/bin/env python3', file=top)
  print (f'import dispatcher', file=top)
  print (f'import {sys.argv [2]}', file=top)
  print (f'disp = dispatcher.Dispatcher ()', file=top)
  print (f"top = {sys.argv[2]}._{sys.argv [2]} (disp, None, '')", file=top)
  print (f'top.kickstart ()', file=top)
  print (f'disp.dispatch ()', file=top)




  
