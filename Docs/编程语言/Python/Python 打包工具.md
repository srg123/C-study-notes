# Python 打包工具

[Distutils]
[py2exe]
[pyinstaller]


#### Distutils

**用来把你的 Python 代码打包成Python 安装包（给别的 Python 开发者用），不是 exe**.
 - Distutils 作用：把你写的一堆`.py`源码，整理成压缩包，别人拿到后，可以用 `python setup.py install`，直接把你的库安装到他本机 Python 环境，之后就能`import`导入你的模块
  
  - - 你写一个`setup.py`，里面调用 distutils 的 setup 函数，写清楚：

  - - 库叫什么名字、版本
  - - 包含哪些 py 文件
  - - 作者、描述信息

```python
from distutils.core import setup

setup(
    name="mycvtool",
    version="1.0",
    description="自己写的图像处理小工具",
    py_modules=["cvtool"] # 需要打包的py模块
)



```

#### py2exe

**把**Python 解释器 + 你的代码 + 用到的所有库**捆在一起，变成一个`.exe`文件**.

#### pyinstaller（目前主流）


```python

# 安装
pip install pyinstaller
# 打包命令
pyinstaller -F cv_tool.py


别人拿到你的源码包，执行：
python setup.py install
就会自动把`cvtool.py`复制到他 Python 的库目录，之后直接`import cvtool`。

## Distutils 能干啥

1. 打包源码，生成 tar.gz 源码压缩包（源码分发包）
2. 安装你的模块到本地 Python 环境
3. 可以编译 C 语言扩展模块（C 写的代码，封装给 Python 调用，OpenCV 底层就有 C 扩展）

```

### 总结

- `-F`：所有内容打包成**单个 exe 文件**
- 打包完成后 exe 出现在 dist 文件夹里
-  打包后文件巨大，因为会把 OpenCV、Numpy 全部打包进去
- 有些动态库、模型文件、图片，不会自动打包，需要手动指定一起打包
- 杀毒软件容易误报 exe
- Distutils：Python 自带源码分发工具，用来把你的 Python 代码做成库，供其他开发者安装导入；**不能直接打包 exe**；现在被 setuptools 替代。
 - py2exe 是在 distutils 基础上增加的扩展，才可以生成 exe 文件。
 - distutils 是早期标准库工具，**功能简陋**，现在官方已经不推荐直接使用。
 - 现在替代方案：**setuptools**（distutils 的增强升级版，几乎所有人都用这个），写 setup.py 基本都是 import setuptools。
 - 它不能直接生成 exe！这点很容易和 py2exe 搞混。
 - py2exe 其实是基于 distutils 的插件，在 setup.py 里面加配置，额外扩展出打包 exe 的能力


