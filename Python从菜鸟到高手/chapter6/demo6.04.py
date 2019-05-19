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
dict = {"name":"Bill", "age":34, "sex":"男", "salary":"3456"}

# 遍历key
for key in dict:
    print(key, "=", dict[key], end = " ")

print()
# 遍历key和value
for key,value in dict.items():
    print(key, "=", value, end = " ")
print();
# 并行迭代
list1 = [1,2,3,4,5]
list2 = ["a", "b", "c", "d", "e"]
for i  in range(len(list1)):
    print("list1[" + str(i) + "]", "=", list1[i], "list2[" +str(i) + "]" ,"=", list2[i],end=" ")
    
print();
# 压缩
for value in zip(list1, list2):
     print(value, end = " ")
print()
list3 = ['x', 'y']
for value in zip(list2, list3):
    print(value, end = " ")
    
#  反转排序迭代
print()
values1 = [4,1,3,6,5,2,8]
print(sorted(values1))

values2 = reversed(values1)
for v in values2:
    print(v, end=" ")
print()

print(''.join(list(reversed("hello world"))))


