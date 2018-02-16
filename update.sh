#!/bin/bash

USER_SCRIPT=https://gist.githubusercontent.com/mangar/728c09a28b3acf808644f14157b2b214/raw/a1109bd56e625ac6b7a7b5ea13ee6b9f2d3ca014/main.go
OUTPUT_SCRIPT=/app/user/bin/command.py

wget -q $USER_SCRIPT -O $OUTPUT_SCRIPT