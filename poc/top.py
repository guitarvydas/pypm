#!/usr/bin/env python3
import dispatcher
import re
import pm
disp = dispatcher.Dispatcher ()
top = pm._pm (disp, None, '')
top.kickstart ()
disp.dispatch ()
