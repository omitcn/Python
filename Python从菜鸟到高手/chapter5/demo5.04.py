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
# 引用string模块中的Template类
from string import Template
template1 = Template("$s是我最喜欢的编程语言, $s非常容易学习，而且功能强大")
# 指定格式化参数s的值是Python
print(template1.substitute(s='Python'))
# 当格式化参数是一个字符串的一部分时，为了和字符串的其他部分区分开，
# 需要用一对大括号将格式化参数变量括起来
template2 = Template("${s}stitute")
print(template2.substitute(s='sub'))

template3 = Template("$dollar$$相当于多少$pounds")
# 替换两个格式化参数变量
print(template3.substitute(dollar=20,pounds='英磅'))

template4 = Template("$dollar$$相当于多少$pounds")
data = {}
data['dollar'] = 100
data['pounds'] = '英磅'
# 使用字典指定格式化参数值
print(template4.substitute(data))
