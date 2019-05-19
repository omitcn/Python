'''
--------《Python从菜鸟到高手》源代码------------

欧瑞科技版权所有
作者：李宁
如有任何技术问题，请加QQ技术讨论群：264268059    
或关注“极客起源”订阅号或“欧瑞科技”服务号或扫码关注订阅号和服务号，二维码在源代码根目录
如果QQ群已满，请访问https://geekori.com，在右侧查看最新的QQ群，同时可以扫码关注公众号

“欧瑞学院”是欧瑞科技旗下在线IT教育学院，包含大量IT前沿视频课程，
请访问http://geekori.com/edu或关注前面提到的订阅号和服务号，进入移动版的欧瑞学院

“极客题库”是欧瑞科技旗下在线题库，请扫描源代码根目录中的小程序码安装“极客题库”小程序

关于更多信息，请访问下面的页面
https://geekori.com/help/videocourse/readme.html



'''
from urllib3 import *
import re
import threading
disable_warnings()
http = PoolManager()

f = open('urls.txt','r')
urlList = []
while True:
    url = f.readline()
    if url == '':
        break;
    urlList.append(url.strip())
f.close()


class DownloadThread(threading.Thread):
    def __init__(self, func, args):
        super().__init__(target=func,args=args)

def download(filename,url):
    response = http.request('GET', url)
    f = open(filename,'wb')
    f.write(response.data)
    f.close()
    print('<',url,'>','下载完成')
for i in range(len(urlList)):
    thread = DownloadThread(download,(str(i) + '.jpg',urlList[i]))
    thread.start()