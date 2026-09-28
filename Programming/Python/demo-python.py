

# python实战小项目

# 项目1：简易计算器---------------------------


def simple_calculator():
    op = input("请选择运算(+ - * /): ")
    num1 = float(input("请输入第一个数字: "))
    num2 = float(input("请输入第二个数字: "))
    
    if op == '+':
        print(f"计算结果：{num1 + num2}")
    elif op == '-':
        print(f"计算结果：{num1 - num2}")
    elif op == '*':
        print(f"计算结果：{num1 * num2}")
    elif op == '/':
        if num2 != 0:
            print(f"计算结果：{num1 / num2}")
        else:
            print("错误：除数不能为0")
    else:
        print("不支持的运算符号")

# 运行计算器
simple_calculator()



# 文件批量重命名---------------------------
# 可以快速给指定文件夹下的所有图片批量添加统一前缀，解决日常办公的重复劳动


import os

# 指定要处理的文件夹路径
# folder_path = "./images"
# prefix = "旅行照片_"

# # 遍历文件夹内所有文件
# for index, filename in enumerate(os.listdir(folder_path)):
#     # 分离文件名和后缀
#     name, suffix = os.path.splitext(filename)
#     # 拼接新文件名
#     new_name = f"{prefix}{index+1}{suffix}"
#     # 执行重命名
#     os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))
