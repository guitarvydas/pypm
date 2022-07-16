#!/usr/bin/env python3
import dispatcher
import mdfilereader
disp = dispatcher.Dispatcher ()
top = mdfilereader._mdfilereader (disp, None, '')
top.kickstart ()
disp.dispatch ()
