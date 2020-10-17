#!/usr/bin/env python3
import os
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

# if download_list.txt is modified recently
# print("Current time:%s, dl_list time:%s, delta:%s" %(time.time(),f_st.st_mtime,time.time()-f_st.st_mtime))
if int(time.time() - f_st.st_mtime) < DOWNLOAD_WAIT : 
    print('Start download at %s' % time.asctime())
    with open(dl_list) as f:
        # os.system('cd video')
        for l in f:
            if l.strip() != '' and not l.startswith('#'):
                print('Downloading %s' % l, flush=True)
                dl_cmd = '/usr/local/bin/youtube-dl -o "%%(title)s.%%(ext)s" %s' % l
                # print('dl_cmd:', dl_cmd)
                r = bash(dl_cmd)
                # Note: youtube-dl returncode is always 0 even fails with errors, so check stderr instead of returncode.
                if r.stderr == '':
                    print('File downloaded.',flush=True)
                elif 'File name too long' in r.stderr: 
                    # shorten filename and retry
                    print('File name too long, shorten and retrying...',flush=True)
                    t = bash('/usr/local/bin/youtube-dl --get-filename %s' % l)
                    if t.stderr == '':                       
                        filename = t.stdout
                        suffix = filename.split('.')[-1].strip() # strip the space
                        filename = filename[:50] + '.' + suffix
                        # print('Shortened filename: %s.' % filename,flush=True)
                        dl_cmd = '/usr/local/bin/youtube-dl -o "%s" %s' % (filename,l)
                        # print(dl_cmd)
                        r = bash(dl_cmd) 
                
                if r.stderr != '':
                    print('Download failed:\n',r.returncode,r.stdout,r.stderr,flush=True)
    
    for i in os.listdir():
        if '.' in i and i.split('.')[-1] in ('mp4', 'webm'):
            # remove '#' which will cause web link issue
            new_filename = i.replace('#','')
            os.rename(i,new_filename)
            time.sleep(0.01) # delay for file rename takes effect
            print('moving %s.' %  new_filename)
            mv_cmd = 'mv "%s" video/' % new_filename
            # print(mv_cmd)
            r=bash(mv_cmd)
            if r.returncode !=0:
                print(r.stdout,r.stderr)

    print('Download done!')

f_st = os.stat('video')
# print("Current time:%s, video time:%s, delta:%s" %(time.time(),f_st.st_mtime,time.time()-f_st.st_mtime))
# if video folder is modified recently
if int(time.time() - f_st.st_mtime) < RENDER_WAIT : 
    render()
    print('All Done!')
    
