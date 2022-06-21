Development of script for copying book parts for "Pattern Matching" using 0D components in Python.

See pm-copy.drawio.

See 0D parts:
- filereader.py
- omitcomments.py
- omitcodequotes.py
- pm.py

The first 3 are Leaves, whereas pm.py is a Container.

Blue parts are Leaf Implementations.

Grey part (pm.py) is a Container Implementation which coordinates / composes / routes fileread.py, omitcomments.py and omitcodequotes.py.
