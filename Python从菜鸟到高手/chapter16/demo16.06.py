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
disable_warnings()
http = PoolManager(timeout=Timeout(connect=2,read=2))
url1 = 'https://www.baidu1122.com'
url2 = 'http://httpbin.org/delay/3'
try:
    http.request('GET', url1,timeout=Timeout(connect=2.0,read=4))
except Exception as e:
    print(e)
print('------------')
response = http.request('GET', url2,timeout=Timeout(connect=2,read=4))
print(response.info())
print('------------')
print(response.info()['Content-Length'])
http.request('GET', url2,timeout=Timeout(connect=2,read=2))