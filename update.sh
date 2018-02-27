#!/bin/bash

USER_SCRIPT=https://gist.githubusercontent.com/mangar/42616e81e0914ccab6bb15acb7620612/raw/515afee46a6728a8eb9774d6d1e5f73813f211e8/command_dev.py
OUTPUT_SCRIPT=/home/pi/rpi_netmon-master/user/bin/command_dev.py

wget -q $USER_SCRIPT -O $OUTPUT_SCRIPT