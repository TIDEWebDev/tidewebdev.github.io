#!/bin/sh

cd $(dirname $0)
cd docs
python3 -m http.server
