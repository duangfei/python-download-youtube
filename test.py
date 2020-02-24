# -*- coding: utf-8 -*-
'''
@Description: 
@Author: violeteve
@Date: 2020-02-24 16:48:17
@LastEditors: violeteve
@LastEditTime: 2020-02-24 17:51:00
@FilePath: /python-download-youtube/test.py
'''

from os import rename
import time
import json
import youtube_dl

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

class GetItem(object):

    def rename_hook(self,d):
        # 重命名下载的视频名称的钩子
        if d['status'] == 'finished':
            file_name = 'Youtube/{}.mp4'.format(int(time.time()))
            rename(d['filename'], file_name)
            print('下载完成{}'.format(file_name))

    def download(self,youtube_url):
        # 定义某些下载参数
        ydl_opts = {
            # 我指定了要下载 “1” 这个格式，也可以填写 best/worst/worstaudio 等等
            # 'progress_hooks': [self.rename_hook],
            # 格式化下载后的文件名，避免默认文件名太长无法保存
            'outtmpl': '%(extractor_key)s/%(extractor)s-%(id)s-%(title)s.%(ext)s',
            # 打印日志
            'logger': MyLogger()
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            # 下载给定的URL列表
            ydl.download([youtube_url])

if __name__ == '__main__':
    getItem =  GetItem()
    getItem.download('https://www.youtube.com/watch?v=GoZ0YUcuFuA')
