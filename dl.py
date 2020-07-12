#!/usr/bin/env python3
import os
#from time import time
import time
from render import render

DOWNLOAD_WAIT = 60 * 2
RENDER_WAIT = DOWNLOAD_WAIT

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
# print("Current time:%s, dl_list time:%s, delta:%s" %(time.time(),f_st.st_mtime,time.time()-f_st.st_mtime))
if int(time.time() - f_st.st_mtime) < DOWNLOAD_WAIT : 
    with open(dl_list) as f:
        # os.system('cd video')
        for l in f:
            if l.strip() != '' and not l.startswith('#'):
                print('Downloading %s' % l, end='',flush=True)
                r = bash('youtube-dl %s' % l)
                if r.returncode == 0:
                    print('File downloaded.',flush=True)
        
    bash('mv *.mp4 video/')
    bash('mv *.webm video/')
    print('Download done!')

f_st = os.stat('video')
# print("Current time:%s, video time:%s, delta:%s" %(time.time(),f_st.st_mtime,time.time()-f_st.st_mtime))
# if download_list is modified recently, N minutes
if int(time.time() - f_st.st_mtime) < RENDER_WAIT : 
    render()
    print('All Done!')
    
