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
# 初始化函数
def init(data):
    data["d"] = {}
    data["names"] = []
    data["products"] = []
# 从控制台采集数据，并转化为列表或字典的函数，flag为True采集列表，为False，采集Dict
# msg表示提示文本，为了方便，这里假设输入的数据以逗号分隔，也可以将分隔符通过函数参数传入
def inputListOrDict(flag,msg):
    print(msg)
    inputStr = input(":")
    list = inputStr.split(",")
    # 返回列表
    if flag:
        return list
    
    keys = []
    values = []
    result = {}
    for i in range(len(list)):
        # key
        if i % 2 == 0:
            keys.append(list[i])
        else:
            values.append(list[i])
    # 返回字典
    return dict(zip(keys,values))
# 输出字典中的数据
def outDict(data):
    for key in data.keys():
        print(key,":",data[key])
