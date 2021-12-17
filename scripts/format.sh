#!/bin/sh -e

set -x

isort main.py models.py --force-single-line-imports
autoflake --remove-all-unused-imports --recursive --remove-unused-variables main.py models.py --exclude=__init__.py
black main.py models.py
isort main.py models.py