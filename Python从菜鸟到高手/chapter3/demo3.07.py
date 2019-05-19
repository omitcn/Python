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
print(1,end=" ")
print(2,end=" ")
print(3,end=" ")
print(4,end=" ")
print(5,end=" ")
print(6,end=" ")
print(7,end=" ")
print(8,end=" ")
print(9,end=" ")
print(10)

# 用while循环输出1到10
print("用while循环输出1到10")
x = 1
while x <= 10:
    print(x,end=" ")
    x += 1

#  定义一个数组
numbers = [1,2,3,4,5,6,7,8,9,10]
print("\n用for循环输出数组中的值（1到10）")
for num in numbers:
    print(num, end= " ")
    
numbers = range(1,10000)
print("\n用for循环输出数组中的值（1到9999）")
for num in numbers:
    print(num, end= " ")
print("\n用for循环输出数组中的值的乘积（0到99）")
for num in range(100):
    print(num * num, end= " ")