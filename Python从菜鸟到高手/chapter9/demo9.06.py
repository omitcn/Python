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
class NegativeException(Exception):
    pass
class ZeroException(Exception):
    pass

class SpecialCalc:
    def add(self,x,y):
        if x < 0 or y < 0:
            raise NegativeException("x和y都不能小于0")
        return x + y
    def sub(self,x,y):
        if x - y < 0:
            raise NegativeException("x与y的差值不能小于0")
        return x - y
    def mul(self,x,y):
        if x == 0 or y == 0:
            raise ZeroException("x和y都不能等于0")
        return x * y
    def div(self,x,y):
        return x / y

while True:
    try:
        calc = SpecialCalc()
        expr = input("请输入要计算的表达式，例如，add(1,2)：")
        if expr == ":exit":
            break;
        result = eval('calc.' + expr)
        print("计算结果：{:.2f}".format(result))
    except (NegativeException,ZeroException) as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)    
    except:
        print("******其他异常******")
        