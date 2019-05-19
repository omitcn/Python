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
from PyQt5.QtWidgets import (QWidget, QProgressBar, 
    QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer
import sys

class ProgressBar(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
    def initUI(self):      

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(40, 40, 200, 25)
         
        self.btn = QPushButton('开始', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.value = 0
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar控件')
        self.show()
        
        
    def timerEvent(self, e):
      
        if self.value >= 100:
            self.timer.stop()
            self.btn.setText('完成')
            return            
        self.value = self.value + 1
        self.pbar.setValue(self.value)
        

    def doAction(self):
      
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('开始')
        else:
            self.timer.start(100, self)
            self.btn.setText('停止')
            
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ProgressBar()
    sys.exit(app.exec_())