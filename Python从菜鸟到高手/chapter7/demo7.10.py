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
x = 1                # 全局变量
def fun1():
    x = 30            # 局部变量
fun1()
# 运行结果：1
print(x)

x = 123                # 全局变量
def fun2():
    print(x)            # 运行结果：123
fun2()

x = 123
def fun3():
    x = 30
    print(x)            # 运行结果：30
fun3()

x = 123
def fun4():    
    print(x)            # 执行这行代码会抛出异常
    x = 30            
fun4()

x = 30
def fun5():
    x = 40
    # 嵌套函数
    def fun6():
        # 这里的变量x是在函数fun5中定义的局部变量
        print(x)
        print("fun6")
    # 返回fun6函数本身
    return fun6
fun5()()        # 调用了fun5函数的嵌套函数fun6
