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

@app.route("/totrade")
def tra():
    return app.send_static_file('trade.htm')

@app.route('/trade',methods=['GET','POST'])
def trade():
    cursor=db.cursor()
    id=session['userid']
    sql="select * from v_shop_combo_trade where user_id=%d" %(id)
    print(sql)
    try:   
        cursor.execute(sql)
        results=cursor.fetchall()
        par=['_id','trasaction_id','combo_id','product_name','amount','user_id','start_time','end_time','yn','total','discount_cost','original_cost','combo_cover','shop_name','shop_id','shop_cover']
        arr=[]
        for row in results:
            arr.append(dict(zip(par,row)))
        return json.dumps(arr)
        
    except Exception as e:
        print(e)
        return "123"
    db.close()

@app.route('/trade/paid',methods=['GET','POST'])
def paid():
    cursor=db.cursor()
    id=session['userid']
    sql="select * from v_shop_combo_trade where yn=1 and user_id=%d" %(id)
    print(sql)
    try:   
        cursor.execute(sql)
        results=cursor.fetchall()
        par=['_id','trasaction_id','combo_id','product_name','amount','user_id','start_time','end_time','yn','total','discount_cost','original_cost','combo_cover','shop_name','shop_id','shop_cover']
        arr=[]
        for row in results:
            arr.append(dict(zip(par,row)))
        return json.dumps(arr)
        
    except Exception as e:
        print(e)
        return "123"
    db.close()
    
@app.route('/trade/non-payment',methods=['GET','POST'])
def nopayment():
    cursor=db.cursor()
    id=session['userid']
    sql="select * from v_shop_combo_trade where yn=0 and user_id=%d" %(id)
    print(sql)
    try:   
        cursor.execute(sql)
        results=cursor.fetchall()
        par=['_id','trasaction_id','combo_id','product_name','amount','user_id','start_time','end_time','yn','total','discount_cost','original_cost','combo_cover','shop_name','shop_id','shop_cover']
        arr=[]
        for row in results:
            arr.append(dict(zip(par,row)))
        return json.dumps(arr)
        
    except Exception as e:
        print(e)
        return "123"
    db.close()
    

@app.route("/totinfo/<tid>")
def toinfo(tid):
    return app.send_static_file('trade_info.htm')
    

@app.route('/tradeinfo',methods=['GET','POST'])
def tinfo():
    cursor=db.cursor()
    tid=request.form.get('tid')
    id=session['userid']
    sql="select * from v_shop_combo_trade where trasaction_id=%s and user_id=%d" %(tid,id)
    print(sql)
    try:   
        cursor.execute(sql)
        results=cursor.fetchall()
        par=['_id','trasaction_id','combo_id','product_name','amount','user_id','start_time','end_time','yn','total','discount_cost','original_cost','combo_cover','shop_name','shop_id','shop_cover']
        arr=[]
        for row in results:
            arr.append(dict(zip(par,row)))
        return json.dumps(arr)
        
    except Exception as e:
        print(e)
        return "123"
    db.close()  