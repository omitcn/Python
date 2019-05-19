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
# 可视化统计数据（依赖Matplotlib）
import pandas
import matplotlib.pyplot as plt
df = pandas.read_csv('gapminder.tsv',sep='\t')

global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()
print(global_yearly_life_expectancy)
multi_group_var = df.groupby('year')['gdpPercap'].mean()
print(multi_group_var)

fig,(ax1, ax2) = plt.subplots(1,2,figsize=(8,4))
ax1.plot(global_yearly_life_expectancy)
ax2.plot(multi_group_var)
plt.show()
