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
class MyClass:
    name = "Bill"
    def __init__(self):
        print("MyClass的构造方法被调用")
        self.value = 20
    @staticmethod
    def run():
        print('*', MyClass.name, '*')
        print("MyClass的静态方法run被调用")
    @classmethod
    # 这里self是元数据
    def do(self):
        print(self)
        print('[', self.name, ']')
        print('调用静态方法run')
        self.run()
        # 如果是类方法，就无法访问self中的成员变量了
        #print(self.value)
        print("成员方法do被调用")
    def do1(self):
        print(self.value)
        print('<',self.name, '>')
        print(self)
        
MyClass.run()
c = MyClass()
c.do()
print('MyClass2.name','=',MyClass.name)
MyClass.do()
c.do1()



