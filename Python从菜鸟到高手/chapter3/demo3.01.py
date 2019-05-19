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
#  输出用空格分隔的多参数值
print("name =", "Bill")
#  输出用空格分隔的多参数值
print("age =", 30)
#  输出用空格分隔的多参数值
print("Apple" + "," + "Orange" + "," + "Banana")
#  修改多参数值分隔符为逗号（,），然后输出多参数值
print("Apple", "Orange","Banana", sep=",")
#  修改多参数值分隔符为逗号（,），然后输出多参数值
print("Can","you","tell","me", "how", "to", "get", "to","the","nearest", "tube", "station", sep="&")
#  修改输出字符串结尾符为空格，这样下一次调用print函数，就会中同一行输出内容了
#  运行结果：Hello world
print("Hello", end=" ")
print("world")
# 修改输出字符串结尾符为长度为0的字符串，这样下一次调用print函数，输出的内容不仅会在同一行，
# 而且会收尾相接，运行结果：abc
print("a",end="");
print("b",end="");
print("c");
