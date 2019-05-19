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
import tkinter as tk

window = tk.Tk()
window.title('MenuBar')
window.geometry('200x200')

label = tk.Label(window, width = 20, bg='yellow')
label.pack()
counter = 0
def menuClick():
    global counter
    label.config(text='第 '+ str(counter) + ' 次点击')
    counter+=1

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar)
menubar.add_cascade(label='文件', menu=filemenu)
filemenu.add_command(label='新建', command=menuClick)
filemenu.add_command(label='打开', command=menuClick)
filemenu.add_command(label='保存', command=menuClick)
filemenu.add_separator()
filemenu.add_command(label='退出', command=window.quit)

editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='编辑', menu=editmenu)
editmenu.add_command(label='剪切', command=menuClick)
editmenu.add_command(label='复制', command=menuClick)
editmenu.add_command(label='粘贴', command=menuClick)

submenu = tk.Menu(filemenu)
filemenu.add_cascade(label='导入', menu=submenu)
submenu.add_command(label="导入文本文件", command=menuClick)
submenu.add_command(label="导入pdf文件", command=menuClick)

window.config(menu=menubar)

window.mainloop()
