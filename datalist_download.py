# -*- coding: utf-8 -*-
'''
@Description: 
@Author: violeteve
@Date: 2020-02-24 19:51:25
@LastEditors: violeteve
@LastEditTime: 2020-02-24 20:58:19
@FilePath: \python-download-youtube\datalist_download.py
'''



import json
import youtube_dl

class GetItem(object):

    def download(self,youtube_url):
        # 定义某些下载参数
        ydl_opts = {
            # 格式化下载后的文件名
            'outtmpl': '%(extractor_key)s/%(title)s-%(id)s.%(ext)s',
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

        for i in range (0,2666):#5684
            file = "1.txt"
            with open(file) as fi:  # 打开
                line1 = fi.read()
            number = int(line1)  # 转成Int型
            print("number", number)
            fi.close()
            if i==number:
                print(i)
                if i==0:
                    re="https://www.youtube.com/watch?v="+"GoZ0YUcuFuA"
                    nu=97
                else:
                    t=s[i][1:]
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

path = r"data/train_list.json"
resolveJson(path)