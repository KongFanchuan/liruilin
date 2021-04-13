# """
# print('你好')
# print(1+2)
# print(100*100)
# print(1+2+3)  
# print('哈'*100)
# print("ha"*100)
# """
# a = input("请输入：")
# b = input("请输入：")
# print("获取的内容:",a+b)
# print("字符长度是:",len(a+b))

# a =[1,2,3,"haha","xixi",True ,False]
# print(a)
# print(a[4])
# 切片
# print(a[0:4]) #左闭右开
# print(a[4:6])
# print(a[6:7])
# a.append("append1")
# a.append("append2")
# print(a)
# a.insert(0,"insert") # 在指定位置插入数据
# print(a)
# b = a.pop(5) # 剪切
# print(a)
# print(b)

# print(a.index("haha"))
# print(a.count("haha"))
# b = (a,"空","帆","船")
# print(b[0][3])

# a.clear(a)
# print(a)
# 
# 
"""
所有的方法都是小括号结尾，比如，print(),input(),len()
元组、数组、字典的取值，都是用中括号，比如a[0]
元组、数组、字典的定义，分别是(),[],{}
"""

# 字典
# 字典的特点：没有顺序
# 字典结构必须是 键值对 的结构。key:value
# 


name= input("请输入姓名:")
age= input("输入年龄:")
sex= input("输入性别:")
userinfo= {}
userinfo.update(name = name,sex = sex,age = age)
 # 取值
print(userinfo)
# 新增
# a["name"] = "李四"
# 修改
# print(a)


