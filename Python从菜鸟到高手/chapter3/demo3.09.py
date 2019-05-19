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
import random
'''
x = 0
break_flag = False
while x < 10:
    x += 1
    if x == random.randint(1,20):
        break_flag = True
        print(x)
        break;
if not break_flag:
    print("没有中断while循环")
'''

x = 0
while x < 10:
    x += 1
    if x == random.randint(1,20):
        print(x)
        break;    
else:
    print("没有中断while循环")
    
numbers = [1,2,3,4,5,6]
for number in numbers:
    if number == random.randint(1,12):
        print(number)
        break;
else:
    print("正常退出循环")
    
