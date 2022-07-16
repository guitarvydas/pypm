#!/bin/bash
cat ../../mac/mac.js parse/parseraw.js >temp.js
node temp.js $1
