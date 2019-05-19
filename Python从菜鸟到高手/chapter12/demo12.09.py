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
from collections import deque

q = deque(range(10))
print(q)
q.append(100)
q.append(-100)
print(q)
q.appendleft(20)
print(q)
print(q.pop())
print(q)
print(q.popleft())
print(q)
q.rotate(-2)
print(q)
q.rotate(4)
print(q)
q1 = deque(['a','b'])
q.extend(q1)
print(q)
q.extendleft(q1)
print(q)
