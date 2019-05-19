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
print("{0:=^10.2f}".format(-4.56))

from math import pi
print("{pi:012.3f}".format(pi = pi))
numStr = input("请输入章节序号的位数：")
num = int(numStr)
print("第{:0{num}.0f}章，第{:03.0f}节".format(1,2,num = num))
print('{0:<10.2f}\n{0:^10.2f}\n{0:>10.2f}'.format(pi))
print("{:$^20}".format(" 美元 "))
print("{:￥<20}".format(" 人民币 "))
print("{0:=10.2f}".format(-pi))
sign = input("请输入在数值前面输出的符号：")
print("{0:{sign}=10.2f}".format(-pi,sign = sign))
numStr = input("请输入要转换为二进制和十六进制的数：")
num = int(numStr)
print("{:b}".format(num))
print("{:#b}".format(num))
print("{:x}".format(num))
print("{:#x}".format(num))




