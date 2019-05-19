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
def sub1(m, n):
    return m - n

print(sub1(20,4))
print(sub1(4,20))

print(sub1(m = 20, n = 4))
print(sub1(n = 4, m = 20))

def sub2(m = 100, n = 50):
    return m - n

    
print(sub2())
print(sub2(45,21))
print(sub2(53, n = 12))
print(sub2(n = 123))
print(sub2(m = 542,n = 143))
print(sub2(53, m = 12))  