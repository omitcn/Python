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
import sys
import Login
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox
from PyQt5.QtCore import QCoreApplication
if __name__ == '__main__':
    def usr_login():
        usr_name = ui.lineEditUserName.text()
        usr_pwd = ui.lineEditPassword.text()
        if usr_name == 'geekori' and usr_pwd == '1234':
            QMessageBox.information(MainWindow, '消息',
            "登录成功")

        else:
            QMessageBox.warning(MainWindow, '消息',
            "用户名或密码错误")      
        print()
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Login.Ui_MainWindow()
    # 调用setupUi方法动态创建控件
    ui.setupUi(MainWindow)
    ui.pushButtonOK.clicked[bool].connect(usr_login)
    ui.pushButtonCancel.clicked.connect(QCoreApplication.instance().quit)
    # 显示窗口
    MainWindow.show()
   
    # 当窗口关闭后会退出程序
    sys.exit(app.exec_())
    