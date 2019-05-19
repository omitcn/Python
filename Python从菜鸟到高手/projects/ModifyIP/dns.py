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
#coding:utf-8
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication,QLineEdit,QLabel,QPushButton
from PyQt5.QtCore import QTimer
from aliyunsdkcore import client
from aliyunsdkalidns.request.v20150109 import DescribeDomainsRequest,DescribeDomainRecordsRequest,UpdateDomainRecordRequest
import json,urllib,re
from urllib3 import *
from asyncio.tasks import sleep
import time

class ModifyIP(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):         
        self.lb=QLabel(self)
        self.lb.setText('当前IP')
        self.lb.move(50,22) 
        #获取当前ip  
        ip=getLocalIP()    
        self.le = QLineEdit(self)
        self.le.setText(ip)
        self.le.resize(150,22)
        self.le.move(130, 26)
        #设置时间
        self.lbs=QLabel(self)
        self.lbs.setText('更新时间')
        self.lbs.move(50,52) 
        #获取当前ip  
        self.les = QLineEdit(self)
        self.les.setText('10')
        self.les.resize(150,22)
        self.les.move(130, 56)
        #提交按钮
        qbtn = QPushButton('执行', self)
        
        qbtn.clicked.connect(self.start)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(150, 90)       
        #主体
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('获取当前ip')    
        self.show()
    def start(self):
        a=self.gettext()
        t=int(a)*1000
        self.timer=QTimer(self)
        self.timer.timeout.connect(self.setip)
        self.timer.start(t)
     
    def gettext(self):
        a=self.les.text()
        return a   
        
    def setip(self):    
        ip=getLocalIP()
        self.le.setText(ip)
        updateIp()    

http = PoolManager()
#替换以下参数
ID="LTxI55ycy4l6jmFxc4"
Secret="P4Pwa3cox3QsrixfS543a4fruQPKq35wC942"
RegionId="cn-hangzhou"
DomainName="geekori.com"
#想要自动修改的主机名和域名类型
HostNameList = ['www','@']
Types = "A"

clt = client.AcsClient(ID,Secret,RegionId)

#获取公网ip
def getLocalIP():
    IPInfo = http.request('get',"http://ip.chinaz.com/getip.aspx")
    IPInfo=IPInfo.data.decode('utf-8')
    IPInfo=IPInfo.replace('b','')
    IPInfo=IPInfo.replace('ip','"ip"')
    IPInfo=IPInfo.replace('address','"address"')
    IPInfo=eval(IPInfo)
    IP = IPInfo['ip']
    return IP

#获取域名列表（暂时无用）
def getDomainList():
    DomainList = DescribeDomainsRequest.DescribeDomainsRequest()
    DomainList.set_accept_format('json')
    DNSListJson = json.loads(clt.do_action_with_exception(DomainList))
    print (DNSListJson)

#更新域名ip
def editDomainRecord(HostName, RecordId, Types, IP):
    try:
        updateDomainRecord = updateDomainRecordRequest.updateDomainRecordRequest()
        updateDomainRecord.set_accept_format('json')
        updateDomainRecord.set_RecordId(RecordId)
        updateDomainRecord.set_RR(HostName)
        updateDomainRecord.set_Type(Types)
        updateDomainRecord.set_TTL('600')
        updateDomainRecord.set_Value(IP)
        updateDomainRecordJson = json.loads(clt.do_action_with_exception(updateDomainRecord))

    except Exception as e:
        return e   

#获取域名信息
def getAllDomainRecords(DomainName, Types, IP):
    DomainRecords = DescribeDomainRecordsRequest.DescribeDomainRecordsRequest()
    DomainRecords.set_accept_format('json')
    DomainRecords.set_DomainName(DomainName)
    DomainRecordsJson = json.loads(clt.do_action_with_exception(DomainRecords))
    for HostName in HostNameList:
        for x in DomainRecordsJson['DomainRecords']['Record']:
            RR = x['RR']
            Type = x['Type']
            if RR == HostName and Type == Types:
                RecordId = x['RecordId']
                print (RecordId)
                editDomainRecord(HostName, RecordId, Types, IP)

def updateIp():
    IP = getLocalIP()
    #getDomainList()
    getAllDomainRecords(DomainName, Types, IP)
    
        

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ModifyIP()
    sys.exit(app.exec_())

