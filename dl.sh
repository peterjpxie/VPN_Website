#!/bin/sh
if ! ps -ef|grep -v grep | grep dl.py; then
python /root/Website/dl.py  | tee /root/Website/dl.log  
fi 
