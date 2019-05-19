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
from socket import *
import os
def responseHeaders(file,length):
    f = open(file,'r')
    
    headersText = f.read()
    headersText = headersText % length
    return headersText

def filePath(get):
    if get == '/':
        return 'static' + os.sep + 'index.html'
    else:
        paths = get.split('/')
        s = 'static'
        for path in paths:
            if path.strip() != '':
                s = s + os.sep + path 
        return s
host = ''
bufferSize = 1024
port = 9876
addr = (host,port)
tcpServerSocket = socket(AF_INET, SOCK_STREAM)
tcpServerSocket.bind(addr)
tcpServerSocket.listen(5)
while True:
    print('正在等待客户端连接')
    tcpClientSocket,addr = tcpServerSocket.accept()
    print('客户端已经连接','addr','=','addr')
    data = tcpClientSocket.recv(bufferSize)
    data = data.decode('utf-8')
    try:
        firstLine = data.split('\n')[0]
        path = firstLine.split(' ')[1]
        print(path)
        path = filePath(path)
        if os.path.exists(path):
            file = open(path,'rb')
            content = file.read()
            file.close()        
        else:
            content = '<h1>File Not Found</h1>'.encode(encoding='utf-8')
        rh = responseHeaders('response_headers.txt',len(content)) + '\r\n'        
        tcpClientSocket.send(rh.encode(encoding='utf-8') + content)
            
    except Exception as e:
        print(e)
    tcpClientSocket.close()
tcpServerSocket.close();
        