#!/bin/bash

# Update setup.py, create a release, and run this script

rm -rf btcmd.egg-info dist
python3 setup.py sdist
twine upload dist/*