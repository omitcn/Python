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
# 罩杯和上胸围综合统计与数据可视化
# B  75   75B  80A
from pandas import *
from matplotlib.pyplot import *
import sqlite3
import sqlalchemy
engine = sqlalchemy.create_engine('sqlite:///bra.sqlite')
rcParams['font.sans-serif'] = ['SimHei']
options.display.float_format = '{:,.2f}%'.format

sales = read_sql('select source,size1,size2 from t_sales',engine)
size1size2Count = sales.groupby(['size1','size2'])['size1'].count()

size1size2Total = size1size2Count.sum()

size1size2 = size1size2Count.to_frame(name='销量')

n = 500
others = DataFrame([size1size2[size1size2['销量'] <= n].sum()],index=MultiIndex(levels=[[''],['其他']],labels=[[0],[0]]))


size1size2 = size1size2[size1size2['销量']>n].append(others)
print(size1size2)

size1size2 = size1size2.sort_values(['销量'],ascending=[0])
size1size2.insert(0,'比例',100 * size1size2Count / size1size2Total)
print(size1size2)
labels = size1size2.index.tolist()
newLabels = []
for label in labels:
    newLabels.append(label[1] + label[0])
pie(size1size2['销量'],labels=newLabels,autopct='%.2f%%')
legend()
axis('equal')
title('罩杯+上胸围销售比例')
show()




