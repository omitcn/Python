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
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication

class Menu(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
    def initUI(self):                 
        menubar = self.menuBar()
        print(menubar)
        fileMenu = menubar.addMenu('文件')
        newAct = QAction('新建', self)   
        impMenu = QMenu('导入', self)
        impAct1 = QAction('从PDF导入', self) 
        impAct2= QAction('从Word导入', self) 
        impAct1.triggered.connect(self.actionHandler1)
        impAct2.triggered.connect(self.actionHandler2)
        impMenu.addAction(impAct1)
        impMenu.addAction(impAct2)
        
        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('菜单')    
        self.show()
    def actionHandler1(self):          
        print('从PDF导入')    
    def actionHandler2(self):          
        print('从Word导入')       
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Menu()
    sys.exit(app.exec_())