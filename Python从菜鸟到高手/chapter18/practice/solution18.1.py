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
from tkinter import messagebox  # import this to fix messagebox error
import pickle

window = tk.Tk()
window.title('登录窗口')
window.geometry('450x200')



# user information
tk.Label(window, text='User name: ').place(x=50, y= 10)
tk.Label(window, text='Password: ').place(x=50, y= 50)

var_usr_name = tk.StringVar()
var_usr_name.set('geekori')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=10)
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=50)

def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    if usr_name == 'geekori' and usr_pwd == '1234':
        tk.messagebox.showinfo(title='登录', message='登录成功')
    else:
        tk.messagebox.showerror(message='用户名或密码错误！')

btn_login = tk.Button(window, text='登录', command=usr_login)
btn_login.place(x=180, y=90)
btn_cancel = tk.Button(window, text='取消', command=window.quit)
btn_cancel.place(x=250, y=90)


window.mainloop()
