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
s1 = "hello world"
#  在字符串中使用索引
print(s1[0])                # 获取s1的第1个字符，运行结果：h
print(s1[2])                # 获取s1的第3个字符，运行结果：l
#  在字符串中使用分片
print(s1[6:9])                    # 获取s1从第7个字符往后的3个字符，运行结果：wor
print(s1[6:])                # 获取s1从第7个字符后的所有字符，运行结果：world
print(s1[::2])                # 在s1中每隔一个取一个字符，运行结果：hlowrd

s2  = "abc"
#  在字符串中使用乘法
print(10 * s2)                #  运行结果：abcabcabcabcabcabcabcabcabcabc
print(s2 * 5)                #  运行结果：abcabcabcabcabc
#  在字符串中使用in运算符
print('b' in s2)            #  运行结果：True
print('x' not in s2)        #  运行结果：True

print(len(s1))                #  获取s1的长度，运行结果：11
print(min(s2))                #  获取s2中按ASCII计算最小的字符，运行结果：a
print(max(s2))                #  获取s2中按ASCII计算最大的字符，运行结果：c
