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
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.left = 0
        self.top = 0
    def __setattr__(self,name,value):        
        print("{}被设置，新值为{}".format(name,value))
        if name == 'size':
            self.width, self.height = value
        elif name == 'position':
            self.left, self.top = value
        else:
            self.__dict__[name] = value  # 必须加上

    def __getattr__(self,name):
        print("{}被获取".format(name))
        if name == 'size':
            return self.width,self.height
        elif name == 'position':
            return self.left, self.top 

    def __delattr__(self,name):
        if name == 'size':
            self.width,self.height = 0, 0
        elif name == 'position':
            self.left, self.top = 0,0
r = Rectangle()
r.size = 300,500
r.position = 100,400
print('size', '=', r.size)
print('position', '=', r.position)
del r.size, r.position
print(r.size)
print(r.position)


class MyClass:
     def __setattr__(self,name,value):        
        if name == 'value':
            if value > 0:
                self.__dict__[name] = value
            else:
                print('{}属性的值必须大于0'.format(name))
        else:
           self.__dict__[name] = value
c = MyClass()
c.value = 20
print('c.value','=',c.value)
c.value = -43
print('c.value','=',c.value)
