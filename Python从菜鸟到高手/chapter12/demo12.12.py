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
import time

time1 = time.time()
time2 = time1 + 60             # 1分钟
time3 = time1 + 60 * 60         # 1小时
time4 = time1 - 60 * 60 * 24    # 1天
time1 = time.localtime(time1)
time2 = time.localtime(time2)
time3 = time.localtime(time3)
time4 = time.localtime(time4)
print (time.strftime("%Y-%m-%d %H:%M:%S", time1))
print (time.strftime("%Y-%m-%d %H:%M:%S", time2))
print (time.strftime("%Y-%m-%d %H:%M:%S", time3))
print (time.strftime("%Y-%m-%d %H:%M:%S", time4))

