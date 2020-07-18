#!/bin/sh
if ! ps -ef|grep -v grep | grep dl.py; then
# echo "starting dl.py"
python /root/Website/dl.py  >> /root/Website/dl.log  
fi
# echo "dl.sh done" 
