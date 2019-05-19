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
from PyQt5.QtWidgets import (QWidget, QLabel, 
    QComboBox, QApplication)
import sys

class ComboBox(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        self.lbl = QLabel("中国", self)
        self.lbl.move(50, 150) 
        combo = QComboBox(self)
        combo.addItem("中国")
        combo.addItem("美国")
        combo.addItem("法国")
        combo.addItem("德国")
        combo.addItem("俄罗斯")
        combo.addItem("澳大利亚")
        combo.move(50, 50)
        self.lbl.move(50, 150)

        combo.activated[str].connect(self.onActivated)        
         
        combo1 = QComboBox(self)
        combo1.addItem("Item1")
        combo1.addItem("Item2")
        combo1.addItem("Item3")
        combo1.move(200, 50)
 
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QComboBox控件')
        self.show()
        
        
    def onActivated(self, text):
      
        self.lbl.setText(text)
        self.lbl.adjustSize()  
        
                
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ComboBox()
    sys.exit(app.exec_())