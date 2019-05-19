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
# 保存爬取的数据

from urllib3 import *
from re import *
import os
import hashlib
http = PoolManager()
disable_warnings()
os.makedirs('download', exist_ok = True)
def computeMD5hash(myString):
    m = hashlib.md5()
    m.update(myString.encode('utf-8'))
    return m.hexdigest()

f = open('download/urls.txt','w')
def download(url):
    result = http.request('GET', url)
    md5 = computeMD5hash(url)
    f.write(url + '\n')
    htmlStr = result.data.decode('utf-8')
    htmlFile =open('download/' + md5,'w')
    htmlFile.write(htmlStr)
    htmlFile.close()
    return htmlStr
#print(download('http://www.weather.com.cn/'))
def analyse(htmlStr):
    # <a href='a.html'>a</a>
    aList = findall('<a[^>]*>',htmlStr)
    result = []
    for a in aList:
        # <a href='a.html'>
        g = search('href[\s]*=[\s]*[\'"]([^>\'""]*)[\'"]',a)
        if g != None:
            url = g.group(1)
            url = 'http://localhost:8888/files/' + url
            result.append(url)
    return result

def crawler(url):
    print(url)
    html = download(url)
    urls = analyse(html)
    for url in urls:
        crawler(url)
crawler('http://localhost:8888/files')
f.close()

