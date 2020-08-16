#!/usr/bin/env python3
import os
#from time import time
import time
from render import render

DOWNLOAD_WAIT = 60 * 1
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
                dl_cmd = '/usr/local/bin/youtube-dl -o "%%(title)s.%%(ext)s" %s' % l
                # print('dl_cmd:', dl_cmd)
                r = bash(dl_cmd)
                if r.returncode == 0:
                    print('File downloaded.',flush=True)
                else:
                    print('Download failed:\n',r.returncode,r.stdout,r.stderr,flush=True)
    
    r=bash('mv *.mp4 video/')
    # print('mv *.mp4 to video/\n:',r.stdout,r.stderr,flush=True)
    r=bash('mv *.webm video/')
    print('Download done!')

f_st = os.stat('video')
# print("Current time:%s, video time:%s, delta:%s" %(time.time(),f_st.st_mtime,time.time()-f_st.st_mtime))
# if download_list is modified recently, N minutes
if int(time.time() - f_st.st_mtime) < RENDER_WAIT : 
    render()
    print('All Done!')
    
