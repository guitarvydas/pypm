#!/usr/bin/env python3
import dispatcher
import re
import dev
disp = dispatcher.Dispatcher ()
top = dev._dev (disp, None, '')
top.kickstart ()
disp.dispatch ()
