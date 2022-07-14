#!/bin/bash
cat ../../mac/mac.js parse/parseinit.js >temp.js
node temp.js $1
