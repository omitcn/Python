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
# Series中的方法
import pandas as pd
import matplotlib.pyplot as plt
scientists = pd.DataFrame({
    'Name':['Rosaline Franklin', 'William Gosset'],
    'Occupation':['Chemist', 'Statistician'],
    'Born':['1920-07-25', '1876-06-13'],
    'Died':['1958-04-16','1937-10-16'],
    'Age':[37,61]},columns=['Occupation','Born','Died','Age'],
            index=['Rosaline Franklin', 'William Gosset'])
print(scientists)

ages = scientists['Age']
print(type(ages))
print(ages)
print('mean',':',ages.mean())  # 取平均数
print('min',':',ages.min())
print('max',':',ages.max())
print('std',':',ages.std())
print('-------------')
print(ages.sort_values(ascending=False))
print('-------------')
print(ages.append(ages))
