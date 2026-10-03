# Python 图形 GUI

[![什么是 GUI]]
[![Tkinter 是什么]]

#### 什么是 GUI

**GUI = 图形窗口界面**.

#### Tkinter 是什么

 **Tkinter 就是 Python 自带做 GUI 的工具包，不用额外安装**.

#### 事件驱动

**窗口开好之后，就原地等着，啥也不干，等待用户操作（事件）**.

 - 事件：点击按钮、鼠标移动、键盘输入;
 - 绑定：把【按钮】和【一段 Python 函数】绑在一起。点按钮，自动执行这个函数


```python

# 导入自带GUI库tkinter
import tkinter as tk

# 1. 创建主窗口（整个程序的大框架）
win = tk.Tk()
win.title("简易图片工具") # 窗口标题

# 定义按钮点击后要执行的函数
def click_func():
    print("按钮被点击！可以在这里写图片处理代码")

# 创建标签，放文字
label = tk.Label(win, text="机器视觉小工具")
label.pack() # pack：自动摆放组件

# 创建按钮，command绑定点击事件，点了就跑click_func
btn = tk.Button(win, text="点击处理图片", command=click_func)
btn.pack()

# 主循环：窗口一直运行，监听鼠标、键盘事件
win.mainloop()


```

### 用例总结

1. `win.mainloop()`：GUI 的灵魂，开启循环，一直等待鼠标点击事件
2. 什么时候会用到 GUI，工业机器视觉项目，需要做简单上位机软件
3. 窗口展示摄像头拍到的画面
4. 放按钮：【开始检测】【保存图片】
5. 在图片上画出检测框、标记缺陷 → Canvas 画布
6. PyQt / PySide：工业软件最常用，功能强，复杂视觉上位机基本用这个


