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
# 读取和设置节点的属性
html = '''
<html>
    <head><title>index</title></head>
    <body attr='test xyz' class='style1 style2'>
        <a rel='ok1 ok2 ok3' class='a1 a2' href='a.html'>first page</a>
        <p>
        <a href='b.html'>second page</a>
        <p>
        <a  href='c.html'>third page</a>
        <p>
        <x k='123' attr1='hello' attr2='world'>hello</x>
    </body>
</html>
'''
from bs4 import *

soup = BeautifulSoup(html,'lxml')
print(type(soup.body.attrs))
print('body.class','=',soup.body['class'])
print('body.attr','=',soup.body['attr'])
print('a.class','=',soup.a['class'])
soup.x['attr1'] = 'ok'
print('x.attr1','=',soup.x['attr1'])

soup.body['class'] = ['x','y','z']
soup.body['class'].append('ok')
print(soup.body)
print(soup.a['rel'])
# class、rel,rev,accept-charset,headers,accesskey

