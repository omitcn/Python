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
       age            INT     NOT NULL)''')


    conn.commit()
    conn.close()
conn = sqlite3.connect(dbPath)
c = conn.cursor()
while True:
    id = input('请输入id：')
    if id == 'exit:':
        break;
    id = int(id)
    name = input('请输入name：')
    if name == 'exit:':
        break;
    age = input('请输入age：')
    if age == 'exit:':
        break;   
    age = int(age) 
    c.execute("INSERT INTO persons (id,name,age) \
          VALUES ({},'{}',{})".format(id,name,age));

conn.commit()


persons = c.execute("select id,name,age from persons order by age")

result = []
for person in persons:
    value = {}
    value['id'] = person[0]
    value['name'] = person[0]
    value['age'] = person[1]  
    result.append(value)
conn.close() 

print(result)




