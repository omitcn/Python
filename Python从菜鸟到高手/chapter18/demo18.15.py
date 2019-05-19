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
window.title('Checkbutton控件')
window.geometry('200x200')
window['background'] = 'blue'
label = tk.Label(window, bg='yellow', width=20, text='empty')
label.pack()

def printSelection():
    text = ''
    if var1.get() == 1:
        text += ' ' + c1.cget('text')
    if var2.get() == 1:
        text += ' ' + c2.cget('text')
    if var3.get() == 1:
        text += ' ' + c3.cget('text')
    if var4.get() == 1:
        text += ' ' + c4.cget('text')
    label.config(text=text)

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0,
                    command=printSelection)
c2 = tk.Checkbutton(window, text='C++', variable=var2, onvalue=1, offvalue=0,
                    command=printSelection)
c3 = tk.Checkbutton(window, text='Kotlin', variable=var3, onvalue=1, offvalue=0,
                    command=printSelection)
c4 = tk.Checkbutton(window, text='Swift', variable=var4, onvalue=1, offvalue=0,
                    command=printSelection)

c1.pack()
c2.pack()
c3.pack()
c4.pack()


window.mainloop()
