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

import poplib

import re
# pop3服务器地址
host = "pop.126.com"
# 用户名
username = "邮箱账号" # 如abcd@126.com
# 密码
password = "邮箱密码"

#pp = poplib.POP3(host)
pp = poplib.POP3_SSL(host)
# 设置调试模式，可以看到与服务器的交互信息
pp.set_debuglevel(1)
# 向服务器发送用户名
pp.user(username)
# 向服务器发送密码
pp.pass_(password)
# 获取服务器上信件信息，返回是一个列表，第一项是一共有多上封邮件，第二项是共有多少字节
ret = pp.stat()

# 需要取出所有信件的头部，信件id是从1开始的。
mailCount = ret[0]
print('一共',mailCount,'封邮件')
for i in range(1, mailCount):
    # 取出信件头部。注意：top指定的行数是以信件头为基数的，也就是说当取0行，
    # 其实是返回头部信息，取1行其实是返回头部信息之外再多1行。
    try:
        mlist = pp.top(i, 0)
        print(mlist[1])
        print(mlist[1][7])
        if i > 20: break;
    except:
        pass

# 列出服务器上邮件信息，这个会对每一封邮件都输出id和大小。不象stat输出的是总的统计信息
ret = pp.list()

# 取第一封邮件完整信息，在返回值里，是按行存储在down[1]的列表里的。down[0]是返回的状态信息
#down = pp.retr(mailCount)
down = pp.retr(1)


# 输出邮件
charset = ''
for line in down[1]:  
    result = re.search('charset\s*=\s*"([^\"]*)"',line.decode('ISO-8859-1'))   
    if result != None:
        charset = result.group(1)
        print(charset)        
    if charset != '':
        print(line.decode(charset))

# 退出
pp.quit()