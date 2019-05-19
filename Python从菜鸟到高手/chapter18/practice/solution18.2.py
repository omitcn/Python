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
from tkinter import *
import math
window = Tk()
window.title('计算器') 

Button(window,text="=",width=10).grid(row=4, column=4,columnspan=2)
Button(window,text='AC',width=3).grid(row=1, column=4)
Button(window,text='C',width=3).grid(row=1, column=5)
Button(window,text="+",width=3).grid(row=4, column=3)
Button(window,text="x",width=3).grid(row=2, column=3)
Button(window,text="-",width=3).grid(row=3, column=3)
Button(window,text="÷",width=3).grid(row=1, column=3) 
Button(window,text="%",width=3).grid(row=4, column=2)
Button(window,text="7",width=3).grid(row=1, column=0)
Button(window,text="8",width=3).grid(row=1, column=1)
Button(window,text="9",width=3).grid(row=1, column=2)
Button(window,text="4",width=3).grid(row=2, column=0)
Button(window,text="5",width=3).grid(row=2, column=1)
Button(window,text="6",width=3).grid(row=2, column=2)
Button(window,text="1",width=3).grid(row=3, column=0)
Button(window,text="2",width=3).grid(row=3, column=1)
Button(window,text="3",width=3).grid(row=3, column=2)
Button(window,text="0",width=3).grid(row=4, column=0)
Button(window,text=".",width=3).grid(row=4, column=1)
Button(window,text="(",width=3).grid(row=2, column=4)
Button(window,text=")",width=3).grid(row=2, column=5)
Button(window,text="√",width=3).grid(row=3, column=4)
Button(window,text="x²",width=3).grid(row=3, column=5)


window.mainloop()