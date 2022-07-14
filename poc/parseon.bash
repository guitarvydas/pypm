#!/bin/bash
cat ../../mac/mac.js parse/parseon.js >temp.js
node temp.js $1
