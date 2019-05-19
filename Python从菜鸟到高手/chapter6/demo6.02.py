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
# 字典中的键可以是任意不可变的类型
dict = {}
dict[20] = "Bill"   
dict["Mike"] = {'age':30,'salary':3000}
dict[(12, "Mike", True)] = "hello"
print(dict)

#list = []
#list[30] = "hello"   # 抛出异常

#  演示key in dict操作

IDEs = {
    'eclipse':
        {
        'languages':['Java', 'Python', 'JavaScript','PHP'],
        'organization':'Eclipse基金会'
        },
    'visualstudio':
        {
        'languages':['C#','C++', 'VB.NET'],
        'organization':'微软'
        },
    'webstorm':
        {
        'languages':['JavaScript'],
        'organization':'JetBrains'
        }
    
    }

labels = {
    'languages':'支持的编程语言',
    'organization':'所属机构'
    }
IDE = input('请输入IDE的名字：')
findIDE = IDE.replace(" ", "").lower()
choice = input('要查询IDE支持的编程语言(lang)还是所属组织机构(org)？')
if choice == "lang": key = 'languages'
if choice == "org": key = 'organization'

if findIDE in IDEs:
    print("{}{}是{}.".format(IDE, labels[key], IDEs[findIDE][key]))

