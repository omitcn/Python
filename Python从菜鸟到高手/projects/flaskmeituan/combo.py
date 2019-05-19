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
from common import *
from random import *
query = Query()
db = query.conn()

@app.route('/tocombo/<shopId>/<comboId>')
def tocombo(shopId,comboId):
    return app.send_static_file('combo.htm')

@app.route('/combo',methods=['GET','POST'])
def combo():
    cursor = db.cursor()
    comboId = request.form.get('cid')
    sql = "select * from v_shop_combo where _id='%d'" % (int(comboId))
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        fields = ['_id','shop_id','combo_name','end_time','discount_cost','original_cost','combo_cover','shop_name','shop_cover','hits','address','current_cost','tel','time','sub_field_id','sub_field_name','sub_field_name','field_name']
        arr = []
        for row in results:
            time = str(row[3])
            d = dict(zip(fields,row))
            d['end_time'] = time
            arr.append(d)
        return json.dumps(arr)  
    except Exception as e:
        print(e)
    db.close();
#  获取套餐的详细内容
@app.route('/combo/content',methods=['GET','POST'])
def comboContent():
    cursor=db.cursor()
    comboId = request.form.get('cid')
    sql = "select * from t_sub_combo where combo_id = '%d'" % (int(comboId))
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        fields = ['_id','combo_id','cname','product','price','amount','total']
        arr = []
        for row in results:
            arr.append(dict(zip(fields,row)))  
        return json.dumps(arr)        
    except Exception as e:
        print(e)
    db.close()        
    
# 获取店铺的推荐信息
@app.route('/combo/recommend',methods=['GET','POST'])
def recommend():
    cursor = db.cursor()
    shopId = request.form.get('sid')
    sql= "select * from v_shop_pic where type=2 and shop_id='%d'" % int(shopId)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        fields = ['_id','shop_id','pic_url','type','shop_name']
        arr = []
        for row in results:
            arr.append(dict(zip(fields,row)))  
        return json.dumps(arr)          
    except Exception as e:
        print(e)
@app.route('/combo/shoppic',methods=['GET','POST'])
def shoppic():
    cursor = db.cursor()
    shopId = request.form.get('sid')
    sql = "select * from v_shop_pic where type=1 and shop_id='%d'" % int(shopId)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        fields = ['_id','shop_id','pic_url','type','shop_name']
        arr = []
        for row in results:
            arr.append(dict(zip(fields,row)))  
        return json.dumps(arr)          
    except Exception as e:
        print(e)
        