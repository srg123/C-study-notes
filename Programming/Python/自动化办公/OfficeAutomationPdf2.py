

# 文本提取

import pdfplumber

with pdfplumber.open("report.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            print(text)

# ‌带格式的文本提取‌：想获取字体、位置等元数据，用 extract_words()

# with pdfplumber.open("formatted_doc.pdf") as pdf:
#     page = pdf.pages
#     words = page.extract_words()
#     for word in words:
#         print(f"内容: {word['text']}, 位置: ({word['x0']}, {word['top']}), 字体: {word['fontname']}")
# ```‌‌:ml-citation{ref="0" appearance="aggregated" data="citationList"}

# &zwnj;**按区域提取**&zwnj;：只提取指定坐标区域的内容（比如发票金额），用 `crop()`：‌‌:ml-citation{ref="1,11" appearance="aggregated" data="citationList"}


# with pdfplumber.open("invoice.pdf") as pdf:
#     page = pdf.pages
#     # (x0, top, x1, bottom)，单位为点（1英寸=72点）
#     amount_area = (300, 400, 500, 420)
#     cropped = page.crop(amount_area)
#     print("发票金额:", cropped.extract_text())
# ```‌‌:ml-citation{ref="0" appearance="aggregated" data="citationList"}

# ### 📊 表格提取

# 这是pdfplumber的招牌功能，能自动识别表格边框线并输出结构化数据。‌‌:ml-citation{ref="1,7" appearance="aggregated" data="citationList"}

# &zwnj;**基础表格提取**&zwnj;：对于有清晰边框的表格，直接调用 `extract_table()`：‌‌:ml-citation{ref="1" appearance="aggregated" data="citationList"}


# with pdfplumber.open("financial_report.pdf") as pdf:
#     page = pdf.pages
#     table = page.extract_table()
#     if table:
#         print("表头:", table)
#         for row in table[1:4]:
#             print("数据行:", row)
# ```‌‌:ml-citation{ref="1,0" appearance="aggregated" data="citationList"}

# 提取结果是二维列表，可直接转成pandas DataFrame：‌‌:ml-citation{ref="1,10" appearance="aggregated" data="citationList"}


# import pandas as pd
# df = pd.DataFrame(table[1:], columns=table)
# df.to_excel("output.xlsx", index=False)
# ```‌‌:ml-citation{ref="0" appearance="aggregated" data="citationList"}

# &zwnj;**无边框表格**&zwnj;：需要自定义识别策略，把默认的 `"lines"` 改成 `"text"`，让pdfplumber根据文字对齐位置推断表格边界：‌‌:ml-citation{ref="1,4" appearance="aggregated" data="citationList"}


# table_settings = {
#     "vertical_strategy": "text",   # 基于文本分布确定垂直分割线
#     "horizontal_strategy": "text", # 基于文本分布确定水平分割线
#     "min_words_vertical": 2,       # 至少2个文字垂直对齐才认为有列边界
#     "min_words_horizontal": 1,
#     "text_tolerance": 5,           # 允许5点的偏移容差
# }

# with pdfplumber.open("no_border.pdf") as pdf:
#     page = pdf.pages
#     table = page.extract_table(table_settings)
# ```‌‌:ml-citation{ref="0" appearance="aggregated" data="citationList"}

# &zwnj;**跨页表格合并**&zwnj;：多页连续表格需要跳过后续页面的重复表头：‌‌:ml-citation{ref="1,12" appearance="aggregated" data="citationList"}


# full_table = []
# with pdfplumber.open("multi_page_table.pdf") as pdf:
#     for i, page in enumerate(pdf.pages):
#         table = page.extract_table()
#         if not table:
#             continue
#         if i == 0:
#             full_table.extend(table)   # 第一页保留表头
#         else:
#             full_table.extend(table[1:])  # 其他页跳过表头



# 可视化调试
# 表格提取不准时，用 debug_tablefinder() 把检测到的线条和表格边界画出来，问题一目了然：‌‌


# with pdfplumber.open("debug_target.pdf") as pdf:
#     page = pdf.pages
#     im = page.to_image()
#     im.debug_tablefinder()  # 高亮显示检测到的表格线
#     im.save("table_debug.png")
# ```‌‌:ml-citation{ref="0" appearance="aggregated" data="citationList"}

# 需要先安装 Pillow 库。

# ### ⚠️ 重要限制

# - &zwnj;**扫描件无效**&zwnj;：pdfplumber只能处理电子版PDF（有文字层），扫描件需要配合OCR工具（如paddleocr）使用。
# - &zwnj;**中文支持**&zwnj;：整体不错，但如果PDF嵌入了特殊字体或编码有问题，可能出现乱码，建议用 `page.chars` 排查。
# - &zwnj;**内存占用**&zwnj;：处理几百页的大文件时内存占用较高，建议逐页处理而不是一次性加载整个文档。‌‌:ml-citation{ref="4,7" appearance="aggregated" data="citationList"}

# :::ml-data{name=citationList}
# ```json
# [{"source":{"logo":"","name":"腾讯云"},"disabled":false,"isVideo":false,"title":"处理pdf相关pdfplumber","thumbnail":"","linkInfo":{"data-click-info":"{}","href":"https://cloud.tencent.com/developer/article/2692100","target":"_blank","data-noblank":true,"data-show":"list","data-show-ext":"{\"pos\":\"1\",\"component_content\":{\"component_name\":\"reference\"}}"}},{"source":{"logo":"","name":"腾讯云"},"disabled":false,"isVideo":false,"title":"当涉及到PDF中的数据挖掘,PDFPlumber是您的得力助手","thumbnail":"http://t9.baidu.com/it/u=4072917047,901739124&fm=217&app=126&f=JPEG?w=610&h=785&s=21B04533591F75CC467D84DA030080B2","linkInfo":{"data-click-info":"{}","href":"https://cloud.tencent.com/developer/article/2350162","target":"_blank","data-noblank":true,"data-show":"list","data-show-ext":"{\"pos\":\"2\",\"component_content\":{\"component_name\":\"reference\"}}"}},{"source":{"logo":"","name":"知乎"},"disabled":false,"isVideo":false,"title":"Python助你轻松实现PDF格式转换:PDFplumber","thumbnail":"http://t8.baidu.com/it/u=3225127214,2903566355&fm=3031&app=3031&f=JPEG?w=495&h=274&s=29B4ED16978578EAC86845DF010080A2","linkInfo":{"data-click-info":"{}","href":"https://zhuanlan.zhihu.com/p/344770523","target":"_blank","data-noblank":true,"data-show":"list","data-show-ext":"{\"pos\":\"3\",\"component_content\":{\"component_name\":\"reference\"}}"}},{"source":{"logo":"","name":"CSDN博客"},"disabled":false,"isVideo":false,"title":"Python pdfplumber实战:PDF表格数据提取与参数调优指南","thumbnail":"","linkInfo":{"data-click-info":"{}","href":"https://blog.csdn.net/weixin_34194087/article/details/88739220","target":"_blank","data-noblank":true,"data-show":"list","data-show-ext":"{\"pos\":\"4\",\"component_content\":{\"component_name\":\"reference\"}}"}},{"source":{"logo":"","name":"百度智能云"},"disabled":false,"isVideo":false,"title":"Python解析PDF工具对比:pdfminer、tabula与pdfplumber实战指南","thumbnail":"","linkInfo":{"data-click-info":"{}","href":"https://cloud.baidu.com/article/3696683","target":"_blank","data-noblank":true,"data-show":"list","data-show-ext":"{\"pos\":\"5\",\"component_content\":{\"component_name\":\"reference\"}}"}},{"source":{"logo":"","name":"CSDN博客"},"disabled":false,"isVideo":false,"title":"用Python+pdfplumber一键提取PDF表格到Excel,批量处理与调参指南","thumbnail":"","linkInfo":{"data-click-info":"{}","href":"https://blog.csdn.net/weixin_34199764/article/details/164447625","target":"_blank","data-noblank":true,"data-show":"list","data-show-ext":"{\"pos\":\"6\",\"component_content\":{\"component_name\":\"reference\"}}"}},{"source":{"logo":"","name":"CSDN博客"},"disabled":false,"isVideo":false,"title":"5分钟上手PDF解析:pdfplumber新手第一课,安装并跑通你的第一个提取示例","thumbnail":"http://t7.baidu.com/it/u=439924559,2515514661&fm=217&app=137&f=JPEG?w=800&h=400&s=68F1A9441A23BB570E6C4D9803005086","linkInfo":{"data-click-info":"{}","href":"https://blog.csdn.net/gitblog_00599/article/details/162961775","target":"_blank","data-noblank":true,"data-show":"list","data-show-ext":"{\"pos\":\"7\",\"component_content\":{\"component_name\":\"reference\"}}"}},{"source":{"logo":"","name":"知乎"},"disabled":false,"isVideo":false,"title":"Python助你轻松实现PDF格式转换:PDFplumber","thumbnail":"http://t8.baidu.com/it/u=3225127214,2903566355&fm=3031&app=3031&f=JPEG?w=495&h=274&s=29B4ED16978578EAC86845DF010080A2","linkInfo":{"data-click-info":"{}","href":"https://zhuanlan.zhihu.com/p/344770523","target":"_blank","data-noblank":true,"data-show":"list","data-show-ext":"{\"pos\":\"8\",\"component_content\":{\"component_name\":\"reference\"}}"}},{"source":{"logo":"","name":"腾讯云"},"disabled":false,"isVideo":false,"title":"​Python 操作pdf(pdfplumber读取PDF写入Exce)","thumbnail":"http://t7.baidu.com/it/u=30696970,4109903053&fm=217&app=126&f=JPEG?w=722&h=637&s=E39AC32BEBC742DA1D7DA0CF030010B0","linkInfo":{"data-click-info":"{}","href":"https://cloud.tencent.com/developer/article/2360141","target":"_blank","data-noblank":true,"data-show":"list","data-show-ext":"{\"pos\":\"9\",\"component_content\":{\"component_name\":\"reference\"}}"}},{"source":{"logo":"","name":"CSDN博客"},"disabled":false,"isVideo":false,"title":"Python pdfplumber实战:PDF表格提取与Excel导出指南-CSDN博客","thumbnail":"","linkInfo":{"data-click-info":"{}","href":"https://blog.csdn.net/weixin_33851429/article/details/94587883","target":"_blank","data-noblank":true,"data-show":"list","data-show-ext":"{\"pos\":\"10\",\"component_content\":{\"component_name\":\"reference\"}}"}},{"source":{"logo":"","name":"脚本之家"},"disabled":false,"isVideo":false,"title":"Python中PDF解析利器pdfplumber的使用详细教程","thumbnail":"","linkInfo":{"data-click-info":"{}","href":"https://www.jb51.net/python/339016ufz.htm","target":"_blank","data-noblank":true,"data-show":"list","data-show-ext":"{\"pos\":\"11\",\"component_content\":{\"component_name\":\"reference\"}}"}},{"source":{"logo":"","name":"CSDN博客"},"disabled":false,"isVideo":false,"title":"Python pdfplumber提取PDF表格:从原理到实战的完整指南-CSDN博客","thumbnail":"","linkInfo":{"data-click-info":"{}","href":"https://blog.csdn.net/weixin_34391445/article/details/89697696","target":"_blank","data-noblank":true,"data-show":"list","data-show-ext":"{\"pos\":\"12\",\"component_content\":{\"component_name\":\"reference\"}}"}},{"source":{"logo":"","name":"哔哩哔哩"},"disabled":false,"isVideo":true,"title":"Python案例技巧6:pdf文档文本提取","thumbnail":"http://t13.baidu.com/it/u=2644852003,1728415004&fm=225&app=113&f=JPEG?w=1728&h=1080&s=E3D27282C7A28EE91ED8F1050300B0C1","linkInfo":{"data-click-info":"{}","href":"http://www.bilibili.com/video/BV1wcscebE6A","target":"_blank","data-noblank":true,"data-show":"list","data-show-ext":"{\"pos\":\"13\",\"component_content\":{\"component_name\":\"reference\"}}"}},{"source":{"logo":"","name":"腾讯云"},"disabled":false,"isVideo":false,"title":"Python提取PDF内容,4个方法让效率翻倍!","thumbnail":"http://t8.baidu.com/it/u=594202801,187479296&fm=217&app=126&f=JPEG?w=800&h=499&s=B83740964CDE25C85D0A799903005098","linkInfo":{"data-click-info":"{}","href":"https://cloud.tencent.com/developer/article/2712594","target":"_blank","data-noblank":true,"data-show":"list","data-show-ext":"{\"pos\":\"14\",\"component_content\":{\"component_name\":\"reference\"}}"}},{"source":{"logo":"","name":"知乎"},"disabled":false,"isVideo":false,"title":"如何使用python提取pdf表格及文本,并保存到excel","thumbnail":"http://t8.baidu.com/it/u=24360154,223164019&fm=3031&app=3031&f=JPEG?w=720&h=312&s=5CA43D72857054215878F4C80000A0B1","linkInfo":{"data-click-info":"{}","href":"https://zhuanlan.zhihu.com/p/353397002","target":"_blank","data-noblank":true,"data-show":"list","data-show-ext":"{\"pos\":\"15\",\"component_content\":{\"component_name\":\"reference\"}}"}},{"source":{"logo":"","name":"php中文网"},"disabled":false,"isVideo":false,"title":"Python PDF处理实战指南:用pdfplumber精准提取文本与表格","thumbnail":"http://t9.baidu.com/it/u=1557132764,4143294638&fm=217&app=126&f=JPEG?w=700&h=395&s=3C8E743303526C631C7DDBEA0300A035","linkInfo":{"data-click-info":"{}","href":"https://www.php.cn/faq/3138058.html","target":"_blank","data-noblank":true,"data-show":"list","data-show-ext":"{\"pos\":\"16\",\"component_content\":{\"component_name\":\"reference\"}}"}},{"source":{"logo":"","name":"知乎"},"disabled":false,"isVideo":false,"title":"我把pdfplumber整成了可以拖拉拽的web应用","thumbnail":"http://t7.baidu.com/it/u=2159592762,1404963252&fm=3031&app=3031&f=JPEG?w=720&h=349&s=88235F301F0A4C4912D0B0C9000010B1","linkInfo":{"data-click-info":"{}","href":"https://zhuanlan.zhihu.com/p/1978571760938022319","target":"_blank","data-noblank":true,"data-show":"list","data-show-ext":"{\"pos\":\"17\",\"component_content\":{\"component_name\":\"reference\"}}"}}]
