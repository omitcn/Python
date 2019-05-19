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
class CustomException1(Exception):
    pass
class CustomException2(Exception):
    pass
class CustomException3(Exception):
    pass
import random


def raiseException():
    n = random.randint(1,3)
    print("抛出CustomException{}异常".format(n))
    if n == 1:
        raise CustomException1
    elif n == 2:
        raise CustomException2
    else:
        raise CustomException3
try:
    raiseException()
except (CustomException1,CustomException2,CustomException3):
    print("******执行异常处理程序******") 