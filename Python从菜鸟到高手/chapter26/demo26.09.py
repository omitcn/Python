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
from urllib import request  
import re  
from bs4 import BeautifulSoup  
from time import ctime,sleep
import os,sys,io
import threading
os.makedirs('urls', exist_ok = True)

insertUrl=["https://geekori.com"]

delUrl=[]

def getUrl():
    while(1):
        global insertUrl
        global delUrl  
        try:  
            if  len(insertUrl)>0 :  
                url = insertUrl[0]
                html = request.urlopen(url).read() 
                
                soup = BeautifulSoup(html,"lxml")
                
#                 write in file
                title=soup.find(name='title').get_text().replace('\n','')
                fp=open("./urls/"+str(title)+".html",'w',encoding='utf-8')
                fp.write(str(html.decode('utf-8')))
                fp.close()
                
                href_ = soup.find_all(name='a')
               
                for each in href_:
                    urlStr=each.get('href')  
                    if str(urlStr)[:4]=='http' and urlStr not in insertUrl:  
                       
                        insertUrl.append(urlStr)
                     
                        print(urlStr)                
                delUrl.append(insertUrl[0])
                del insertUrl[0]
        except:
            delUrl.append(insertUrl[0])
            del insertUrl[0]
            continue
        sleep(2)

threads = []
t1 = threading.Thread(target=getUrl)
threads.append(t1)
t2 = threading.Thread(target=getUrl)
threads.append(t2)
t3 = threading.Thread(target=getUrl)
threads.append(t3)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    for tt in threads:
        tt.join()