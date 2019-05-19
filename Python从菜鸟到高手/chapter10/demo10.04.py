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
class FactorialDict:
    def __init__(self):
        self.numDict = {}
    def factorial(self,n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n -1)
    def __getitem__(self,key):
        print('__getitem__方法被调用,key={}'.format(key))
        if key in self.numDict:
            return self.factorial(self.numDict[key])
        else:
            return 0
    def __setitem__(self,key, value):
        print('__setitem__方法被调用,key={}'.format(key))
        self.numDict[key] = int(value)
    def __delitem__(self,key):
        print('__delitem__方法被调用,key={}'.format(key))
        del self.numDict[key]
    def __len__(self):
        print('__len__方法被调用')
        return len(self.numDict)

d = FactorialDict()
d['4!'] = 4
d['7!'] = 7
d['12!'] = '12'



print('4!', '=', d['4!'])
print('7!', '=',d['7!'])
print('12!', '=',d['12!'])
print('len','=',len(d))
del d['7!']
print('7!', '=',d['7!'])
print('len','=',len(d))
