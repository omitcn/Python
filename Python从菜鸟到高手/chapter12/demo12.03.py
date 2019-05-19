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
import os
if not os.path.exists('newdir1'):
    os.mkdir('newdir1')
if not os.path.exists('newdir2'):
    os.mkdir('newdir2',0o377) # 无法读 用管理员权限可以读

#os.mkdir('a/b/c/d') error
os.makedirs('x/y/z',0o733,True)  # 目录，无法读  sudo
# 以数字mode的mode创建一个名为path的文件夹.默认的 mode 是 0777 (八进制)。

try:
    os.rmdir('newdir1') # 删除path指定的空目录，如果目录非空，则抛出一个OSError异常
except OSError as e:
    print(e)
os.removedirs('x/y/z')
#os.removedirs('newdir1/xx/yy')   # 如果目录为空，删除所有的目录，如果某一层目录不为空，那么包含这一层目录的父目录都不会被删除
# os.remove('test.txt')
if not os.path.exists('mydir'):
    os.mkdir('mydir')
    os.rename('mydir','yourdir')
if os.path.exists('test.txt'):
    os.rename('test.txt','data.txt')
if os.path.exists('bill/mike/john'):
    os.renames('bill/mike/john', 'ok1/ok2/ok3') # 递归地对目录进行更名，也可以对文件进行更名。
if os.path.exists('a/aa.txt'):
    os.renames('a/aa.txt','b/bb.txt')
    os.remove('b/bb.txt')



