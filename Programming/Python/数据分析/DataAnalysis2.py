def clean_user_data(raw_df: pd.DataFrame) -> pd.DataFrame:
    """用户数据清洗流水线，输入原始DataFrame，返回清洗后的DataFrame"""
    df = raw_df.copy()

    # 1. 缺失值处理
    df['城市'] = df['城市'].fillna('未知')
    df['消费金额'] = df['消费金额'].fillna(0)
    median_age = df['年龄'].median()
    df['年龄'] = df['年龄'].fillna(median_age)
    df['用户ID'] = df['用户ID'].fillna('U0000')
    df['姓名'] = df['姓名'].fillna('匿名用户')

    # 2. 重复值处理
    df = df.drop_duplicates(subset=['用户ID'], keep='first')

    # 3. 类型转换
    df['消费金额'] = df['消费金额'].str.replace(',', '', regex=False).astype(float)
    df['年龄'] = df['年龄'].astype(int)
    df['注册日期'] = pd.to_datetime(df['注册日期'], errors='coerce')

    # 4. 文本规范化
    df['姓名'] = df['姓名'].str.strip()
    df['城市'] = df['城市'].str.strip()

    # 5. 异常值处理（IQR法，超界值用中位数替代）
    Q1 = df['年龄'].quantile(0.25)
    Q3 = df['年龄'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df.loc[(df['年龄'] < lower_bound) | (df['年龄'] > upper_bound), '年龄'] = int(df['年龄'].median())

    # 6. 索引重置
    df = df.reset_index(drop=True)
    return df

clean_df = clean_user_data(df)
print(clean_df)






# 问题现象	
# 原因分析	
# 解决方案

# astype(float) 报 ValueError
# 字符串列中混有 , 、 $ 、 % 等符号
# 先用 str.replace 去掉符号，再转换类型


# 日期解析后全是 NaT
# 日期格式特殊， to_datetime 默认识别不了
# 用 pd.to_datetime(s, format='%Y年%m月%d日', errors='coerce') 指定格式

# 清洗后数据行数不对
# 重复值删除或缺失值删除导致行数减少
# 每次删除操作后打印 len(df) ，并在最后记录清洗前后行数

# dropna() 把不该删的行删了
# 默认按整行所有字段判断，任一字段缺失就删
# 用 subset 指定关键字段，用 thresh 指定非空数量阈值

# 分组统计结果出现同一用户多行
# 重复行没有被完全识别，存在字段差异
# 先按业务主键去重，必要时先聚合再降重

# 导出 CSV 用 Excel 打开乱码	
# 重复行没有被完全识别，存在字段差异
# 导出时指定 encoding='utf-8-sig'


# 文本列有不可见字符
# 空格、换行、制表符混在字符串里
# 用 str.strip() 去首尾空白，用 str.replace('\n', '') 去换行，用 repr() 查看真实内容




# # 读取数据
# df = pd.read_csv('胡润百富榜_待清洗.csv')

# # 去除全名_中文列中名字含有的空格
# df['全名_中文'] = df['全名_中文'].str.replace(' ', '')

# # 处理出生地_英文列的缺失值，用出生地_中文列对应的值替代
# df['出生地_英文'] = df['出生地_英文'].fillna(df['出生地_中文'])

# # 将排名变化列和财富值变化列的百分数转换为数值型
# df['排名变化'] = df['排名变化'].str.rstrip('%').astype(float) / 100
# df['财富值变化'] = df['财富值变化'].str.rstrip('%').astype(float) / 100

# # 将年龄列转换为数值型并处理非数值值
# df['年龄'] = pd.to_numeric(df['年龄'], errors='coerce')

# # 去除没用的列-照片列
# df = df.drop(columns='照片')

# # 将排名变化列中的特殊值替换为 0
# df['排名变化'] = df['排名变化'].replace('New', '0')

# # 将财富值变化列中的特殊值替换为 0
# df['财富值变化'] = df['财富值变化'].replace('NEW', '0')

# # 将结果另外保存为csv文件
# df.to_csv('胡润百富榜_清洗后.csv', index=False, encoding='utf_8_sig')




# # 读取数据
# df = pd.read_csv('淄博烧烤B站评论_待清洗.csv')

# # 加载中文停用词
# with open('cn_stopwords.txt', 'r', encoding='utf-8') as file:
#     stopwords = [line.strip() for line in file.readlines()]

# def remove_emoji(text):
# 	"""清洗表情符号"""
# 	emoji_pattern = re.compile(
# 		"["
# 		u"\U0001F600-\U0001F64F"  # emoticons  
# 		u"\U0001F300-\U0001F5FF"  # symbols & pictographs  
# 		u"\U0001F680-\U0001F6FF"  # transport & map symbols  
# 		u"\U0001F1E0-\U0001F1FF"  # flags (iOS)  
# 		u"\U00002702-\U000027B0"  # Arrows  
# 		u"\U000024C2-\U0001F251"  # currency, units (², ㎎, ®, ₿)  
# 		u"\U0001f926-\U0001f937"  # Handshake  
# 		# 可以根据需要添加更多的Unicode范围  
# 		"]+",
# 		flags=re.UNICODE
# 	)
# 	return emoji_pattern.sub(r' ', text)

# # 定义函数去除停用词、转换为小写、去除表情符号
# def clean_text(text):
# 	# 去除表情符号
#     text = remove_emoji(text)
#     # 转换为小写
#     text = text.lower()
#     # 分词、去除停用词
#     words = text.split()
#     filtered_words = [word for word in words if word not in stopwords]
#     return ' '.join(filtered_words)

# # 对评论内容列进行数据清洗
# df['评论内容'] = df['评论内容'].apply(clean_text)

# # 去除空的评论内容所在的行
# df = df[df['评论内容'].str.strip() != '']

# # 把清洗结果另外保存一个csv文件
# df.to_csv('淄博烧烤B站评论_清洗后.csv', index=False, encoding='utf_8_sig')