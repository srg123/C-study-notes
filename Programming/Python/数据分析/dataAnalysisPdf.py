# PyPDF2处理PDF


# 说明
# 如果只是合并、拆分、旋转、加密这些页面级操作，PyPDF2 完全够用，轻量又好上手。
# 但要是经常要抠表格数据或者扫描件文字，建议直接用 pdfplumber



# ‌合并多个 PDF‌：用 PdfMerger 最方便，支持批量追加

from PyPDF2 import PdfMerger

merger = PdfMerger()
for pdf in ["1.pdf", "2.pdf", "3.pdf"]:
    merger.append(pdf)
merger.write("merged.pdf")
merger.close()


# ‌拆分 PDF‌：按页码范围提取页面，生成新文件

from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("input.pdf")
writer = PdfWriter()
for i in range(0, 3):  # 提取第1-3页
    writer.add_page(reader.pages[i])
with open("split.pdf", "wb") as f:
    writer.write(f)


# 提取文本‌：逐页读取文字内容，适合纯文本型 PDF。

from PyPDF2 import PdfReader

reader = PdfReader("test.pdf")
for page in reader.pages:
    print(page.extract_text())



# 加密 PDF‌：给文档设置访问密码。

from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("input.pdf")
writer = PdfWriter()
for page in reader.pages:
    writer.add_page(page)
writer.encrypt("your_password")
with open("encrypted.pdf", "wb") as f:
    writer.write(f)


# ‌添加水印‌：把水印页和每一页合并。

from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("input.pdf")
watermark = PdfReader("watermark.pdf").pages
writer = PdfWriter()
for page in reader.pages:
    page.merge_page(watermark)
    writer.add_page(page)
with open("watermarked.pdf", "wb") as f:
    writer.write(f)
# `‌‌:ml-citation{ref="0" appearance="aggregated" data="citationList"}

#  &zwnj;**旋转页面**&zwnj;：支持 90、180、270 度。

from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("input.pdf")
writer = PdfWriter()
for i, page in enumerate(reader.pages):
    if i == 2:  # 旋转第3页
        page.rotate(90)
    writer.add_page(page)
with open("rotated.pdf", "wb") as f:
    writer.write(f)



# 注意几个坑
# ‌中文文本提取可能乱码‌：PyPDF2 依赖 PDF 内部的字体编码，遇到复杂格式或扫描件，提取效果会打折扣。想要更准的文本提取，建议换 <u>pdfplumber</u> 或 <u>PyMuPDF</u>。
# ‌不能提取图片和表格‌：它只处理页面和文本，图片、表格这些搞不定。
# ‌大文件处理慢‌：超过 50MB 的文件建议用流式读取，避免内存溢出。
# ‌加密 PDF 要密码‌：读取加密文件前先调 decrypt() 验证密码，否则会报错。‌‌