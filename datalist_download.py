# -*- coding: utf-8 -*-
from os import rename
import time
import json
import youtube_dl


class GetItem(object):

    def rename_hook(self,d):
        # 重命名下载的视频名称的钩子
        if d['status'] == 'finished':
            file_name = 'Youtube/{}.mp4'.format(int(time.time()))
            rename(d['filename'], file_name)
            print('下载完成{}'.format(file_name))

    def download(self,youtube_url):
        # 定义某些下载参数
        format:"best"
        ydl_opts = {
            'progress_hooks': [self.rename_hook],
            # 格式化下载后的文件名，避免默认文件名太长无法保存
            'outtmpl': '%(extractor_key)s/%(extractor)s-%(id)s-%(title)s.%(ext)s',
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])


def resolveJson(path):
    with open(path, encoding='utf-8') as f:
        line = f.readline()
        d = json.dumps(line)#loads: 将 字符串 转换为 字典
        s=d.split(']')
        # n=0
        for i in range (0,2):#5684
            # n=n+1
            print(i)
            if i==0:
                re="https://www.youtube.com/watch?v="+"GoZ0YUcuFuA"
                nu=97
            else:
                t=s[i][1:]
                # print(t)
                k=t.split(',')
                re="https://www.youtube.com/watch?v="+k[0][4:15]
                nu = k[1]
                
            getItem =  GetItem()
            getItem.download(re)
            f.close()


# def output():
#     result = resolveJson(path)
#     print(result)
#     for x in result:
#         for y in x:
#             print(y)
path = r"data/test_list.json"
# output()
resolveJson(path)