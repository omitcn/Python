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
url = input("请输入一个Https网址：")
scheme = url[0:5]                    #  分片获取Url中的Scheme
host = url[8:]                        #  分片获取Url中的Host

print("scheme:", scheme)
print("host:",host) 

str = input("请输入一个整数:")
n = int(str);

numbers = range(1,n)                # 产生包含1到n的数值类型的序列
numbers1 = numbers[0::2]            # 分片获取序列中的奇数
numbers2 = numbers[1::2]            # 分片获取序列中的偶数
for number in numbers1:                # 在第1行输出所有的奇数
    print(number, end= " ")
print("")
print(" ",end="")
for number in numbers2:                # 在第2行错位输出所有的偶数
    print(number, end= " ")
