
# 读取旧版 .xls 文件
from pathlib import Path
import xlrd

workbook_path = Path(__file__).with_name('P020260907422800382239.xls')
wb = xlrd.open_workbook(str(workbook_path))
type(wb)

# xlrd 以只读方式读取 .xls 工作簿
# sheet_names：获取工作簿中的表名
# sheets：获取所有工作表
# sheet_by_index：按索引获取工作表
# encoding：获取文档编码

wb.sheet_names()
# ['Sheet1', 'Sheet2', 'Sheet3']
 
wb.sheets()
# [<xlrd.sheet.Sheet object>, <xlrd.sheet.Sheet object>, <xlrd.sheet.Sheet object>]
 
wb.sheet_by_index(0)
# <xlrd.sheet.Sheet object; name 'Sheet1'>
 
wb.encoding
# 'utf-8'

# xlrd 不支持读取工作簿属性或新增工作表；需要编辑时先将文件转换为 .xlsx，再用 openpyxl。
 