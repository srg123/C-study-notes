# Python 测试

[单元测试]
[测试工具]
[代码体检工具]


#### 单元测试概念

**把你写的代码切成一小块一小块，单独拿出来检验，看看这一小块能不能正常干活，这里的 “单元”，一般就是一个函数、一个类里面的某个方法**.

 - 断言 `assert`
 - - 写了一个函数 `def get_img_size(img_path)`，输入图片路径，返回图片宽高。
 - - 单元测试就写：给这个函数传入已知图片，断言返回的宽高等于预期值。

```python

def add(a,b):
    """
    求和
    >>> add(2,3)
    5
    >>> add(-1,1)
    0
    """
    return a+b

# 运行：python -m doctest xxx.py

```
#### 测试工具

 - doctest:直接把样例写在函数的文档字符串里,就是函数说明文档中，写上调用示例和预期输出。运行 doctest，它自动提取文档里的例子，执行比对结果。
 - unittest:专门写测试用例的框架。
 - - 写一个测试类，继承 `unittest.TestCase`
 - - 每个测试函数名字必须以 `test` 开头，框架会自动执行这些 test 函数
 - - 使用自带断言方法：`self.assertEqual(实际结果,预期结果)`

```python

import unittest

# 待测试的函数，模拟CV里图片裁剪函数
def crop_img(w, h):
    return w//2, h//2

# 测试类
class TestImgFunc(unittest.TestCase):
    # 测试函数，名字必须test开头
    def test_crop_size(self):
        # 预期输入600,400，裁剪后应该是300,200
        res_w, res_h = crop_img(600,400)
        # 断言：实际结果和预期相等，不相等就测试失败
        self.assertEqual(res_w, 300)
        self.assertEqual(res_h, 200)

if __name__ == "__main__":
    # 执行所有test开头的测试方法
    unittest.main()


```


#### 代码体检工具
**PyChecker,python2有用** 
**Pylint**
<!-- 检查范围 -->
- 调用函数传参数量不对
- 变量还没赋值就直接使用
- 调用不存在的类属性、方法
- import 导入了模块但是模块不存在
- 定义了变量，全程没使用（多余变量）
- 
- 检查代码是否遵守 Python 编码规范 PEP8：变量命名、一行代码不能写太长、缩进
- 检查函数 / 类缺少文档注释
- 提示代码写得太复杂，建议重构
- 输出报告，给代码打分（满分 10 分）

```python

# 安装
pip install pylint
# 在命令行检测你的代码文件
pylint test_cv_code.py

```

### 单元测试流程

1. 写业务代码（比如图像处理函数）
2. 单独写测试代码：给输入，写好预期输出
3. 执行测试脚本
4. 全部通过 = 没问题；失败，定位这个函数哪里出问题


### 总结

 - 单元测试：**写代码去自动测试代码**，用来保证修改代码的时候，老功能不会被改坏。
 - doctest：文档里附带测试；unittest：正式、结构化的测试框架，Python 自带。
 - **pyChecker/Pylint（静态检查）**：**不跑程序**，只读源码，提前发现低级错误。相当于看文字草稿找错别字。
 - **unittest/doctest 单元测试**：**运行代码**，验证函数输出结果对不对。相当于做一遍试卷，核对答案


