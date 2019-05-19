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
# 未使用函数抽象的代码
data = {}
data["d"] = {}
data["names"] = []
data["products"] = []
print("请输入字典数据，key和value之间用逗号分隔")
dictStr = input(":")
# 将d拆分成key和value的两个集合
list = dictStr.split(",")
keys = []
values = []
for i in range(len(list)):
    # key
    if i % 2 == 0:
        keys.append(list[i])
    else:
        values.append(list[i])
data["d"].update(dict(zip(keys,values)))

print("请输入姓名，多个姓名之间用逗号分隔")
nameStr = input(":")
names = nameStr.split(",")
data["names"].extend(names)


print("请输入产品，多个产品之间用逗号分隔")
productStr = input(":")
products = productStr.split(",")
data["products"].extend(products)


for key in data.keys():
    print(key,":",data[key])


