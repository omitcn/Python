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
#coding=utf-8
from common import  *
from pymysql import *
import json

connmysql=Query()
db=connmysql.conn()

@app.route("/toaccount")
def toaccount():
    return app.send_static_file('account.htm')

@app.route('/account',methods=['GET','POST'])
def account():
    cursor=db.cursor()
    id=session['userid']
    sql="select * from t_users where _id=%d" %(id)
    print(sql)
    try:   
        cursor.execute(sql)
        results=cursor.fetchall()
        fields=['_id','tel_number','nickname','password','user_pic']
        arr=[]
        for row in results:
            arr.append(dict(zip(fields,row)))
        print(arr)
        return json.dumps(arr)
        
    except Exception as e:
        print(e)
        return "123"
    db.close()

@app.route('/account/nickname',methods=['GET','POST'])
def nickname():
    cursor=db.cursor()
    id=session['userid']
    nick=request.form.get('username')
    sql="update t_users set nickname='%s' where _id='%d'" %(nick,id)
    print(nick)
    try:   
        cursor.execute(sql)
        session['nickname'] = nick
        return "1"
        
    except Exception as e:
        print(e)
        return "123"
    db.close()

@app.route('/account/password',methods=['GET','POST'])
def password():
    cursor=db.cursor()
    id=session['userid']
    pwd=request.form.get('password')
    sql="update t_users set password='%s' where _id='%d'" %(pwd,id)
    print(sql)
    try:   
        cursor.execute(sql)
        
        return "1"
        
    except Exception as e:
        print(e)
        return "123"
    db.close()















