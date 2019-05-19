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
from sqlalchemy import create_engine,MetaData,Table,Column,Integer,String,Float,exc,orm
from sqlalchemy.ext.declarative import declarative_base
import uuid
mysql = 'mysql+pymysql://root:12345678@localhost:3306/meituan?charset=utf8'

tableName = 'persons1'


    
engine = create_engine(mysql,encoding='utf-8')
metadata = MetaData(engine)    
person = Table(tableName, metadata,
    Column('id', Integer, primary_key = True),
    Column('name', String(30)),
    Column('age', Integer),
    Column('address', String(100)),
    Column('salary', Float))

engine.connect()

metadata.create_all(engine)

Base = declarative_base()
class Person(Base):
    __tablename__= tableName
    id  = Column(Integer,primary_key=True)
    name = Column(String(30))
    age = Column(Integer)
    address = Column(String(100))
    salary= Column(Float)
    

Session = orm.sessionmaker(bind=engine)
session = Session()

session.query(Person).delete()
session.commit()
person1 = Person(id=10,name='Bill',age=30,address='地球',salary=1234)
person2 = Person(id=20,name='Mike',age=40,address='火星',salary=4321)
person3 = Person(id=30,name='John',age=50,address='氪星',salary=10000)

session.add(person1)
session.add(person2)
session.add(person3)
# 提交即保存到数据库:
session.commit()
print('成功插入记录')

session.query(Person).filter(Person.name == 'Mike').update({'address': '千星之城'})
query = session.query(Person).filter(Person.name == 'John')
print(query)
person = query.scalar()
person.age = 12
person.salary=5432
session.commit()
print('成功更新了记录')
persons = session.query(Person).filter((Person.age >= 10) & (Person.salary >= 2000))
for person in persons:
    print('name','=',person.name,end=' ')
    print('age','=',person.age, end = ' ')
    print('salary','=',person.salary) 

print(persons.first().name)
print(persons.offset(1).scalar().name)  # 剩下最后一行时



# 关闭session:
session.close()
    