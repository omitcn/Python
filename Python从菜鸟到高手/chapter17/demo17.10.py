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
from atexit import register
from random import randrange
from threading import BoundedSemaphore, Lock, Thread
from time import sleep, ctime

lock = Lock()
MAX = 5
candytray = BoundedSemaphore(MAX)

def refill():
    lock.acquire()
    print('重新添加糖果...', end=' ')
    try:
        candytray.release()
    except ValueError:
        print('糖果机都满了，无法添加')
    else:
        print('成功添加糖果')
    lock.release()

def buy():
    lock.acquire()
    print('购买糖果...', end=' ')
    if candytray.acquire(False):
        print('成功购买糖果')
    else:
        print('糖果机为空，无法购买糖果')
    lock.release()

def producer(loops):
    for i in range(loops):
        refill()
        sleep(randrange(3))

def consumer(loops):
    for i in range(loops):
        buy()
        sleep(randrange(3))

def main():
    print('开始:', ctime())
    nloops = randrange(2, 6)
    print('糖果机共有%d个槽!' % MAX)
    Thread(target=consumer, args=(randrange(
        nloops, nloops+MAX+2),)).start() 
    Thread(target=producer, args=(nloops,)).start() 

@register
def exit():
    print('程序执行完毕：', ctime())

if __name__ == '__main__':
    main()

