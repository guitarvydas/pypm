#!/bin/bash
cat ../../../mac/mac.js parseinit.js >temp.js
node temp.js $1
