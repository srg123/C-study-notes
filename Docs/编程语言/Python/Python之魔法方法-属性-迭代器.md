# python 知识点

[![魔法方法]]
[![属性]]
[![迭代器]]



#### 魔法方法

**名字前后带两个下划线 `__xxx__` 的函数，不用你手动调用，Python 会在特定时机自动帮你跑**。就像内置的 “自动触发钩子”.

 - `__init__`：初始化方法。创建对象的时候自动执行。 
 - `__str__`：打印对象的时候自动触发。不写的话打印会出来一串看不懂的对象地址；写了就可以自定义打印内容.
 - `__getitem__`：支持 `对象[下标]` 取值。写了这个，你的类就可以像列表一样用 `obj[0]`，**CV 数据集类超级常用**。 
 - `__len__`：调用`len(对象)`自动执行，返回长度。 

#### 属性

 **把类里面的方法伪装成普通变量，访问的时候像读变量，实际跑的是函数**.

 - `property`：有时候读取 / 修改一个变量，你想顺便加校验、自动计算，但是又不想让使用者调用函数 &mdash;



#### 迭代器


 **可以逐个吐出数据的工具，能被 for 循环遍历**.

 - 可迭代对象（Iterable）：能放到 for 循环里跑的东西，比如列表、字符串;
 - 有`__iter__` 和 `__next__`这两个魔法方法
 - - `__iter__`：for 循环启动时调用，返回迭代器自己
 - - `__next__`：每循环一次，就调用一次，返回下一个元素；没有数据了就抛出`StopIteration`停止循环。

### 用例

1. **魔法方法**：双下划线函数，Python 自动触发，用来定制类的行为（创建对象、下标取值、打印、求长度）
2. **property 属性**：把函数伪装成变量，读写时附带校验 / 自动计算
3. **迭代器**：实现`__iter__`、`__next__`，让对象支持 for 循环逐个拿数据，数据集必备.

```python
class ImageDataset:
    def __init__(self, img_list):
        """
        __init__ 魔法方法：实例创建时自动调用
        作用：给对象初始化数据
        """
        # 保存图片路径列表
        self.img_list = img_list
        # 当前迭代索引，迭代器用
        self.current_index = 0

    @property
    def total_count(self):
        """
        property 属性：把方法伪装成变量
        使用：obj.total_count  不用写括号，自动执行这个函数
        好处：每次读取动态计算，外部看起来像读取普通属性
        """
        return len(self.img_list)

    def __getitem__(self, index):
        """
        魔法方法 __getitem__
        作用：支持 对象[下标] 取值，像列表一样
        CV数据集类高频使用：dataset[0]拿到第1张图片
        """
        if index < 0 or index >= self.total_count:
            raise IndexError("图片下标超出范围！")
        return self.img_list[index]

    def __len__(self):
        """
        魔法方法 __len__
        调用len(对象)的时候自动执行，返回总数
        """
        return self.total_count

    def __iter__(self):
        """
        魔法方法 __iter__
        for循环开始时触发，返回迭代器本身
        """
        # 每次开始循环，把索引重置到0
        self.current_index = 0
        return self

    def __next__(self):
        """
        魔法方法 __next__
        for循环每一轮自动调用，取出下一个元素
        没有数据时抛出 StopIteration，循环终止
        """
        # 判断是否遍历完所有图片
        if self.current_index >= self.total_count:
            raise StopIteration
        # 获取当前图片路径
        img_path = self.img_list[self.current_index]
        # 索引+1，准备下一次
        self.current_index += 1
        return img_path

    def __str__(self):
        """
        魔法方法 __str__
        print(对象)自动触发，自定义打印信息
        """
        return f"图片数据集，一共{self.total_count}张图片"


# ============ 测试代码 ============
if __name__ == "__main__":
    # 图片路径列表，模拟数据集
    paths = ["img01.jpg", "img02.jpg", "img03.jpg", "img04.jpg"]
    # 创建实例，自动调用 __init__
    dataset = ImageDataset(paths)

    # 调用 __str__
    print(dataset)

    # 使用 property属性，不带括号
    print("图片总数：", dataset.total_count)

    # 调用 __getitem__ ，用下标取图片
    print("第2张图片：", dataset[1])

    # 调用 __len__
    print("len查看总数：", len(dataset))

    # for循环遍历，底层调用 __iter__ 和 __next__
    print("\nfor循环遍历所有图片：")
    for img in dataset:
        print(img)

```



### 用例总结

1. `__init__` / `__getitem__` / `__len__` / `__iter__` / `__next__` / `__str__` 都是**魔法方法**，前后双下划线，自动触发，不用手动调用
2. `@property` 装饰器：函数变属性，`dataset.total_count`，动态获取值，外部不能随便改这个总数
3. `__iter__` + `__next__` 一起实现迭代器，让这个类支持 for 循环，就是 Pytorch Dataset 底层的核心思想

