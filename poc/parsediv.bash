#!/bin/bash
cat ../../mac/mac.js divwalker/divwalker.js >temp.js
node temp.js $1
