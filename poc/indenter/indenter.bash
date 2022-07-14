#!/bin/bash
cat ../../../mac/mac.js indenter.js >temp.js
node temp.js $1
