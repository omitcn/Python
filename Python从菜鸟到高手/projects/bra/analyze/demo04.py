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
# 哪一种颜色的胸罩卖的最好
from pandas import *
from matplotlib.pyplot import *
import sqlite3
import sqlalchemy
engine = sqlalchemy.create_engine('sqlite:///bra.sqlite')
rcParams['font.sans-serif'] = ['SimHei']
options.display.float_format = '{:,.2f}%'.format
sales = read_sql('select source,color1 from t_sales',engine)
#print(sales)
color1Count = sales.groupby('color1')['color1'].count()

color1Total = color1Count.sum()
print(color1Total)
color1 = color1Count.to_frame(name='销量')
print(color1)

color1.insert(0,'比例', 100 * color1Count / color1Total)

color1.index.names=['颜色']
color1 = color1.sort_values(['销量'], ascending=[0])
print(color1)
n = 1200
others = DataFrame([color1[color1['销量'] <= n].sum()],index=MultiIndex(levels=[['其他']],labels=[[0]]))


color1 = color1[color1['销量']>n].append(others)
print(color1)


labels = color1.index.tolist()
pie(color1['销量'],labels=labels,autopct='%.2f%%')
legend()
axis('equal')
title('按胸罩颜色统计的比例')
show()
'''


# 数据可视化
# 一个DataFrame由一个或多个Series组成
print(size1['销量'])
labels = ['A罩杯','B罩杯','C罩杯','D罩杯']
size1['销量'].plot(kind='pie',labels = labels, autopct='%.2f%%')
axis('equal')
legend()
show()
'''