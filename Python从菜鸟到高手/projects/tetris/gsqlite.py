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
#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

This is a Tetris game clone.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

from PyQt5.QtWidgets import QMainWindow, QWidget,QFrame, QDesktopWidget,QAction,QMenu,QApplication,QLabel,QMessageBox,QInputDialog,QLineEdit,QPushButton
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor 
from pymysql import *
import sys, random
import time,os
import pygame
import sqlite3


class Start(QWidget):
    def __init__(self):
        super().__init__()
        self.startUI()
    def startUI(self):
        qbtn = QPushButton('注册', self)
        qbtn.clicked.connect(self.register)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(100, 156)       
        
        qbtn1 = QPushButton('登录', self)
        qbtn1.clicked.connect(self.login)
        qbtn1.resize(qbtn.sizeHint())
        qbtn1.move(100, 216)       
        
        self.resize(275, 400)
        self.center()
        self.setWindowTitle('入口')        
        self.show()    
    
    def register(self):
        a=self.close()
        if a:
            self.next=register()
            self.next.show()    
    
    def login(self):
        if os.path.exists("time.txt"):
            f=open("time.txt")
            ptime=f.read()
            f.close()
            d2=int(round(time.time()))
            if (d2-int(round(float(ptime))))<0:
                result=self.close()
                if result:
                    self.next=Tetris()
                    self.next.show()
            else:
                result=self.close()
                if result:
                    self.next=Login()
                    self.next.show()                    
                
        else:        
            a=self.close()
            if a:
                self.next=Login()
                self.next.show()      
    def center(self):
        '''centers the window on the screen'''
        
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, 
            (screen.height()-size.height())/2)        

class Login(QWidget):
    def __init__(self):
        super().__init__()
        
        self.loginUI()
    def loginUI(self):
        
                   
        self.le = QLineEdit(self)

        self.le.setPlaceholderText('请输入用户名')
        self.le.resize(200,30)
        self.le.move(50, 66)
                 
        self.les = QLineEdit(self)

        self.les.setPlaceholderText('请输入密码')
        self.les.setEchoMode(QLineEdit.Password)
        self.les.resize(200,30)
        self.les.move(50, 146)
        
        qbtn = QPushButton('登录', self)
        qbtn.clicked.connect(self.start)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(150, 216)       
        
        self.resize(300, 400)
        self.center()
        self.setWindowTitle('登录')

    def start(self):
        users=User()
        username=self.getName()
        password=self.getPwd()
        num=users.check(username, password)
        if num>0:
            a=self.close()
            times=str(time.time()+3600)
            
            with open("time.txt","w") as f:
                f.write(times)
                f.close()                    
            if a:
                self.next=Tetris()
                self.next.show()
        else:
            QMessageBox.information(self,"登录err","登录失败?账号或密码错误！",QMessageBox.Yes|QMessageBox.No) 
                
                    
    def getName(self):
        a=self.le.text()
        return a
    def getPwd(self):
        a=self.les.text()
        return a
    def center(self):
        '''centers the window on the screen'''
        
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, 
            (screen.height()-size.height())/2)
    

#注册部分
class register(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.registerUI()
    def registerUI(self):
        
                   
        self.le = QLineEdit(self)

        self.le.setPlaceholderText('请输入用户名')
        self.le.resize(200,30)
        self.le.move(50, 66)
                         
        
        self.les = QLineEdit(self)
        self.les.setPlaceholderText('请输入密码')
        self.les.setEchoMode(QLineEdit.Password)
        self.les.resize(200,30)
        self.les.move(50, 146)
        
        qbtn = QPushButton('注册', self)
        qbtn.clicked.connect(self.start)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(150, 216)       
        
        self.resize(300, 400)
        self.center()
        self.setWindowTitle('注册')        
        #self.show()    
    def start(self):
        users=User()
        username=self.getName()
        password=self.getPwd()
        users.create(username, password)
        times=str(time.time()+3600)
        with open("time.txt","w") as f:
            f.write(times)           
        result=self.close()
        if result:
            self.next=Tetris()
            self.next.show()
    def getName(self):
        a=self.le.text()
        return a
    def getPwd(self):
        a=self.les.text()
        return a
    def center(self):
        '''centers the window on the screen'''
        
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, 
            (screen.height()-size.height())/2)
    
    


#俄罗斯方块窗口部分代码
class Tetris(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):    
        '''initiates application UI'''
          
        self.tboard = Board(self)
        #self.setCentralWidget(self.tboard)
        self.tboard.setGeometry(150,0,400,700)
        self.rank=Rank(self)
        self.rank.setGeometry(0,0,150,700)
        self.statusbar = self.statusBar()        
        self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)
        
        self.tboard.start()
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('文件')
        
        impMenu = QMenu('功能', self)
        impAct = QAction('注销', self) 
        impMenu.addAction(impAct)
        
        fileMenu.addMenu(impMenu)
        impAct.triggered.connect(self.clear)
        
        self.resize(550, 720)
        self.center()
        self.setWindowTitle('Tetris')        
        #self.show()
    
    def clear(self):
        ok=QMessageBox.information(self,"注销","是否注销?",QMessageBox.Yes|QMessageBox.No)
        if ok== QMessageBox.Yes:
            os.remove('time.txt')
            os.remove('credentials.txt')
            self.close()
            
               
                
    def quit(self):
        self.close()
    def show_t(self):
        self.show()         

    def center(self):
        '''centers the window on the screen'''
        
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, 
            (screen.height()-size.height())/2)
        
           
class User():
    def conn(self):
        conn = sqlite3.connect(dbPath)
        return conn
    def create(self,name,pwd):
        
        username=name
        password=pwd    
        db=self.conn()
        cursor=db.cursor()
        sql="INSERT INTO t_rank_user (username,pwd) VALUES ('%s','%s')" %(username,password)
        try:   
            cursor.execute(sql)
            db.commit()
            with open("credentials.txt","w") as f:
                f.write(username)        
                
        except:
            db.rollback()
        
    def check(self,name,pwd):        
        username=name
        password=pwd    
        db=self.conn()
        cursor=db.cursor()
        sql="select * from t_rank_user where username='%s' and pwd='%s'" %(username,password)
        try:   
            cursor.execute(sql)
            result=cursor.fetchall()
            num=len(result)
            
            if num>0:
                with open("credentials.txt","w") as f:
                    f.write(username)
                     
            return num        
        except:
            db.rollback()
            
    def query(self,name):
        username=name
        db=self.conn()
        cursor=db.cursor()
        sql="select * from  t_rank_user where username='%s'" %(username)
        try:   
            cursor.execute(sql)
            num=cursor.rowcount
            return num
        except:
            db.rollback()  
    def queryrank(self):
        db=self.conn()
        cursor=db.cursor()
        sql="select * from  t_rank_user order by rank desc limit 10"
        try:   
            cursor.execute(sql)
            result=cursor.fetchall()
            return result
        except:
            db.rollback()         
    def update(self,rank):
        ranks=rank
        print(ranks)
        f=open("credentials.txt")
        username=f.read()
        f.close()
        print(username)
        db=self.conn()
        cursor=db.cursor()
        sql="select * from  t_rank_user where username='%s'" %(username)
        try:   
            cursor.execute(sql)
            result=cursor.fetchall()
            value=result[0][2]
            #
        except:
            db.rollback()
        if value<ranks:
            sql1="update t_rank_user set rank='%s' where username='%s'" %(ranks,username)
            try:
                cursor.execute(sql1)
                db.commit()
                QMessageBox.information(Tetris(),"恭喜","恭喜你创造新的个人记录！",QMessageBox.Yes)
            except:
                db.rollback()
        else:
            QMessageBox.information(Tetris(),"鼓励","再接再厉哦！",QMessageBox.Yes) 
                                       
    def randomname(self):
        seed = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        sa = []
        for i in range(8):
            sa.append(random.choice(seed))
        salt = ''.join(sa)
        return salt        
class music():
    
    def start(self):
        file=r'./els.mp3'
        pygame.mixer.init()
        track = pygame.mixer.music.load(file)
        pygame.mixer.music.play()
                
    def stop(self):
        pygame.mixer.music.pause()
    def cont(self):
        pygame.mixer.music.unpause()
    def clearmusic(self):
        time.sleep(0.8)
class Rank(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.initrank()
    def initrank(self):
        self.square = QFrame(self)
        self.square.setGeometry(0, 0,150,700)
        self.square.setStyleSheet("QWidget { background-color:#fc9898}")
        
        self.lb=QLabel(self)
        self.lb.setText('游戏排行榜')
        self.lb.setStyleSheet("QLabel {color:#f1f28a;font-size:18px;font-weight:900;padding-top:10px;text-align:center;}")
        self.lb.move(0,0)
        a=1 
        users=User()
        info=users.queryrank()
        rnum=len(info)
        if rnum<10:
            num=rnum
        else:
            num=10    
        while a<=num:
            lbs="lb"+str(a)
            h=a*30
            b=int(a)-1
            infos=info[b]
            name=infos[1]
            rank=infos[2]
            self.lbs=QLabel(self)
            self.lbs.resize(150,30)
            self.lbs.setText(str(a)+":"+name+"---"+str(rank)+"分")
            self.lbs.setStyleSheet("QLabel {font-size:13px;padding-top:10px;}")
            self.lbs.move(0,h) 
            a+=1         
class Board(QFrame):
    
    msg2Statusbar = pyqtSignal(str)
    BoardWidth = 10
    BoardHeight = 22
    Speed = 300

    def __init__(self, parent):
        super().__init__(parent)
        music.start(self)
        self.initBoard()        
    
           
    def initBoard(self):     
        '''initiates board'''

        self.timer = QBasicTimer()
        self.isWaitingAfterLine = False
        
        self.curX = 0
        self.curY = 0
        self.numLinesRemoved = 0
        self.board = []

        self.setFocusPolicy(Qt.StrongFocus)
        self.isStarted = False
        self.isPaused = False
        self.clearBoard()
        
        
    def shapeAt(self, x, y):
        '''determines shape at the board position'''
        
        return self.board[(y * Board.BoardWidth) + x]

        
    def setShapeAt(self, x, y, shape):
        '''sets a shape at the board'''
        
        self.board[(y * Board.BoardWidth) + x] = shape
        

    def squareWidth(self):
        '''returns the width of one square'''
        
        return self.contentsRect().width() // Board.BoardWidth
        

    def squareHeight(self):
        '''returns the height of one square'''
        
        return self.contentsRect().height() // Board.BoardHeight
        

    def start(self):
        '''starts game'''
        if os.path.exists("credentials.txt"):
            f=open("credentials.txt")
            username=f.read()
            f.close()
        else:
            username="路人"    
        if self.isPaused:
            return

        self.isStarted = True
        self.isWaitingAfterLine = False
        self.numLinesRemoved = 0
        self.clearBoard()

        self.msg2Statusbar.emit(username+":"+str(self.numLinesRemoved))

        self.newPiece()
        self.timer.start(Board.Speed, self)

        
    def pause(self):
        username=''
        if os.path.exists("credentials.txt"):
            f=open("credentials.txt")
            username=f.read()
            f.close()
  

        if not self.isStarted:
            return

        self.isPaused = not self.isPaused
        
        if self.isPaused:
            self.timer.stop()
            self.msg2Statusbar.emit("paused")
            
        else:
            self.timer.start(Board.Speed, self)
            self.msg2Statusbar.emit(username+":"+str(self.numLinesRemoved))

    

        
    def paintEvent(self, event):
        '''paints all shapes of the game'''
        
        painter = QPainter(self)
        rect = self.contentsRect()
    
        boardTop = rect.bottom() - Board.BoardHeight * self.squareHeight()
    
        for i in range(Board.BoardHeight):
            for j in range(Board.BoardWidth):
                shape = self.shapeAt(j, Board.BoardHeight - i - 1)
                
                if shape != Tetrominoe.NoShape:
                    self.drawSquare(painter,
                        rect.left() + j * self.squareWidth(),
                        boardTop + i * self.squareHeight(), shape)
    
        if self.curPiece.shape() != Tetrominoe.NoShape:
            
            for i in range(4):
                
                x = self.curX + self.curPiece.x(i)
                y = self.curY - self.curPiece.y(i)
                self.drawSquare(painter, rect.left() + x * self.squareWidth(),
                    boardTop + (Board.BoardHeight - y - 1) * self.squareHeight(),
                    self.curPiece.shape())

                    
    def keyPressEvent(self, event):
        if not self.isStarted or self.curPiece.shape() == Tetrominoe.NoShape:
            super(Board, self).keyPressEvent(event)
            return
    
        key = event.key()
        
        if key == Qt.Key_P:
           
            self.pause()
            return
            
        if self.isPaused:
            return
                
        elif key == Qt.Key_Left:
            self.tryMove(self.curPiece, self.curX - 1, self.curY)
            
        elif key == Qt.Key_Right:
            self.tryMove(self.curPiece, self.curX + 1, self.curY)
            
        elif key == Qt.Key_Down:
            self.tryMove(self.curPiece.rotateRight(), self.curX, self.curY)
            
        elif key == Qt.Key_Up:
            self.tryMove(self.curPiece.rotateLeft(), self.curX, self.curY)
            
        elif key == Qt.Key_Space:
            self.dropDown()
            
        elif key == Qt.Key_D:
            self.oneLineDown()
            
        else:
            super(Board, self).keyPressEvent(event)
                

    def timerEvent(self, event):
        '''handles timer event'''
        
        if event.timerId() == self.timer.timerId():
            
            if self.isWaitingAfterLine:
                self.isWaitingAfterLine = False
                self.newPiece()
            else:
                self.oneLineDown()
                
        else:
            super(Board, self).timerEvent(event)

            
    def clearBoard(self):
        '''clears shapes from the board'''
        
        for i in range(Board.BoardHeight * Board.BoardWidth):
            self.board.append(Tetrominoe.NoShape)

        
    def dropDown(self):
        '''drops down a shape'''
        
        newY = self.curY
        
        while newY > 0:
            
            if not self.tryMove(self.curPiece, self.curX, newY - 1):
                break
                
            newY -= 1

        self.pieceDropped()
        

    def oneLineDown(self):
        '''goes one line down with a shape'''
        
        if not self.tryMove(self.curPiece, self.curX, self.curY - 1):
            self.pieceDropped()
            

    def pieceDropped(self):
        '''after dropping shape, remove full lines and create new shape'''
        
        for i in range(4):
            
            x = self.curX + self.curPiece.x(i)
            y = self.curY - self.curPiece.y(i)
            self.setShapeAt(x, y, self.curPiece.shape())

        self.removeFullLines()

        if not self.isWaitingAfterLine:
            self.newPiece()
            

    def removeFullLines(self):
        '''removes all full lines from the board'''
        
        numFullLines = 0
        rowsToRemove = []

        for i in range(Board.BoardHeight):
            
            n = 0
            for j in range(Board.BoardWidth):
                if not self.shapeAt(j, i) == Tetrominoe.NoShape:
                    n = n + 1

            if n == 10:
                rowsToRemove.append(i)

        rowsToRemove.reverse()
        

        for m in rowsToRemove:
            
            for k in range(m, Board.BoardHeight):
                for l in range(Board.BoardWidth):
                        self.setShapeAt(l, k, self.shapeAt(l, k + 1))

        numFullLines = numFullLines + len(rowsToRemove)
        if os.path.exists("credentials.txt"):
            f=open("credentials.txt")
            username=f.read()
            f.close()
        else:
            username="路人"    
        
        if numFullLines > 0:
            music.stop(self)
            time.sleep(1)
            music.cont(self)
            self.numLinesRemoved = self.numLinesRemoved + numFullLines
            self.msg2Statusbar.emit(username+":"+str(self.numLinesRemoved))
               
            self.isWaitingAfterLine = True
            
            self.curPiece.setShape(Tetrominoe.NoShape)
             
            self.update()
           
        
    def clearmusic(self):
        file=r'clear.mp3'
        pygame.mixer.init()
        track = pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        time.sleep(0.8)
        pygame.mixer.music.stop()
        
            
    def newPiece(self):
        '''creates a new shape'''
        
        self.curPiece = Shape()
        self.curPiece.setRandomShape()
        self.curX = Board.BoardWidth // 2 + 1
        self.curY = Board.BoardHeight - 1 + self.curPiece.minY()
        
        if not self.tryMove(self.curPiece, self.curX, self.curY):
            
            self.curPiece.setShape(Tetrominoe.NoShape)
            self.timer.stop()
            self.isStarted = False
            num=self.numLinesRemoved
            users=User()
            users.update(num)
            self.msg2Statusbar.emit("Game over")



    def tryMove(self, newPiece, newX, newY):
        '''tries to move a shape'''
        
        for i in range(4):
            
            x = newX + newPiece.x(i)
            y = newY - newPiece.y(i)
            
            if x < 0 or x >= Board.BoardWidth or y < 0 or y >= Board.BoardHeight:
                return False
                
            if self.shapeAt(x, y) != Tetrominoe.NoShape:
                return False

        self.curPiece = newPiece
        self.curX = newX
        self.curY = newY
        self.update()
        
        return True
        

    def drawSquare(self, painter, x, y, shape):
     
        
        colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]
    
        color = QColor(colorTable[shape])
        painter.fillRect(x + 1, y + 1, self.squareWidth() - 2, 
            self.squareHeight() - 2, color)
    
        painter.setPen(color.lighter())
        painter.drawLine(x, y + self.squareHeight() - 1, x, y)
        painter.drawLine(x, y, x + self.squareWidth() - 1, y)
    
        painter.setPen(color.darker())
        painter.drawLine(x + 1, y + self.squareHeight() - 1,
            x + self.squareWidth() - 1, y + self.squareHeight() - 1)
        painter.drawLine(x + self.squareWidth() - 1, 
            y + self.squareHeight() - 1, x + self.squareWidth() - 1, y + 1)


class Tetrominoe(object):
    
    NoShape = 0
    ZShape = 1
    SShape = 2
    LineShape = 3
    TShape = 4
    SquareShape = 5
    LShape = 6
    MirroredLShape = 7


class Shape(object):
    
    coordsTable = (
        ((0, 0),     (0, 0),     (0, 0),     (0, 0)),
        ((0, -1),    (0, 0),     (-1, 0),    (-1, 1)),
        ((0, -1),    (0, 0),     (1, 0),     (1, 1)),
        ((0, -1),    (0, 0),     (0, 1),     (0, 2)),
        ((-1, 0),    (0, 0),     (1, 0),     (0, 1)),
        ((0, 0),     (1, 0),     (0, 1),     (1, 1)),
        ((-1, -1),   (0, -1),    (0, 0),     (0, 1)),
        ((1, -1),    (0, -1),    (0, 0),     (0, 1))
    )

    def __init__(self):
        
        self.coords = [[0,0] for i in range(4)]
        self.pieceShape = Tetrominoe.NoShape

        self.setShape(Tetrominoe.NoShape)
        

    def shape(self):
        '''returns shape'''
        
        return self.pieceShape
        

    def setShape(self, shape):
        '''sets a shape'''
        
        table = Shape.coordsTable[shape]
        
        for i in range(4):
            for j in range(2):
                self.coords[i][j] = table[i][j]

        self.pieceShape = shape
        

    def setRandomShape(self):
        '''chooses a random shape'''
        
        self.setShape(random.randint(1, 7))
       

        
    def x(self, index):
        '''returns x coordinate'''
        
        return self.coords[index][0]

        
    def y(self, index):
        '''returns y coordinate'''
        
        return self.coords[index][1]

        
    def setX(self, index, x):
        '''sets x coordinate'''
        
        self.coords[index][0] = x

        
    def setY(self, index, y):
        '''sets y coordinate'''
        
        self.coords[index][1] = y

        
    def minX(self):
        '''returns min x value'''
        
        m = self.coords[0][0]
        for i in range(4):
            m = min(m, self.coords[i][0])

        return m

        
    def maxX(self):
        '''returns max x value'''
        
        m = self.coords[0][0]
        for i in range(4):
            m = max(m, self.coords[i][0])

        return m

        
    def minY(self):
        '''returns min y value'''
        
        m = self.coords[0][1]
        for i in range(4):
            m = min(m, self.coords[i][1])

        return m

        
    def maxY(self):
        '''returns max y value'''
        
        m = self.coords[0][1]
        for i in range(4):
            m = max(m, self.coords[i][1])

        return m

        
    def rotateLeft(self):
        '''rotates shape to the left'''
        
        if self.pieceShape == Tetrominoe.SquareShape:
            return self

        result = Shape()
        result.pieceShape = self.pieceShape
        
        for i in range(4):            
            result.setX(i, self.y(i))
            result.setY(i, -self.x(i))

        return result

        
    def rotateRight(self):
        '''rotates shape to the right'''
        
        if self.pieceShape == Tetrominoe.SquareShape:
            return self

        result = Shape()
        result.pieceShape = self.pieceShape
        
        for i in range(4):
            
            result.setX(i, -self.y(i))
            result.setY(i, self.x(i))

        return result


if __name__ == '__main__':
    
    app = QApplication([])
    try:
        dbPath = 'tetris.sqlite'
        if not os.path.exists(dbPath):
            conn = sqlite3.connect(dbPath)
            c = conn.cursor()
            c.execute('''CREATE TABLE `t_rank_user` (
                        `_id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        `username`    TEXT NOT NULL,
                        `rank`    INTEGER NOT NULL DEFAULT 0,
                        `pwd`    TEXT NOT NULL
                    );''')
        
        
            conn.commit()
            conn.close()
        
        #users=user()
        s=Start()    
        '''if os.path.exists("credentials.txt"):
            f=open("credentials.txt")
            name=f.read()
            f.close()
            unum=users.query(name)
            if unum>0:
                print("默认登录！")
                te=Tetris()
                te.show()
            else:
                print("用户不存在！")
                os.remove("credentials.txt")   
                QMessageBox.information(register(),"警告","用户不存在，请重新注册",QMessageBox.Yes | QMessageBox.No) 
                r=register() 
        else:
            r=register()'''
    except Exception as e:  
        print(e)        
                 
        
    sys.exit(app.exec_())