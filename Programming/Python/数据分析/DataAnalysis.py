
# Pandas做数据清洗------------------------


# Pandas和Matplotlib是Python数据分析流程里配合最默契的一对：‌Pandas负责把数据洗干净、整理好，Matplotlib再把整理好的数据画成图‌。简单说就是“Pandas管数据，Matplotlib管看图”，先清洗后可视化，顺序别反。‌‌

# 🧹 Pandas数据清洗：先把数据弄“干净”
# 数据分析前，原始数据通常会有缺失值、重复行、格式乱、异常值这些问题，清洗就是把这些坑填平或删掉，不然分析结果会跑偏。‌‌

# ‌缺失值处理‌：用 isnull() 查缺失，用 dropna() 删掉含空值的行，或用 fillna() 填充（比如用均值、中位数）。
# ‌重复值处理‌：用 duplicated() 查重复，drop_duplicates() 直接去重。
# ‌格式统一‌：日期用 pd.to_datetime() 转成标准格式，文本用 str.strip() 去空格、str.lower() 统一大小写，数字列用 pd.to_numeric() 转数值。
# ‌异常值处理‌：用 describe() 看最大值、均值这些统计量，或画箱线图找出离谱的值，再决定删掉还是替换。‌‌
# 清洗逻辑一般是：先处理缺失值，再格式化，最后处理异常值，每步操作保留原始数据备份，方便回溯。‌‌

#  Matplotlib数据可视化：把“干净”数据画出来
# 清洗完的数据就可以拿来画图了，Matplotlib能画折线图、柱状图、散点图、直方图这些常用图表。‌‌

# ‌折线图‌：plt.plot(x, y)，适合看数据随时间的变化趋势。
# ‌柱状图‌：plt.bar(categories, values)，适合对比不同类别的数值大小。
# ‌散点图‌：plt.scatter(x, y)，适合看两个变量之间的关系。
# ‌直方图‌：plt.hist(data, bins=n)，适合看数据分布情况。‌‌
# 绘图时记得加上标题（plt.title()）、轴标签（plt.xlabel() / plt.ylabel()）和图例（plt.legend()），不然图出来别人看不懂。‌‌







# df = pd.read_csv(
#     'orders_01.csv',
#     encoding='utf-8',        # 文件编码，经常需要切换
#     sep=',',                 # 分隔符，CSV 默认逗号
#     dtype={'订单ID': str},    # 指定列的数据类型，防止 ID 变成数值
#     parse_dates=['下单时间'],  # 把日期列自动转成 datetime 类型
#     skiprows=0              # 跳过文件开头几行“说明文字”
# )

# 模拟数据
import pandas as pd
import numpy as np

df = pd.DataFrame({
    '用户ID': ['U1001', 'U1002', 'U1001', 'U1004', 'U1005', 'U1006', None, 'U1008', 'U1008', 'U1010'],
    '姓名': [' 张三', '李四', '张三', '王五', '赵六 ', None, '孙七', '李四', '李四', '周八'],
    '城市': ['北京', '上海', '北京', '广州', '深圳', '杭州', None, '上海', '上海', '南京'],
    '注册日期': ['2024-01-15', '2024/02/20', '2024-01-15', '20240305', '2024-04-10', '2024-05-11', '2024年6月1日', '2024-02-20', '2024-02-20', '2024-07-30'],
    '消费金额': ['1,299.50', '899', '1,299.50', None, '3,500.00', '1200.5', '799', '899', '899', '12,000.00'],
    '年龄': [25, 30, 25, 28, 35, None, 22, 30, 30, 120],
    'VIP等级': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'B', 'A']
})


# 数据清洗本质上是一个“把原始数据规整为统一、准确、可用格式”的过程
#  info() 看类型和缺失，
#  shape（） 看规模，
#  describe() 看数值分布，
#  nunique() 看离散字段的去重数

# 非数值列，用 df['VIP等级'].value_counts() 和 df['城市'].nunique() 来看分布和去重数量

df['城市'] = df['城市'].fillna('未知') 

# 所有列的缺失数量和比例
missing_count = df.isna().sum()
missing_ratio = df.isna().sum() / len(df)
missing_df = pd.DataFrame({'缺失数量': missing_count, '缺失比例': missing_ratio})
print(missing_df)


# print(df.info());
# print(df.describe());
# print(df['VIP等级'].value_counts());
# print(df['城市'].nunique(dropna=False));



# # 第3步：按业务场景处理缺失值
# # 分类文本列：城市填"未知"
# df['城市'] = df['城市'].fillna('未知')

# # 数值列：消费金额缺失去填充，没有消费记录就填0
# df['消费金额'] = df['消费金额'].fillna(0)

# # 数值列：年龄缺失用中位数填充
# median_age = df['年龄'].median()
# df['年龄'] = df['年龄'].fillna(median_age)

# # 标识列：用户ID缺失，但金额存在，标记为未知客户
# df['用户ID'] = df['用户ID'].fillna('U0000')

# # 姓名缺失：用"匿名用户"标记，避免后续groupby时丢失该样本
# df['姓名'] = df['姓名'].fillna('匿名用户')


# df.dropna(subset=['用户ID', '消费金额'], thresh=2) 


# 第4步：基于关键列处理重复值
# subset指定判断重复的列，keep='first'保留第一条
# df = df.drop_duplicates(subset=['用户ID'], keep='first')


# 第5步：统一数据类型
# 消费金额：去逗号 -> 转浮点
df['消费金额'] = df['消费金额'].str.replace(',', '', regex=False).astype(float)

# 年龄：转整数，因为年龄不可能是小数
df['年龄'] = df['年龄'].astype(int)


# 日期统一为datetime类型
df['注册日期'] = pd.to_datetime(df['注册日期'], errors='coerce')


# 第6步：文本规范化
df['姓名'] = df['姓名'].str.strip()
df['城市'] = df['城市'].str.strip()


# 第7步：用IQR法检测异常值
Q1 = df['年龄'].quantile(0.25)
Q3 = df['年龄'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
anomaly_mask = (df['年龄'] < lower_bound) | (df['年龄'] > upper_bound)
print('异常值数量：', anomaly_mask.sum())



# 第8步：列名标准化与索引重置
df.columns = df.columns.str.strip()
df = df.reset_index(drop=True)


# 第9步：全量校验
print('剩余缺失值数量: ', df.isna().sum().sum())
print('重复用户ID数量: ', df.duplicated(subset=['用户ID']).sum())
print(df['消费金额'].describe())



# 第10步：导出结果
df.to_csv('clean_users.csv', index=False, encoding='utf-8-sig')



