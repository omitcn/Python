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
<<<<<<< HEAD
import tkinter

window = tkinter.Tk()
window['background']='blue'
w = 300
h = 200
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
print(ws)
x = (ws/2) - (w/2)     
y = (hs/2) - (h/2)
window.title('第一个tkinter应用')


window.geometry('%dx%d+%d+%d' % (w, h, x, y)) 

label = tkinter.Label(window, text='Hello World!')
label.pack()
=======
# 导入tkinter模块
import tkinter
# 创建Tk类的实例，也就是要显示的窗口
window = tkinter.Tk()
# 设置窗口背景为蓝色
window['background']='blue'
# 定义窗口的宽度
w = 300
# 定义窗口的高度
h = 200
# 获取屏幕宽度
ws = window.winfo_screenwidth()
# 获取屏幕高度
hs = window.winfo_screenheight()
# 根据屏幕宽度和窗口宽度计算让窗口水平居中的x坐标值
x = (ws/2) - (w/2)   
# 根据屏幕高度和窗口高度计算让窗口垂直居中的y坐标值
y = (hs/2) - (h/2)
# 设置窗口标题
window.title('第一个tkinter应用')
# 设置窗口的尺寸和位置
window.geometry('%dx%d+%d+%d' % (w, h, x, y)) 
# 创建Label对象，并将Label放在窗口上，文本显示“Hello World”
label = tkinter.Label(window, text='Hello World!')
# 使用Pack布局让Label水平居中
label.pack()
# 调用mainloop函数进入事件循环
>>>>>>> branch 'master' of https://geekori@bitbucket.org/oridemo/pythonsamples.git
tkinter.mainloop()
