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
import sqlite3
import os

dbPath = 'data.sqlite'
if not os.path.exists(dbPath):
    conn = sqlite3.connect(dbPath)
    c = conn.cursor()
    c.execute('''CREATE TABLE persons
       (id INT PRIMARY KEY     NOT NULL,
       name           TEXT    NOT NULL,
       age            INT     NOT NULL,
       address        CHAR(50),
       salary         REAL);''')


    conn.commit()
    conn.close()
    print('创建数据成功')



conn = sqlite3.connect(dbPath)
c = conn.cursor()
c.execute('delete from persons')
c.execute("INSERT INTO persons (id,name,age,address,salary) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");
c.execute("INSERT INTO persons (id,name,age,address,salary) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

c.execute("INSERT INTO persons (id,name,age,address,salary) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

c.execute("INSERT INTO persons (id,name,age,address,salary) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");    
conn.commit()

print('插入数据成功')

persons = c.execute("select name,age,address,salary from persons order by age")
print(type(persons))
result = []
for person in persons:
    value = {}
    value['name'] = person[0]
    value['age'] = person[1]
    value['address'] = person[2]
    result.append(value)
conn.close() 
print(type(result))
print(result)

import json
resultStr = json.dumps(result)
print(type(resultStr))
print(resultStr)


