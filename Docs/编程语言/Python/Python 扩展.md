# Python 扩展

[原生C扩展]
[打包exe（py2exe/pyinstaller）]



#### 为什么扩展python

**用Python 本身跑得慢的地方，可以用 C 语言写代码，写完封装一下，给 Python 调用。这就叫扩展 Python，写出来的叫 C 扩展模块**.

 - Python 负责业务逻辑、读图片、控制流程；C 负责重活、计算密集活

 ####  原生 C 扩展

1. 用 C 写核心功能代码
2. 用 Python 提供的 C API，写一层 “接口胶水代码”
3. 编译 C 代码，生成`.so`(Linux) / `.pyd`(Windows) 文件
4. 在 Python 里直接`import`这个文件，就像导入普通模块

举个 CV 例子：
写 C 函数，用来遍历图像像素做滤波，速度比纯 Python 快几十倍。Python 导入这个 C 函数直接调用。

缺点：

- 要会 C 语言，开发麻烦
- 跨平台麻烦：Windows 编译一份，Linux 还要重新编译
- Python 版本一变，经常要重新编译


#### 不用手写 C 胶水代码：

- Cython：类 Python 语法，编译成 C，简化扩展开发。很多 CV 库用它。
- ctypes：直接调用现成已经编译好的 dll，不用写 Python 胶水层。工业视觉经常调用相机 SDK 的 dll。

#### Distutils

distutils 可以帮你编译 C 扩展！
在 setup.py 里声明你有 C 源码，执行安装命令时，自动调用编译器把 C 代码编译成扩展模块。
OpenCV、numpy 底层大量 C 代码，就是靠这种方式编译打包


### 总结

 - 知道很多视觉库底层不是 Python，是 C 写的扩展模块；遇到图像密集运算，纯 Python 太慢，可以 C/C++ 加速。
 - ctypes 调用相机、运动控制板卡的 dll，工业视觉项目很常用
