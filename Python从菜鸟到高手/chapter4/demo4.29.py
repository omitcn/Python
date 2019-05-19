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
print("----测试append方法-----")
numbers = [1,2,3,4]
numbers.append(5)                    # 将5添加到numbers列表的最后
print(numbers)                        # 运行结果：[1, 2, 3, 4, 5]
numbers.append([6,7])                # 将列表[6,7]作为一个值添加到numbers列表后面
print(numbers)                        # [1, 2, 3, 4, 5, [6, 7]]

print("----测试clear方法-----")
names = ["Bill","Mary", "Jack"]
print(names)
names.clear();                        # 清空names列表
print(names)                # 运行结果：[]

print("----测试copy方法-----")
a = [1,2,3]
b = a                            # a和b指向了同一个列表
b[1] = 30                           # 修改列表b的元素值，a列表中对应的元素值也会改变
print(a)                        # 运行结果：[1, 30, 3]

aa = [1,2,3]
bb = aa.copy()                    # bb是aa的副本
bb[1] = 30                        # 修改bb中的元素值，aa中的元素值不会有任何变化
print(aa)                        # 运行结果：[1, 2, 3]

print("----测试count方法-----")
search = ["he", "new", "he", "he", "world", "peter",[1,2,3],"ok",[1,2,3]]
#  搜索“he”在search出现的次数，运行结果：3
print(search.count("he"))
#  搜索[1,2,3]在search出现的次数，运行结果：2
print(search.count([1,2,3]))

print("----测试extend方法-----")
a = [1,2,3]
b = [4,5,6]
a.extend(b)                     #  将b列表接在a列表的后面，extend方法并不返回值
print(a)                        #  运行结果：[1, 2, 3, 4, 5, 6]

# 如果使用列表连接操作，效率会更低，并不建议使用
a = [1,2,3]
b = [4,5,6]
print(a + b)                    #  运行结果：[1, 2, 3, 4, 5, 6]

# 可以使用分片赋值的方法实现同样的效果
a = [1,2,3]
b = [4,5,6]
a[len(a):] = b
print(a)                        #  运行结果：[1, 2, 3, 4, 5, 6]        

print("----测试index方法-----")
s = ["I", "love", "python"];
print(s.index("python"))        #  查询”python”的索引位置，运行结果：2
print("xyz在列表中不存在，所以搜索是会抛出异常.")
#str.index("xyz")               # 会抛出异常，因为”xyz”在s列表中不存在
  
print("----测试insert方法-----")
numbers = [1,2,3,4,5]            
numbers.insert(3,"four")        # 在numbers列表的第4个元素的位置插入一个”four”
print(numbers)                        #  运行结果：[1, 2, 3, 'four', 4, 5]
#  可以使用分片赋值实现同样的效果
numbers = [1,2,3,4,5]
numbers[3:3] = ['four']                #  使用分片赋值在列表中插入另一个列表
print(numbers)                        #  运行结果：[1, 2, 3, 'four', 4, 5]

print("----测试pop方法-----")
numbers = [1,2,3]
#  pop方法返回删除的元素值
print(numbers.pop())                #  删除numbers列表中的最后一个元素值，运行结果：3
print(numbers.pop(0))                #  删除numbers列表中的第1个元素值，运行结果：1
print(numbers)                        #  运行结果：[2]

print("----测试remove方法-----")
words = ["he", "new", "he", "yes", "bike"]
words.remove("he")                    #  删除words列表中的第1个”he”
print(words)                        #  运行结果：['new', 'he', 'yes', 'bike']
# words.remove("ok")                # 删除不存在的列表元素，会抛出异常

print("----测试reverse方法-----")
numbers = [1,2,3,4,5,6]
numbers.reverse()                    #  将numbers列表中的元素值倒序摆放
print(numbers)                        #  运行结果：[6, 5, 4, 3, 2, 1]

print("----测试sort方法-----")
numbers = [5,4,1,7,4,2]                
numbers.sort()                       # 对numbers列表中的元素值按升序排序（默认）
print(numbers)                        # 运行结果：[1, 2, 4, 4, 5, 7]

values = [6,5,2,7,"aa","bb","cc"]
# 待排序列表的元素类型必须是可比较的，字符串和数值类型不能直接比较，否则会抛出异常
# values.sort()                      #  抛出异常

# 使用sort方法排序，会直接修改原列表，如果要想对列表的副本进行排序，可以使用下面的代码
# 方法1：使用分片操作
x = [5,4,1,8,6]
y = x[:]
y.sort();                           # 对列表的副本进行排序
print(x)                            # 运行结果：[5, 4, 1, 8, 6]
print(y)                                # 运行结果：[1, 4, 5, 6, 8]

# 方法2：使用sorted函数
x = [7,6,4,8,5]
y = sorted(x)                       #  对x的副本进行排序
print(x)                            #  运行结果：[7, 6, 4, 8, 5]
print(y)                    # 运行结果：[4, 5, 6, 7, 8]

# sorted函数可以对任何序列进行排序，例如对字符串进行排序
print(sorted("geekori"))    # 运行结果：['e', 'e', 'g', 'i', 'k', 'o', 'r']

x = [5,4,1,7,5]
x.sort(reverse=True)        # 对列表x中的元素值降序排列
print(x)                   # 运行结果：[7, 5, 5, 4, 1]
