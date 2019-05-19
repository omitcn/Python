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
from django.shortcuts import render
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django import forms
import pymysql
import json
import hashlib
def assocArr(str,par):
	# python查询出来是索引数组(下标1 2 3) 转为关联数组
	# 参数 (查询出来的json字符串 , 理想的下标)
	results=json.loads(str)
	arr=[]
	for row in results:
		arr.append(dict(zip(par,row)))
	return arr
def md5(str):
	# md5加密
    import hashlib
    m = hashlib.md5()   
    m.update(str)
    return m.hexdigest()
def mysqlConnect(sql):
	# 数据库访问
    db = pymysql.connect("localhost","root","12345678","58",charset='utf8')
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    data = json.dumps(data)
    db.commit()
    db.close()
    return data

def hello(request):
	# 测试函数
    return HttpResponse("Hello world !1111 ")


# 403解决方法
@csrf_exempt
def register(request):
	# 注册
	if request.method == "GET":
		return render(request, 'register.html')
	else:
		u=request.POST.get('username')
		p=request.POST.get('password')
		sql='select * from users where username="'+u+'"'
		res=mysqlConnect(sql)
		if res!="[]":
			# 存在用户名
			return HttpResponse('isset')
		else:
			# md5(p.encode("utf-8")) 加密之前 一定要转码
			sql2='insert into users(username,password) values("'+u+'","'+md5(p.encode("utf-8"))+'")'
			mysqlConnect(sql2)
			# session 不好用 一般情况为setting文件问题
			# 或者出现 no such table: django_session 错误提示 
			# 解决方法 : 可以通过控制台(cmd)进入到项目根目录 即manage.py文件所在的文件夹
			# 1.9之后的执行'python manage.py migrate'命令(我用的这个命令)，
    		# 1.9之前的执行'python manage.py syscdb'命令(baidu的时候看到的，自己没有用过)
			request.session['username'] = u
			return HttpResponse('success')
			
@csrf_exempt
def login(request):
	# 登录
	if request.method == "GET":
		return render(request, 'login.html')
	else:
		u=request.POST.get('username')
		p=request.POST.get('password')
		sql='select * from users where username="'+u+'" and password="'+md5(p.encode("utf-8"))+'"'
		res=mysqlConnect(sql)
		if res=="[]":
			return HttpResponse('defeat')
		else:
			request.session['username'] = u
			return HttpResponse('success')
def logout(request):
	# 注销
	del request.session['username']  
	return HttpResponseRedirect('/index')       
def index(request):
	# 首页
    context = {}
    context['index_list']=mysqlConnect('select * from index_list order by value')
    context['username']=request.session.get('username')
    # return HttpResponseRedirect('/index')
    return render(request, 'index.html', context)

def recruitment(request):
	# 招聘首页
	context = {}
	context['username']=request.session.get('username')
	typeStr=mysqlConnect('select * from rec_type order by value')
	# type=json.loads(typestr)
	par=['id','name','hot','value']
	type=assocArr(typeStr,par)
	context['type']=type
	return render(request, 'recruitment.html', context)

def recList(request):
	# 招聘列表
	context = {}
	context['username']=request.session.get('username')
	# 获取当前筛选条件信息
	# 福利
	if request.GET.get('wid'):
		context['welfareInfo']=assocArr(mysqlConnect('select * from welfare where id='+str(request.GET.get('wid'))),['id','name'])[0]
	# 分类
	context['typeInfo']=assocArr(mysqlConnect('select * from rec_type where id='+str(request.GET.get('type'))),['id','name','hot','value'])[0]
	# 获取分类
	typeStr=mysqlConnect('select * from rec_type order by value')
	typePar=['id','name','hot','value']
	context['type']=assocArr(typeStr,typePar)


	# 获取福利筛选------------------------------------------------------------------
	welfareStr=mysqlConnect('select * from welfare')
	welPar=['id','name']
	context['welfareList']=assocArr(welfareStr,welPar)
	

	# 获取招聘信息------------------------------------------------------------------
	typeId=request.GET.get('type')
	
	if request.GET.get('wid'):
		# 福利选项id
		sql="select * from v_all_rec_list where type="+str(typeId) + " and wid="+str(request.GET.get('wid'))
	else:
		sql="select * from v_rec_list where type="+ str(typeId)
	# context['sql']=sql
	recListStr=mysqlConnect(sql)
	recPar=['id','type','company_id','money','title','job_name','edu','exp','cname','wid_list','mname_list']
	recList=assocArr(recListStr,recPar)
	resRecList=[]
	# 分割出福利
	for row in recList:
		row['mname_list']=row['mname_list'].split(',')
		row['wid_list']=row['wid_list'].split(',')
		resRecList.append(row)
	context['recList']=resRecList
	return render(request, 'recList.html', context)


@csrf_exempt
# ajax访问一定要带这句话
def apply(request):
	# 申请
	res=mysqlConnect('select * from apply where username="'+request.session.get('username')+'" and rec_id='+request.POST.get('rid'))
	# return HttpResponse(res)
	if res!="[]":
		# 已申请过
		return HttpResponse('isset')
	else:
		mysqlConnect('insert into apply(rec_id,username) values("'+request.POST.get('rid')+'","'+request.session.get('username')+'")')
		return HttpResponse('success')

def recDetails(request):
	# 招聘详情
	id=request.GET.get('id')
	recInfo=assocArr(mysqlConnect('select * from v_rec_list where id='+str(id)),['id','type','company_id','money','title','job_name','edu','exp','cname','wid_list','mname_list'])[0]
	context = {}
	context['username']=request.session.get('username')
	recInfo['mname_list']=recInfo['mname_list'].split(',')
	recInfo['wid_list']=recInfo['wid_list'].split(',')
	context['recInfo']=recInfo
	return render(request, 'recDetails.html', context)

def carList(request):
	# 汽车列表
	context = {}
	context['username']=request.session.get('username')
	return render(request, 'carList.html', context)

@csrf_exempt
def carAjaxInfo(request):
	# 汽车部分 Vue异步获取新信息接口
	requesType=request.GET.get('type')

	if requesType=='carBrand':
		# 获取品牌
		carBrand=assocArr(mysqlConnect('select * from car_brand'),['id','name'])
		return HttpResponse(json.dumps(carBrand))
	elif requesType=='carType':
		# 获取类型 轿车 suv....
		carType=assocArr(mysqlConnect('select * from car_type'),['id','name'])
		return HttpResponse(json.dumps(carType))
	else :
		# 二手车信息列表
		if request.GET.get('tid') and request.GET.get('bid'):
			sql="select * from car where type_id="+request.GET.get('tid')+" and brand_id="+request.GET.get('bid')
		elif not request.GET.get('tid') and request.GET.get('bid'):
			sql="select * from car where brand_id="+request.GET.get('bid')
		elif request.GET.get('tid') and not request.GET.get('bid'):
			sql="select * from car where type_id="+request.GET.get('tid')
		else :
			sql="select * from car"

		carList=assocArr(mysqlConnect(sql),['id','type_id','brand_id','title','rush','time','journey','cc','gear','price','hy','img'])
		return HttpResponse(json.dumps(carList))
