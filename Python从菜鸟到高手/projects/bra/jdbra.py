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
import sqlite3
import json
import re
import os
from bs4 import BeautifulSoup
disable_warnings()
http = PoolManager()
dbPath = 'bra.sqlite'
conn = sqlite3.connect(dbPath)
cursor = conn.cursor()
#print(jdDict)
#print(jdDict['maxPage'])
#print(jdDict['comments'][2]['content'].encode(encoding = 'ISO-8859-1').decode('GB18030'))
def getComments(productId,page):
    url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv14&productId=' + str(productId) + '&score=0&sortType=5&page=' + str(page) + '&pageSize=10&isShadowSku=0&fold=1'
    r = http.request('GET',url)
    c = r.data.decode('ISO-8859-1')
    c = c.replace('fetchJSON_comment98vv14(','')
    c = c.replace(')','')
    c = c.replace('false','"false"')
    c = c.replace('true','"true"')
    c = c.replace('null','"null"')
    c = c.replace(';','')
    jdDict = json.loads(c)
    return jdDict
def getMaxPage(productId):
    return getComments(productId,0)['maxPage']
def str2Headers(file):
    headerDict = {}
    f = open(file,'r')
    headersText = f.read()
    headers = re.split('\n',headersText)
    for header in headers:
        result = re.split(':',header,maxsplit = 1)
        headerDict[result[0]] = result[1]
    f.close()
    return headerDict
headers = str2Headers('headers.txt')
def getProductIdList():
    url = "https://search.jd.com/Search?keyword=%E8%83%B8%E7%BD%A9&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E8%83%B8%E7%BD%A9&psort=3&click=0"
    r = http.request('GET', url,headers = headers)
    r = r.data.decode('ISO-8859-1')

    soup = BeautifulSoup(r,'lxml')
    links = []
    idList = []
    tags = soup.find_all(href=re.compile('//item.jd.com/'))

    for tag in tags:
        links.append(tag['href'])
    linkList = list(set(links))
    for k in linkList:
        a = k.split('com/')
        
        idList.append(a[1].replace('.html','').replace('#comment',''))
    return idList
#print(getProductIdList())
productIdList = getProductIdList()
initial = 0
while initial < len(productIdList):
    try:
        productId = productIdList[initial]
        maxnum = getMaxPage(productId)
        num = 1
        while num <= maxnum:
            try:
                jdDict = getComments(productId, num)
                comments = jdDict['comments']
                n = 0
                while n < len(comments):
                    comment = comments[n]
                    content = comment['content'].encode(encoding='ISO-8859-1').decode('GB18030')
                    productColor = comment['productColor'].encode(encoding='ISO-8859-1').decode('GB18030')
                    creationTime = comment['creationTime'].encode(encoding='ISO-8859-1').decode('GB18030')
                    productSize = comment['productSize'].encode(encoding = 'ISO-8859-1').decode('GB18030')
                    cursor.execute('''insert into t_sales(color,size,source,discuss,time) 
                                    values('%s','%s','%s','%s','%s')''' 
                                    % (productColor,productSize,'京东','a',creationTime))
                    
                    conn.commit()
                    n += 1
                num += 1        
            except Exception as e:
                print(e)                
                continue
        initial += 1
    except Exception as e:
        print(e)
conn.close()



