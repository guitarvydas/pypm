#!/usr/bin/env python3
import dispatcher
import omitcomments
disp = dispatcher.Dispatcher ()
top = omitcomments._omitcomments (disp, None, '')
top.kickstart ()
disp.dispatch ()
