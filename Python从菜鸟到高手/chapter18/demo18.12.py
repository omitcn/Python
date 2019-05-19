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
import random  
      
window = tk.Tk() 
window.title('Label控件和Button控件') 
window['background']='blue'
window.geometry("300x200+30+30")          

label1 = tk.Label(window, 
    text='Hello World',  
    bg='green', font=('Arial', 12), width=20, height=2)
label1.pack()
var = tk.StringVar() 
var.set('Hello World')  
label2 = tk.Label(window, 
    textvariable=var,
    fg = 'blue',   
    bg='yellow', font=('Arial', 12), width=15, height=2)
label2.pack(pady = 20) 
onHit = False  
def hitMe():
    global onHit
    if onHit == False:     
        onHit = True
        var.set('世界你好')  
    else:      
        onHit = False
        var.set('Hello World') 
button1 = tk.Button(window, 
    text='点击我', 
    command=hitMe)     
button1.pack()
def getLabelText():
    print(var.get())
button2 = tk.Button(window, 
    text='获取Label控件的文本', 
    command=getLabelText)     
button2.pack(pady = 20)   
   


window.mainloop()  