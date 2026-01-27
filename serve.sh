#!/bin/sh

cd $(dirname $0)
cd docs
if python3 -m http.server
then
  echo Called with Python3
else
  python -m http.server
  echo Called with Python
fi
