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
x = 0
while x < 100:
    if x == 5:
        break;
    print(x, end=" ") 
    x += 1
names = ["Bill", "Mike", "Mary"]
print("\nbreak语句在for循环中的应用")
for name in names:
    if not name.startswith("B"):
        break;
    print(name)

print("break语句在for循环中的应用")
for name in names:
    if name.startswith("B"):
        continue;
    print(name, end=" ")

print("\n嵌套循环")
arr1 = [1,2,3,4,5]
arr2 = ["Bill", "Mary", "John"]
arr = [arr1, arr2]
i = 0;
while i < len(arr):
    for value in arr[i]:
        print(value, end = " ")
    i += 1
    print()
        