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
def addNumbers(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result
print(addNumbers(1,2,3,4,5))
print("--------------")
def calculator(type, *numbers):
    result = 0
    if type == "add":
        for number in numbers:
            result += number
    elif type == "sub":
        result = numbers[0]
        for i in range(1, len(numbers)):
            result -= numbers[i]
    elif type == "mul":
        result = 1
        for number in numbers:
            result *= number
    else:
        result = numbers[0]
        for i in range(1, len(numbers)):
            result /= numbers[i]
    return result

print(calculator("add",1,2,3,4,5,6))
print(calculator("sub",1234,44,54,12,57))
print(calculator("mul",1,2,3,4,5,6,7))
print(calculator("div",100,2,5))
print("--------------")
def calculator1(type, *numbers, ratio):
    return calculator(type, *numbers) * ratio
    
print(calculator1("add",1,2,3,4,5,6,ratio = 3))
print(calculator1("sub",1234,44,54,12,57,ratio = 2))
print(calculator1("mul",1,2,3,4,5,6,7,ratio = 4))
print(calculator1("div",100,2,5,ratio = 4))
print("--------------")
def calculator2(type, *numbers, ratio = 4):
    return calculator(type, *numbers) * ratio
print(calculator2("add",1,2,3,4,5,6))