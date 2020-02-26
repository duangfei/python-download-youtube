# -*- coding: utf-8 -*-
'''
@Description: 
@Author: violeteve
@Date: 2020-02-24 19:51:25
@LastEditors: violeteve
@LastEditTime: 2020-02-25 15:05:55
@FilePath: /python-download-youtube/datalist_download.py
'''

import json
import youtube_dl

class GetItem(object):

    def download(self,youtube_url):
        # 定义某些下载参数
        ydl_opts = {
            # 格式化下载后的文件名
            # 'outtmpl': '%(extractor_key)s/%(title)s-%(id)s.%(ext)s',
            'outtmpl': '/Users/duanfei/OneDrive/YouTube/test_list/%(title)s-%(id)s.%(ext)s',
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

        for i in range (0,1684):#5684
            file = "1.txt"
            with open(file) as fi:  # 打开
                line1 = fi.read()
            number = int(line1)  # 转成Int型
            fi.close()
            if i == number:
                print("开始下载！！ 编号：",i)
                # print(i)
                if i==0:
                    re="https://www.youtube.com/watch?v="+"GoZ0YUcuFuA"
                    nu=97
                else:
                    t=s[i][1:]
                    k=t.split(',')
                    re="https://www.youtube.com/watch?v="+k[0][4:15]
                    nu = k[1]
                try:
                    getItem =  GetItem()
                    getItem.download(re)
                # except youtube_dl.utils.DownloadError as err:
                #     print('下载异常，尝试重新下载！')
                #     getItem =  GetItem()
                #     getItem.download(re)
                #     with open('1.txt', 'w') as file:  # .txt可以不自己新建,代码会自动新建
                #         file.write (str(i+1))  # 写入
                #         file.close()
                #         print("下载成功！")
                except youtube_dl.utils.DownloadError as err:
                    print('下载异常，跳过该视频！')
                    with open('1.txt', 'w') as file:  # .txt可以不自己新建,代码会自动新建
                        file.write (str(i+1))  # 写入
                        file.close()
                else:
                    with open('1.txt', 'w') as file:  # .txt可以不自己新建,代码会自动新建
                        file.write (str(i+1))  # 写入
                        file.close()
                        print("下载成功！")

            elif i<=number:
                i=number+1
            else:
                break
            f.close()

path = r"data/test_list.json"
resolveJson(path)