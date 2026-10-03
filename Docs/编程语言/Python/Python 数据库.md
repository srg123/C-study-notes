# Python 数据库

[数据库结构]
[PythonDBAPI]
[SQLite]

#### 数据库结构

**专门用来存大量结构化数据的仓库**.
1. **表 (table)**：就像 Excel 里一张工作表。一张表放一类数据。
2. **行**：Excel 的一行，代表一条记录（一条图片信息）
3. **列（字段）**：Excel 表头，比如`图片路径`、`类别`、`时间`
4. **SQL**：操作数据库的语言，用来：增、查、改、删数据


#### PythonDBAPI

 **统一的接口标准**.
 - 数据库有很多种：MySQL、SQLite、PostgreSQL。
 - 如果没有统一标准，每种数据库的 Python 代码写法完全不一样。
 - DB API 规定一套通用规则：连接数据库、建表、插入数据、查询数据。
换数据库，代码改动很小

#### SQLite
**轻量级文件数据库**

 - 不需要单独装数据库服务，它就是一个`.db`文件，直接存在电脑磁盘。
不用启动服务器，Python 自带驱动，开箱即用




```python

import sqlite3

# 1.连接数据库，文件不存在会自动创建test.db
conn = sqlite3.connect("test.db")
# 2.拿到游标
cur = conn.cursor()

# 建一张表，存图片信息
cur.execute('''
CREATE TABLE IF NOT EXISTS img_info(
    id INTEGER PRIMARY KEY,
    img_path TEXT,
    label TEXT
)
''')

# 插入一条数据
cur.execute("INSERT INTO img_info(img_path,label) VALUES (?,?)", ("test1.jpg","ok"))
# 提交，保存修改
conn.commit()

# 查询所有记录
cur.execute("SELECT * FROM img_info")
# fetchall拿到全部查询结果
res = cur.fetchall()
print(res)

# 关闭
cur.close()
conn.close()


```

### Python 操作数据库的流程

1. 连接数据库（打开仓库大门）
2. 获取游标 cursor（相当于给你一支笔，可以写 SQL 指令）
3. 执行 SQL 语句：新增、查询、修改、删除
4. 提交事务（如果是写入修改，确认保存；查询不用）
5. 关闭游标、关闭连接（关门）


