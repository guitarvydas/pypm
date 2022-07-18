#!/usr/bin/env python3
import dispatcher
import mpos
import pm
disp = dispatcher.Dispatcher ()
top = pm._pm (disp, None, '')
m = mpos.InputMessage ('', 'filename', 'test.md')
top.enqueueInput (m)
disp.dispatch ()
for m in top.outputsAsList ():
    print (f'tag={m.tag} data={m.data}')
