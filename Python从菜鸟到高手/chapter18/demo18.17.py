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
window.title('Listbox控件')
window.geometry('200x200')
window['background'] = 'blue'

var1 = tk.StringVar()
l = tk.Label(window, bg='yellow', width=10, textvariable=var1)
l.pack()


var2 = tk.StringVar()
var2.set((11,22,33,44))
lb = tk.Listbox(window, listvariable=var2)
def onselect(evt):
    w = evt.widget
    value = w.get(w.curselection())
    var1.set(value)
lb.bind('<<ListboxSelect>>', onselect)
lb.selection_set(first=0)
value = lb.get(lb.curselection())
var1.set(value)


list_items = [11111,22222,3333,4444]
for item in list_items:
    lb.insert('end', item)
lb.insert(1, 'Python')
lb.insert(2, 'Kotlin')
lb.insert(3, 'Swift')
lb.delete(2)
lb.pack(pady = 20)

window.mainloop()