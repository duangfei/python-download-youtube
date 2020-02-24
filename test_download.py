# -*- coding: utf-8 -*-
'''
@Description: 
@Author: violeteve
@Date: 2020-02-24 19:51:25
@LastEditors: violeteve
@LastEditTime: 2020-02-24 20:25:30
@FilePath: \python-download-youtube\test_download.py
'''

from os import rename
import time
import json
import youtube_dl

class GetItem(object):

    def rename_hook(self,d):
        # 重命名下载的视频名称的钩子
        if d['status'] == 'finished':
            file_name = 'Youtube/{}''.mp4'.format(int(time.time()))
            rename(d['filename'], file_name)
            print('下载完成{}'.format(file_name))

    def download(self,youtube_url):
        # 定义某些下载参数
        ydl_opts = {
            # 'progress_hooks': [self.rename_hook],
            # 格式化下载后的文件名，避免默认文件名太长无法保存
            'outtmpl': '%(extractor_key)s/%(title)s.%(ext)s',
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])


def resolveJson(path):
    sum=0
    with open(path, encoding='utf-8') as f:
        line = f.readline()
        d = json.dumps(line)#loads: 将 字符串 转换为 字典
        s=d.split(']')
        # n=0

        for i in range (0,10):#5684
            file = "1.txt"
            with open(file) as fi:  # 打开
                line1 = fi.read()
            number = int(line1)  # 转成Int型
            print("number", number)
            fi.close()
            if i==number:
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
                with open('1.txt', 'w') as file:  # .txt可以不自己新建,代码会自动新建
                    file.write (str(i+1))  # 写入
                    file.close()
            elif i<=number:
                i=number+1
            else:
                break
            f.close()


path = r"data/test_list.json"
resolveJson(path)