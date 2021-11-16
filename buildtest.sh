#!/bin/bash

set -e

./.env/bin/python3.8 -m pip install .
./.env/bin/python3.8 -m pytest .
