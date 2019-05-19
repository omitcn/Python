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

class CounterList(list):
    def __init__(self,*args):
        super().__init__(*args)
        self.counter = 0
    def __getitem__(self,index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)
c = CounterList(range(10))
print(c)
c.reverse()
print(c)
del c[2:7]
print(c)
print(c.counter)
print(c[1] + c[2])
print(c.counter)

class CounterDict(dict):
    def __init__(self,*args):
        super().__init__(*args)
        self.counter = 0
    def __getitem__(self,key):
        self.counter += 1
        return super(CounterDict, self).__getitem__(key)
d = CounterDict({'name':'Bill'})
print(d['name'])
print(d.get('age'))    
d['age'] = 30
print(d['age'])
print(d.counter)


class MultiString(str):
    def __new__(cls, *args, sep = ' '):
        s = ''
        for arg in args:
            s += arg + sep
        index = -len(sep)
        if index == 0:
            index = len(s)
        return str.__new__(cls, s[:index])
    def __init__(self, *args, sep = ' '):
        pass
cs1 = MultiString('a', 'b', 'c')

cs2 = MultiString('a', 'b', 'c', sep=',')
cs3 = MultiString('a', 'b', 'c', sep='')
print('[' + cs1 + ']')
print('[' + cs2 + ']')
print('[' + cs3 + ']')

