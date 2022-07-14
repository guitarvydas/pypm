#!/bin/bash
cat ../../../mac/mac.js parseon.js >temp.js
node temp.js $1
