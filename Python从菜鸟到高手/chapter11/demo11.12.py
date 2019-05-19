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
# 常用的正则表达式

import re
# Email
email = '[0-9a-zA-Z]+@[0-9a-zA-Z]+\.[a-zA-Z]{2,3}'
result = re.findall(email, 'lining@geekori.com')
print(result)
result = re.findall(email, 'abcdefg@aa')
print(result)
result = re.findall(email, '我的email是lining@geekori.com，不是bill@geekori.cn，请确认输入的Email是否正确')
print(result)



ipv4 = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
result = re.findall(ipv4, '这是我的IP地址：33.12.54.34，你的IP地址是100.32.53.13吗')
print(result)

url = 'https?:/{2}\w.+'
url1 = 'https://geekori.com'
url2 = 'ftp://geekori.com'
print(re.match(url,url1))
print(re.match(url,url2))
