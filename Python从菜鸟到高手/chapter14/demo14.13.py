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
from pymongo import *
Client = MongoClient()
db = Client.data
# db = Client['data']


#collection = db['test_collection']

# 插入数据
person1 = {"name": "Bill", "age": 55, "address": "地球", "salary": 1234.0}
person2 = {"name": "Mike", "age": 12, "address": "火星", "salary": 434.0}
person3 = {"name": "John", "age": 43, "address": "月球", "salary": 6543.0}
persons = db.persons  

persons.delete_many({'age':{'$gt':0}})


personId1 = persons.insert_one(person1).inserted_id
personId2 = persons.insert_one(person2).inserted_id
personId3 = persons.insert_one(person3).inserted_id
print(personId3)
'''
和上面的不能同时使用
personList = [person1,person2,person3]
result = persons.insert_many(personList)
print(result.inserted_ids)
'''

print(persons.find_one())
print(persons.find_one()['name'])
# 搜索所有数据
for person in persons.find():
    print(person)
print('--------------')
persons.update_one({'age':{'$lt':50}},{'$set':{'name':'超人'}})  # update_many更新所有满足条件的文档
#persons.delete_one({'age':{'$gt':0}})  # 只删除满足条件的第1个文档
# 搜索指定数据
for person in persons.find({'age':{'$lt':50}}):
    print(person)
    
print('--------------')
# 更新

for person in persons.find({'age':{'$gt':50}}):
    print(person)
print('总数', '=', persons.count())
