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
# 创建数据库
dbPath = 'bra.sqlite'
if os.path.exists(dbPath):
    os.remove(dbPath)
conn = sqlite3.connect(dbPath)
cursor = conn.cursor()
cursor.execute('''create table t_sales
            (id integer primary key autoincrement not null,
            color text not null,
            size text not null,
            source text not null,
            discuss mediumtext not null,
            time text not null);''')
conn.commit()

# Cookie劫持
http = PoolManager()
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
# GBK  GB2312  GBK  GB18030   utf-8 
#url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=547632594354&spuId=837695373&sellerId=3075989694&order=3&currentPage=1&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvV9vEvbQvjQCkvvvvvjiPPLqytjiWRFdv0jrCPmP9lj1Rn2dhgjtbPL5OljkjvpvhvvpvvvhCvvOvCvvvphmivpvUvvmvWvxBSF8EvpvVmvvC9cXHKphv8vvvvUrvpvvvvvv2UZCvHCQvvvZvphvZ99vvCpCvpCBEvvvHvhCvHhZEvpCWHh1Bvvai5fkXAfJ0v0KHAp0YWdEI27zOa4p7%2B3%2BdaNoxfBkK4Qtr6j7QIEt07reYiXhpV2lvIUcE5fu0EZSBsfvHDtyG28L%2BkweA%2BvGCvvpvvPMMRphvCvvvvvm5vpvhvvmv99%3D%3D&isg=AicnCqnpMRAuArW0dnbW1P8Ttl0xBOSG7c_a0PmUQ7bd6EeqAXyL3mXqft4N&needFold=0&_ksTS=1512991667023_1277&callback=jsonp1278'
#r = http.request('GET',url,headers = headers)
#print(r.data)
'''
c = r.data.decode('GB18030')

c = c.replace('jsonp1278(','')
c = c.replace(')','')
c = c.replace('false','"false"')
c = c.replace('true','"true"')
#print(c)
tmalljson = json.loads(c)
#print(type(tmalljson))
#print(tmalljson)
print(tmalljson['rateDetail']['paginator']['lastPage'])
print(tmalljson['rateDetail']['rateList'][1]['auctionSku'])
'''
def getRateDetail(itemId,currentPage):
    url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=' + str(itemId) + '&spuId=837695373&sellerId=3075989694&order=3&currentPage=' + str(currentPage) + '&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvV9vEvbQvjQCkvvvvvjiPPLqytjiWRFdv0jrCPmP9lj1Rn2dhgjtbPL5OljkjvpvhvvpvvvhCvvOvCvvvphmivpvUvvmvWvxBSF8EvpvVmvvC9cXHKphv8vvvvUrvpvvvvvv2UZCvHCQvvvZvphvZ99vvCpCvpCBEvvvHvhCvHhZEvpCWHh1Bvvai5fkXAfJ0v0KHAp0YWdEI27zOa4p7%2B3%2BdaNoxfBkK4Qtr6j7QIEt07reYiXhpV2lvIUcE5fu0EZSBsfvHDtyG28L%2BkweA%2BvGCvvpvvPMMRphvCvvvvvm5vpvhvvmv99%3D%3D&isg=AicnCqnpMRAuArW0dnbW1P8Ttl0xBOSG7c_a0PmUQ7bd6EeqAXyL3mXqft4N&needFold=0&_ksTS=1512991667023_1277&callback=jsonp1278'
    r = http.request('GET',url,headers = headers)
    c = r.data.decode('GB18030')
    c = c.replace('jsonp1278(','')
    c = c.replace(')','')
    c = c.replace('false','"false"')
    c = c.replace('true','"true"')
    tmalljson = json.loads(c)
    return tmalljson
tmalljson = getRateDetail('537808595989',10)
#print(getRateDetail('19628167605',1))

def getLastPage(itemId):
    tmalljson = getRateDetail(itemId,1)
    return tmalljson['rateDetail']['paginator']['lastPage']
def getProductIdList():
    url = 'https://list.tmall.com/search_product.htm?spm=a220m.1000858.1000724.4.38b7981eyLhA9O&cat=50025983&q=%D0%D8%D5%D6&sort=d&style=g&from=mallfp..pc_1_searchbutton&smAreaId=210100#J_Filter'
    r = http.request('GET', url,headers = headers)
    c = r.data.decode('GB18030')
    soup = BeautifulSoup(c,'lxml')
    linkList = []
    idList = []
    tags = soup.find_all(href=re.compile('detail.tmall.com/item.htm'))
    for tag in tags:
        linkList.append(tag['href'])
    linkList = list(set(linkList))
    for link in linkList:
        aList = link.split('&')
        # //detail.tmall.com/item.htm?id=562173686340
        idList.append(aList[0].replace('//detail.tmall.com/item.htm?id=',''))
    return idList

print(getLastPage('19628167605'))
initial = 0
productIdList = getProductIdList()
while initial < len(productIdList):
    try:
        itemId = productIdList[initial]
        print('----------',itemId,'------------')
        maxnum = getLastPage(itemId)
        num = 1
        while num <= maxnum:
            try:
                tmalljson = getRateDetail(itemId, num)
                rateList = tmalljson['rateDetail']['rateList']
                n = 0
                while n < len(rateList):
                    # 颜色分类:H007浅蓝色加粉色;尺码:32/70A
                    colorSize = rateList[n]['auctionSku']
                    m = re.split('[:;]',colorSize)
                    rateContent = rateList[n]['rateContent']
                    color = m[1]
                    size = m[3]
                    dtime = rateList[n]['rateDate']
                    cursor.execute('''insert into t_sales(color,size,source,discuss,time) 
                                    values('%s','%s','%s','%s','%s') ''' % (color,size,'天猫',rateContent,dtime))
                    conn.commit()
                    n += 1
                    print(color)
                print(num)
                num += 1
                #import time
                #time.sleep(3)
            except Exception as e:
                continue        
        initial += 1
    except Exception as e:
        print(e)
        
conn.close()
