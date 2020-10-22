#!/usr/bin/env python3
import os
# import fileinput

def render():
    html_file = 'video.html'
    html_template = 'video.template.html'

    video_list = []
    for f in os.listdir('video'):  # list current folder
        if f.endswith('.mp4') or f.endswith('.webm'):
            video_list.append(f)
            # print(f)

    video_list.sort()
    # print(video_list)
    video_div = '<br>'
    id = 0
    for f in video_list:
        id += 1
        f_no_ext = f.replace('.mp4','').replace('.webm','')    
        one_video = """ 
        <video class="video_responsive" id="%s" controls>
          <source src="video/%s" type="video/mp4">
          Your browser does not support the video tag.
        </video><br>
        <p class="video_responsive">%s</p><br>
        """ % (id,f,f_no_ext)
        video_div += one_video
    # print(video_div) 
                    
    with open(html_template, 'r')as template:
        with open(html_file,'w+') as f:    
            content = template.read()
            content = content.replace(r'{#replace#}',video_div)
            f.write(content)

if __name__ == '__main__':
    render()