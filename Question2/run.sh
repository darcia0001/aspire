#!/bin/bash

# CSV path
#shoul give the path
FILE_PATH="data/dataset-list.csv"

# Python run.
source venv/bin/activate
python code/ebola-dataset-list.py $FILE_PATH
