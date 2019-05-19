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
import tkinter.messagebox

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

def hit_me():
    tk.messagebox.showinfo(title='信息对话框', message='这是我要的信息')   # return 'ok'
    tk.messagebox.showwarning(title='警告对话框', message='这是警告信息')   # return 'ok'
    tk.messagebox.showerror(title='错误对话框', message='这是错误信息')   # return 'ok'
    print(tk.messagebox.askquestion(title='询问对话框', message='你要干嘛？'))   # return 'yes' , 'no'
    print(tk.messagebox.askyesno(title='yes/no', message='请给出你的选择'))   # return True, False
    print(tk.messagebox.askokcancel(title='ok/cancal', message='确定/取消'))   # return True, False
    print(tk.messagebox.askyesnocancel(title="yes/no/cancel", message="请给出你的选择"))     # return, True, False, None

tk.Button(window, text='hit me', command=hit_me).pack()
window.mainloop()
