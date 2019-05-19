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
from bs4 import BeautifulSoup
import re
disable_warnings()
http = PoolManager()
def str2Headers(file):
    headerDict = {}
    f = open(file,'r')
    
    headersText = f.read()

    headers = re.split('\n',headersText)
    n = 0
    for header in headers:
        result = header.split(':',maxsplit=1)
        headerDict[result[0]] = result[1] 
    f.close()
    return headerDict
headers = str2Headers('headers.txt')
#https://item.jd.com/12224904.html
r = http.request('GET','https://item.jd.com/12002469.html',headers = headers )
soup = BeautifulSoup(r.data,"lxml")

priceList = soup.find_all('ul',class_='p-parameter-list')
bookDetails1 = {}
for child in priceList[0].children:
    if child.name == 'li':  
        list = child.text.split('：')
        key = list[0].strip()
        value = list[1].strip()
        bookDetails1[key] = value

def filterFun(tag):
    if tag.name == 'li':
        if tag.parent.get('class') == ['p-parameter-list']:
            return True
    return False
bookDetails2 = {}
for tag in soup.find_all(filterFun):
    list = tag.text.split('：')
    key = list[0].strip()
    value = list[1].strip()
    bookDetails2[key] = value
print(bookDetails2)

