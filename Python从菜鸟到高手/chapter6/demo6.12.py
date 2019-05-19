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
dict1 = {
    'title':'欧瑞学院',
    'website':'https://geekori.com',
    'description':'从事在线IT课程研发和销售'    
    }
dict2 = {
    'title':'欧瑞科技',
    'products':['欧瑞学院','博客','读书频道','极客题库','OriUnity'],
    'description':'从事在线IT课程研发和销售，工具软件研发'
    }
dict1.update(dict2)
for item in dict1.items():
    print("key = {key}  value = {value}".format(key = item[0],value = item[1]))
