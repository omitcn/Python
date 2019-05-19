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
# 罩杯和上胸围分布【盒状图和直方图】
# 75B
from pandas import *
from matplotlib.pyplot import *
import sqlite3
import sqlalchemy
engine = sqlalchemy.create_engine('sqlite:///bra.sqlite')
rcParams['font.sans-serif'] = ['SimHei']
options.display.float_format = '{:,.2f}%'.format
sales = read_sql('select source,size1,size2,color1 from t_sales', engine)

sales.loc[sales['size1'] == 'A','size1'] = 1
sales.loc[sales['size1'] == 'B','size1'] = 2
sales.loc[sales['size1'] == 'C','size1'] = 3
sales.loc[sales['size1'] == 'D','size1'] = 4
sales = sales.dropna()
print(sales)
sales['size3'] = sales['size1'].astype('str') + '.' + sales['size2'].astype('str')
print(sales)
# 将size3转换为float类型的列
sales['size3'] = sales['size3'].astype('float')
box = {
    'facecolor':'0.75',
    'edgecolor':'b',
    'boxstyle':'round'
    }
fig,(ax1,ax2) = subplots(1,2,figsize=(12,6))
ax1.hist(x=sales.size3) 
ax2.boxplot(sales.size3)
ax1.text(3.5,8000,'1:A\n2:B\n3:C\n4:D\n小数部分：上胸围\n1.80 = A80\n2.75 = B75',bbox = box)
ax2.text(1.2,4,'1:A\n2:B\n3:C\n4:D\n小数部分：上胸围\n1.80 = A80\n2.75 = B75',bbox = box)

show()

# A、B、C、D  =  1、2、3、4
# B.75  2.75   3.80


