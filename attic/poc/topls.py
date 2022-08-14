#!/usr/bin/env python3
import dispatcher
import ls
disp = dispatcher.Dispatcher ()
top = ls._ls (disp, None, '')
top.kickstart ()
disp.dispatch ()
