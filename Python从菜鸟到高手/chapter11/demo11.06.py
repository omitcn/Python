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
import re
# abc aabc   abbbccc
s = 'a+b+c+'
strList = ['abc','aabc','bbabc','aabbbcccxyz']
for value in strList:    
    m = re.match(s, value)
    if m is not None:
        print(m.group())
    else:
        print('{}不匹配{}'.format(value,s))

print('--------------')

# 任意3个数字-任意3个小写字母  
# 123-abc   433-xyz
#s = '\d\d\d-[a-z][a-z][a-z]'
s = '\d{3}-[a-z]{3}'  
strList = ['123-abc','432-xyz','1234-xyz','1-xyzabc','543-xyz^%ab']
for value in strList:    
    m = re.match(s, value)
    if m is not None:
        print(m.group())
    else:
        print('{}不匹配{}'.format(value,s))
print('-------------')
s = '[a-z]?\d+'
strList = ['1234','a123','ab432','b234abc']
for value in strList:    
    m = re.match(s, value)
    if m is not None:
        print(m.group())
    else:
        print('{}不匹配{}'.format(value,s))

print('-------------')
# email
email = '\w+@(\w+\.)*\w+\.com'
emailList = ['abc@126.com','test@mail.geekori.com','test-abc@geekori.com','abc@geekori.com.cn']
for value in emailList:    
    m = re.match(email,value)
    if m is not None:
        print(m.group())
    else:
        print('{}不匹配{}'.format(value,email))
strValue = '我的email是lining@geekori.com，请发邮件到这个邮箱'
m = re.search(email, strValue)
print(m)
email = '[a-zA-Z0-9]+@(\w+\.)*\w+\.com'
m = re.search(email, strValue)
print(m)


