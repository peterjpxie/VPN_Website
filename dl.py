#!/usr/bin/env python3
import os
#from time import time
import time
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

dl_list = 'download_list.txt'
f_st = os.stat(dl_list)

# if download_list is modified recently, N minutes
if int(time.time() - f_st.st_mtime) < 60 * 10: 
    with open(dl_list) as f:
        # os.system('cd video')
        for l in f:
            if l.strip() != '':
                print('Downloading %s' % l, end='')
                r = bash('youtube-dl %s' % l)
                if r.returncode == 0:
                    print('File downloaded.')
        
    bash('mv *.mp4 video/')
    bash('mv *.webm video/')
    print('Download done!')

render()
print('All Done!')
    
