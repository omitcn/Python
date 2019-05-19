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
import ftplib

host = 'localhost'
def dirCallback(dir):
    print(dir.encode('ISO-8859-1').decode('utf-8'))
def main():
    try:
        f = ftplib.FTP(host)
  
    except Exception as e:
        print(e)
        return
    print('FTP服务器已经成功连接')
    try:
        f.login('用户名','密码')
    except Exception as e:
        print(e)
        return    
    print('FTP服务器已经成功登录.')
    f.cwd('Pictures')
    f.dir(dirCallback)
    print('当前工作目录：',f.pwd())
    try:
        f.mkd('新目录'.encode('GBK').decode('ISO-8859-1'))
        f.cwd('新目录'.encode('GBK').decode('ISO-8859-1'))
        f.mkd('dir1')
        f.mkd('dir2')
    except:
        f.cwd('新目录'.encode('utf-8').decode('ISO-8859-1'))
        
    print('-----')

   
    upload_file = '/Users/lining/Desktop/a.png'
    ff = open(upload_file,'rb')
    
    print(f.storbinary('STOR %s' % 'a.png',ff))
    f.dir(dirCallback)

    print(f.retrbinary('RETR %s' % 'a.png',open('/Users/lining/Desktop/xx.png','wb').write))
    f.quit()
    
if __name__ == '__main__':
    main()