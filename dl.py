#!/usr/bin/env python3
import os
from render import render

def bash(cmd):
    """ bash   
    """
    from subprocess import run, PIPE  # , Popen, CompletedProcess
    import sys

    if sys.version_info >= (3,7): 
        return run(cmd, shell=True, capture_output=True, text=True)
    else:
        raise Exception('Python 3.7+ required.')

with open('download_list.txt') as f:
    # os.system('cd video')
    for l in f:
        print('Downloading %s' % l)
        r = bash('youtube-dl %s' % l)
        if r.returncode == 0:
            print('File downloaded.')
        
bash('mv *.mp4 video/')
bash('mv *.webm video/')
print('Download done!')

render()
print('All Done!')
    
