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
# 输出带“\n"的字符串，运行结果：<hello
 #                            world>
print("<hello\nworld>")
# 用str函数将1234转换为数字，运行结果：1234
print(str(1234))
#  抛出异常，len函数不能直接获取数字的长度
#print(len(1234))   
#  将1234转换为字符串后，获取字符串长度，运行结果：4
print(len(str(1234)))
#  运行结果：<hello
 #            world>
print(str("<hello\nworld>"))
#  运行结果：13
print(len(str("<hello\nworld>")))
#  运行结果：'<hello\nworld>'
print(repr("<hello\nworld>"))
#  运行结果：16
print(len(repr("<hello\nworld>")))
print("<hello\\nworld>")
print(len("<hello\\nworld>"))
print(r"<hello\nworld>")
print(len(r"<hello\nworld>"))

