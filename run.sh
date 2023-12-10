#!/bin/bash

source ~/anaconda3/etc/profile.d/conda.sh
conda activate fooocus

python entry_with_update.py --preset $1 --disable-auto-launch --disable-analytics

