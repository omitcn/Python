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
# 从百度抓取比基尼美女
from urllib3 import *
import os
import re
import json
http = PoolManager()
disable_warnings()

os.makedirs('download/images', exist_ok = True)
def str2Headers(file):
    headerDict = {}
    f = open(file,'r')
    
    headersText = f.read()

    # Linux、Unix、Mac OS X：\n
    # Windows：\r\n
    headers = re.split('\n',headersText)
    for header in headers:
        result = re.split(':',header, maxsplit=1)
        headerDict[result[0]] = result[1]        
    f.close()
    return headerDict

headers = str2Headers('image_headers.txt')
def processResponse(response):
    global count
    if count > 100:
        return
    s = response.data.decode('utf-8')
    d = json.loads(s)
    n = len(d['data'])
    for i in range(n - 1):
        if count > 100:
            return
        imageUrl = d['data'][i]['hoverURL'].strip()
        if imageUrl != '':
            print(imageUrl)
            r = http.request('GET', imageUrl,headers = headers)
            count += 1
            imageFile = open('download/images/%0.5d.jpg' % count,'wb')
            imageFile.write(r.data)
            imageFile.close()
count = 0
pn = 30
rn = 30
url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E6%AF%94%E5%9F%BA%E5%B0%BC%E7%BE%8E%E5%A5%B3&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%E6%AF%94%E5%9F%BA%E5%B0%BC%E7%BE%8E%E5%A5%B3&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn={pn}&rn={rn}&gsm=1e&1512281761218='.format(pn=pn,rn=rn) 

while count <= 100:
    r = http.request('GET',url)
    processResponse(r)
    pn += 30

