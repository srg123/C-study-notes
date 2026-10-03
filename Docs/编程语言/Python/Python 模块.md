# Python 模块

[模块]
[包]
[模块搜索路径]



#### 模块

**一个 `.py` 文件，就是一个模块；模块就是装一堆函数、类、变量的文件，方便别的代码 import 拿来用**.

 - 你写 `import tool`
 - Python 去找硬盘上 `tool.py` 这个文件
 - 读取、执行里面代码
 - 在内存生成一个叫 `tool` 的模块，里面包含它定义的函数、类
之后就可以写 `tool.xxx()` 调用里面内容

```python
# img_tool.py（这是文件，import之后叫img_tool模块）
width = 640

def show_img():
    print("展示图片")

class ImageHelper:
    pass


# 外部导入：
import img_tool
img_tool.show_img()
print(img_tool.width)


```

 ####  模块搜索路径
 ** 当你写`import xxx`，Python 按顺序去一堆文件夹里找xxx.py。
这一堆文件夹地址,就是`sys.path`。
找不到就报：`ModuleNotFoundError`**

比如：
1. 先看**当前代码所在文件夹**
2. 再去 Python 安装目录自带库文件夹（math、os 就在这里）
3. 第三方库目录（OpenCV、numpy 放这里）


 ####  模块加载

  - 同一个模块，不管你 import 多少次，**只会加载执行一次**。
Python 会缓存模块，第二次 import 直接拿缓存，不会重新跑一遍文件里的顶层代码。


#### 模块里的 `__all__`

 - 在模块里写 `__all__ = ["funcA", "MyClass"]`
 - - 作用：当写 `from xxx import *` 的时候，只会导入`__all__`写好的名字，其他的不会导出。
用来控制：哪些东西对外开放，哪些是内部私有。



### 总结

`.py文件`是硬盘上的代码文件；import 之后，在内存里生成**模块**。模块可以存放函数类，import 多次只会加载一次。多个模块放在带`__init__.py`的文件夹，就叫包。
