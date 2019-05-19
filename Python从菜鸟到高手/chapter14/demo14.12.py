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
from sqlobject import *
from sqlobject.mysql import builder
import json
mysql = 'mysql://root:12345678@localhost:3306/meituan?charset=utf8'
sqlhub.processConnection = connectionForURI(mysql,driver='pymysql')


class Person(SQLObject):
    class sqlmeta:
        table='t_persons'
    name = StringCol(length=30)
    age = IntCol()
    address = StringCol(length=30)
    salary = FloatCol()
try:    
    Person.dropTable()
except:
    pass
Person.createTable()
print('成功创建了Persons表')
person1 = Person(name='Bill', age=55,address='地球',salary=1234)
person2 = Person(name='Mike', age=65,address='月球',salary=4321)
person3 = Person(name='John', age=15,address='火星',salary=4000)
print('成功插入了3条记录')

# 修改表数据
person2.name = "李宁"
person2.address= "赛博坦"

# 查询表数据
persons = Person.selectBy(name='Bill')
print(persons[0])
print(persons[0].id) 
print(persons[0].name) 
print(persons[0].address)

def person2Dict(obj):
    return {
        'id': obj.id,
        'name': obj.name,
        'age': obj.age,
        'address':obj.address,
        'salary':obj.salary
    }

jsonStr = json.dumps(persons[0], default=person2Dict,ensure_ascii=False)
print(jsonStr)

# 删除表数据
persons[0].destroySelf()
