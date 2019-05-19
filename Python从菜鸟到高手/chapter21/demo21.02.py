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
# 静态路由和动态路由
# 先静态路由，后动态路由
from flask import Flask
app = Flask('__name__')
@app.route('/')
def index():
    return '<h1>root</h1>'
@app.route('/greet')
def greet():
    return '<h1>Hello everyone</h1>'
@app.route('/greet/lining1')
def greetLining():
    return '<h1>Hello lining</h1>'
# 动态路由
@app.route('/greet/<name>')
def greetName(name):
    return '<h1>hello my {}</h1>'.format(name)
@app.route('/greet/<a1>/<a2>/<a3>')
def args1(a1,a2,a3):
    return '<h1>{},{},{}</h1>'.format(a1,a2,a3)

@app.route('/greet/<a1>-<a2>-<a3>')
def args2(a1,a2,a3):
    return '<h1>{}*{}*{}</h1>'.format(a1,a2,a3)
if __name__ == '__main__':
    app.run()