#!/usr/bin/env bash

set -e
set -x

flake8 main.py models.py
black main.py models.py --check
isort main.py models.py --check-only