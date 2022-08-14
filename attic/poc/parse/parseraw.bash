#!/bin/bash
cat ../../../mac/mac.js parseraw.js >temp.js
node temp.js $1
