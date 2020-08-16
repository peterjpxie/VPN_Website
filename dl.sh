#!/bin/sh
if ! ps -ef|grep -v grep | grep dl.py; then
# echo "starting dl.py"
python /root/website/dl.py  >> /root/website/dl.log 2>&1
fi
# echo "dl.sh done" 
