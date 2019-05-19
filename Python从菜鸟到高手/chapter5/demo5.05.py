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
s1 = "Today is {}, the temperature is {} degrees."
print(s1.format("Saturday", 24))

s2 = "Today is {week}, the temperature is {degree} degrees."
print(s2.format(degree = 22, week ="Sunday"))

s3 = "Today is {week}, {}，the {} temperature is {degree} degrees."
print(s3.format("aaaaa", 12345, degree = 22, week ="Sunday"))

s4 = "Today is {week}, {1}，the {0} temperature is {degree} degrees."
print(s4.format("aaaaa", 12345, degree = 22, week ="Sunday"))

fullname = ["Bill", "Gates"]
print("Mr {name[1]}".format(name = fullname))

import math
s5 = "The {mod.__name__} module defines the value {mod.pi} for PI"
print(s5.format(mod = math))






