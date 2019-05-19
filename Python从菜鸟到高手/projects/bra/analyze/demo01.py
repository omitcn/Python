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
from pandas import *
from matplotlib.pyplot import *
import sqlite3
import sqlalchemy
engine = sqlalchemy.create_engine('sqlite:///bra.sqlite')
rcParams['font.sans-serif'] = ['SimHei']
sales = read_sql('select source,size1 from t_sales',engine)
size1Count = sales.groupby('size1')['size1'].count()
print(size1Count)
size1Total = size1Count.sum()
print(size1Total)
print(type(size1Count))
size1 = size1Count.to_frame(name='销量')
print(size1)
options.display.float_format = '{:,.2f}%'.format
size1.insert(0,'比例', 100 * size1Count / size1Total)
print(size1)
size1.index.names=['罩杯']
print(size1)

# 数据可视化
# 一个DataFrame由一个或多个Series组成
print(size1['销量'])
labels = ['A罩杯','B罩杯','C罩杯','D罩杯']
size1['销量'].plot(kind='pie',labels = labels, autopct='%.2f%%')
axis('equal')
legend()
show()