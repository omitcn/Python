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
import imaplib
import base64
connection = imaplib.IMAP4_SSL('imap.qq.com', 993)


username = '邮箱用户名'
password = '邮箱密码'
 
# 登陆
try:
    connection.login(username, password)
except Exception as err:
    print('登陆失败: :', err)  # 输出登陆失败的原因
 
# 输出日志
connection.print_log()
res,data = connection.list()
print('Response code:', data)

    
res, data = connection.select('INBOX')

print(res, data)
print(data[0])  # 邮件数

res, msg_ids = connection.search(None, 'ALL')  # 你也可以直接搜索邮件
print(res, msg_ids)
res, msg_data = connection.fetch(data[0], '(UID BODY[TEXT])') # '(UID BODY[TEXT])'  '(BODY.PEEK[TEXT])'
print(msg_data)
connection.logout()