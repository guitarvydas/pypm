## Synopsis

use: make

copy top.py to test.py, modify "kickstart" line to send a kick-off message into the top level

# WARTS in this bootstrap
- grouping is hard-wired to use id_1 (untrue)
- straight-through container.in->container.out is not supported
