# Python 文件操作

[操作逻辑]
[打开模式]




#### 文件操作

**文件操作就是用 Python 代码代替你手动打开、读、写、保存电脑上的 txt、图片、csv 这类文件**.

#### 操作逻辑
1. **open()**：打开文件（开门），必须指定：文件路径 + 打开模式
2. **读 / 写**：read ()、write () 看内容或者写内容
3. **close()**：关闭文件（关门！不关闭，文件可能损坏、内容存不上）

> 推荐写法 `with open(...)`，自动关门，不用手动写 close，工作里基本都用这个。



```python

# 读文件
# with自动关闭文件
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read() # 一次性读取全部文字
    # f.readline() 读一行
    # f.readlines() 按行读取，返回列表，一行是列表里一个元素
print(content)


# 写文件

# w模式，会清空旧内容
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("hello python\n") # \n代表换行

# a追加模式，在末尾添加
with open("test.txt", "a", encoding="utf-8") as f:
    f.write("追加一行文字")


```

### 总结

- 判断文件是否存在：`os.path.exists("xxx.txt")`
- 删除文件：`os.remove()`
- 重命名文件：`os.rename(旧名,新名)`
- 遍历文件夹所有文件：`os.listdir()` （**机器视觉批量读取图片文件夹超级常用**）

## 重点

1. 忘记关闭文件，数据可能丢失；用 with 就避开这个坑
2. `w` 模式一打开就清空文件，别手误覆盖重要文件
3. 中文不写 encoding，大概率乱码
4. 读图片、视频不能用`r`文本模式，要用`rb`二进制
