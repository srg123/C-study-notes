
print("Hello, Python!")
# 注意：在Python中，代码块是通过缩进来表示的，而不是使用大括号 {}。通常建议使用4个空格进行缩进。
# 所有代码中的标点符号必须是‌英文半角符号

# 1、变量和基础数据类型
# 四种基础变量类型
name = "小明"       # 字符串(str)，用引号包裹
age = 22           # 整数(int)
height = 1.75      # 浮点数(float)
is_student = True  # 布尔值(bool)，只有True/False两个取值

# 查看变量类型
print(type(name))  # 输出 <class 'str'>
print(type(age))   # 输出 <class 'int'>
print(type(height))# 输出 <class 'float'>
print(type(is_student)) # 输出 <class 'bool'>

# 2. 常用运算符

# 算术运算符
print(10 + 3)   # 加法，输出13
print(10 % 3)   # 取模（求余数），输出1
print(2 ** 3)   # 幂运算，输出8

# 比较运算符，结果返回布尔值
print(10 > 5)   # 输出True
print(10 == 5)  # 判断相等，输出False

# 逻辑运算符
print(10 > 5 and 3 < 5)  # 输出True
print(not 10 > 5)        # 输出False

# 3. 结构语句、控制流：条件判断

score = 85
if score >= 90:
    print("成绩等级：A")
elif score >= 80:
    print("成绩等级：B")
elif score >= 60:
    print("成绩等级：C")
else:
    print("成绩等级：不及格")


# for循环‌  遍历列表和队列
fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print(f"当前水果：{fruit}")


# while循环‌：满足条件时持续执行

count = 0
while count < 5:
    print(f"当前计数：{count}")
    count += 1

# 实战练习：计算1到100的总和

total = 0
for i in range(1, 101):  # range生成1到100的连续整数
    total += i
print(f"1-100的总和是：{total}")  # 输出5050

#列表（List）
#有序可变的序列，用方括号定义，支持增删改查操作：

nums = [1, 2, 3, 4]
nums.append(5)       # 末尾追加元素，结果变为[1,2,3,4,5]
print(nums[1])       # 按索引取值，索引从0开始，输出2
nums.remove(3)       # 删除元素，结果变为[1,2,4,5]
print(nums[1:3])     # 切片操作，取索引1到3的元素，输出[2,4]

# 字典（Dict）
# 键值对形式的无序集合，用大括号定义，适合存储关联信息：
person = {
    "name": "小红",
    "age": 23,
    "city": "北京"
}
print(person["name"])       # 按键取值，输出小红
person["age"] = 24         # 修改对应的值
person["job"] = "工程师"   # 新增键值对
print(person)              # 输出整个字典

#  元组（Tuple）
# 不可变的序列，用圆括号定义，定义后无法修改元素，适合存储固定不变的数据：

colors = ("红色", "绿色", "蓝色")
print(colors[0])  # 输出红色
# 尝试修改元素会直接报错，保证数据安全

# 集合（Set）
# 无序且元素不重复的集合，最常用的功能是给列表去重：
num_list = [1, 2, 2, 3, 4, 4, 5]
unique_nums = set(num_list)  # 去重后得到{1,2,3,4,5}
set1 = {1,2,3}
set2 = {3,4,5}
print(set1 & set2)  # 求两个集合的交集，输出{3}


# 定义和调用函数
# 使用def关键字定义函数，支持传入参数和返回结果：

# 定义一个计算圆面积的函数
def calc_circle_area(radius):
    """根据半径计算圆的面积"""
    pi = 3.14
    area = pi * radius ** 2
    return area

# 调用函数
result = calc_circle_area(5)
print(f"半径5的圆面积是：{result:.2f}")  # 输出78.50


# 导入标准库
# Python自带大量开箱即用的标准库，无需额外安装，直接导入即可使用：

import math
print(math.sqrt(16))  # 调用math库的开平方函数，输出4.0

import random
print(random.randint(1, 10))  # 生成1-10之间的随机整数


# 安装第三方库
# 通过pip命令可以安装社区提供的海量第三方库，比如数据分析、爬虫相关工具

# 安装常用的网络请求库requests
# pip install requests  
# 安装数据分析库pandas
# pip install pandas



# 查看安装包信息python3 -m pip show 包名
# 查看当前环境所有包安装信息python3 -m pip list -v 
# 查看当前python环境的site-packages根目录命令行python3 -m site 


