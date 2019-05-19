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
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QFrame, QApplication)
from PyQt5.QtGui import QColor
import sys

class PushButton(QWidget):
    
    def __init__(self):
        super().__init__()        
        self.initUI()
        
    def initUI(self):      

        self.color = QColor(0, 0, 0)       
        
        redButton = QPushButton('红', self)
        redButton.setCheckable(True)
        redButton.move(10, 10)
        redButton.clicked[bool].connect(self.setColor)

        greenButton = QPushButton('绿', self)
        greenButton.setCheckable(True)
        greenButton.move(10, 60)

        greenButton.clicked[bool].connect(self.setColor)

        blueButton = QPushButton('蓝', self)
        blueButton.setCheckable(True)
        blueButton.move(10, 110)

        blueButton.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" %  
            self.color.name())
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('按钮控件')
        self.show()
        
        
    def setColor(self, pressed):
        
        source = self.sender()
        
        if pressed:
            val = 255
        else: val = 0
                        
        if source.text() == "红":
            self.color.setRed(val)                
        elif source.text() == "绿":
            self.color.setGreen(val)             
        else:
            self.color.setBlue(val) 
            
        self.square.setStyleSheet("QFrame { background-color: %s }" %
            self.color.name())  
       
       
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = PushButton()
    sys.exit(app.exec_())