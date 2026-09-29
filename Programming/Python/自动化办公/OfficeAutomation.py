
# 打开excel
from pathlib import Path
import openpyxl,pprint

excel_path = Path(__file__).with_name('P020260618647508965495.xlsx')
wb = openpyxl.load_workbook(excel_path)
type(wb)

# 工作薄中取得工作表Worksheet
# sheetnames：获取工作簿中的表（列表）
# worksheets：以列表的形式返回所有的Worksheet(表格)
# active：获取当前活跃的Worksheet
# encoding：获取文档的字符集编码
# properties：获取文档的元数据，如标题，创建者，创建日期等
# create_sheet：创建一个空的表格

# print(wb.sheetnames)
# ['Sheet1', 'Sheet2', 'Sheet3']

# print(wb.worksheets) 
wb.worksheets
# [<Worksheet "Sheet1">, <Worksheet "Sheet2">, <Worksheet "Sheet3">]

# print(wb.active) 
wb.active
# <Worksheet "Sheet1">
 
# print(wb.encoding)
wb.encoding
# 'utf-8'

# print(wb.properties) 
wb.properties
# <openpyxl.packaging.core.DocumentProperties object>
# Parameters:
# creator='Al', title=None, description=None, subject=None, identifier=None, language=None, created=datetime.datetime(2014, 5, 16, 5, 23, 27), modified=datetime.datetime(2015, 3, 18, 23, 12, 43), lastModifiedBy='Al', category=None, contentStatus=None, version=None, revision=None, keywords=None, lastPrinted=None
 
wb.create_sheet('newSheet')
# <Worksheet "newSheet">
 
# print(wb.sheetnames)
wb.sheetnames
# ['Sheet1', 'Sheet2', 'Sheet3', 'newSheet']
 

#  从表（Worksheet）中取得单元格 

# Worksheet 对象，可以按名字访问 Cell 对象。

# Cell对象

# Cell对象比较简单，cell对象包含单元格中保存的值，常用的属性如下:                                                                                                    

# row：单元格所在的行
# column：单元格坐在的列
# value：单元格的值
# coordinate：单元格的坐标


# 常用的Worksheet属性如下：

# title：表格的标题
# columns：按列获取单元格(Cell对象) - 生成器
# values：按行获取表格的内容(数据)  - 生成器
# dimensions：表格的大小，这里的大小是指含有数据的表格的大小，即：左上角的坐标:右下角的坐标
# max_row：表格的最大行
# min_row：表格的最小行
# max_column：表格的最大列
# min_column：表格的最小列
# rows：按行获取单元格(Cell对象) - 生成器



# for www in wb:
# 	print(www.title)
 
# Sheet1
# Sheet2
# Sheet3

 
sheet1 = wb['Sheet1']
# print(sheet1['A1'])
# <Cell 'Sheet1'.A1>
# print(sheet1['A1'].value)
# datetime.datetime(2015, 4, 5, 13, 34, 2)
 
c = sheet1['B1']
# print(c.value)
# 'Apples'
 
# str(c.column)
# '2'
# c.column
# 2
 
# print(sheet1.max_row)

# print(sheet1.max_column)

 
# 'Cell' + c.coordinate + 'is' + c.value
# 'CellB1isApples'
 
# sheet1.cell(row = 1, column = 2)
# <Cell 'Sheet1'.B1>
# sheet1.cell(row =1, column = 2).value
# 'Apples'
 
# for i in range(1, 8 , 2):
# 	print(i , sheet1.cell(row = i, column = 2).value)
 
	
# 1 Apples
# 3 Pears
# 5 Apples
# 7 Strawberries


# print(tuple(sheet1['A1':'C10']))


# 直接取得电子表格中一行、一列或一个矩形区域中的所有Cell 对象
# for rowrr in sheet1['A3':'C4']:
# 	for ff in rowrr:
# 		print(ff.coordinate, ff.value)

# print(list(sheet1.columns)[1])
# (<Cell 'Sheet1'.B1>, <Cell 'Sheet1'.B2>, <Cell 'Sheet1'.B3>, <Cell 'Sheet1'.B4>, <Cell 'Sheet1'.B5>, <Cell 'Sheet1'.B6>, <Cell 'Sheet1'.B7>)
 
 
# for cello in list(sheet1.columns)[1]:
# 	print(cello.value)
 


# 创建并保存 Excel 文档 

# excel_path = Path(__file__).with_name('example_cope.xlsx')
# sheet1.title = '数据分析excel'
# wb.save(excel_path)


# 创建和删除工作表

# remove_sheet：删除一个表格
# create_sheet：创建一个空的表格


# import openpyxl
# wh = openpyxl.Workbook()
 
# wh.active
# <Worksheet "Sheet">
 
# wh.create_sheet(index = 0, title = 'First Sheet')
# <Worksheet "First Sheet">
# wh.sheetnames
# ['First Sheet', 'Sheet']
 
# wh.create_sheet(index = 2, title = 'First Sheet')
# <Worksheet "First Sheet1">
# wh.sheetnames
# ['First Sheet', 'Sheet', 'First Sheet1']
 
# wh.remove(wh['First Sheet1'])
# wh.sheetnames
# ['First Sheet', 'Sheet']

# 将值写入单元格 

# import openpyxl
# wh = openpyxl.Workbook()
 
# sheet = wh.active
# sheet
# <Worksheet "First Sheet">
 
# sheet['A1'] = 'HEELO !'
# sheet['A1'].value
# 'HEELO !'


# 设置单元格的字体风格 
# import openpyxl
# from openpyxl.styles import Font
# wb = openpyxl.Workbook()
# sheet = wb['Sheet']
 
# fontobj = Font(name = 'Times New Roman', bold = True)
# sheet.column_dimensions['A'].font = fontobj
# sheet['A1'] = 'Bold Times New Roman'
 
# fonronbj2 = Font(size = 24, italic = True)
# sheet.column_dimensions['B'].font = fonronbj2
# sheet['B3'] = '24 pt Italic'
 
# wb.save('styles.xlsx')


#  公式

# 公式以一个等号开始，可以配置单元格，让其包含通过其他单元格计算得到的值

# import openpyxl
# wb = openpyxl.Workbook()
# sheet = wb['Sheet']
# sheet['A1'] = 200
# sheet['A2'] = 300
# sheet['A3'] = '=SUM(A1:A2)'
# wb.save('writeFormula.xlsx')


# 设置行高和列宽 


# import openpyxl
# wb = openpyxl.Workbook()
# sheet = wb.active
# sheet['A1'] = 'Tall row'
# sheet['B2'] = 'Wide column'
# sheet.row_dimensions[1].height = 70
# sheet.column_dimensions['B'].width = 20
# wb.save('simension.xlsx')


# 合并和拆分单元格 
# merge_cells ： 合并单元格
# unmerge_cells：拆分单元格



# import openpyxl
# wb = openpyxl.Workbook()
# sheet = wb.active
# sheet.merge_cells('A1:D3')
# sheet['A1'] = 'T.'
# sheet.merge_cells('C5:D5')
# sheet['C5'] = 'dddddddddd'
# wb.save('mer.xlsx')



# import openpyxl
# wb = openpyxl.load_workbook('mer.xlsx') 
# sheet = wb.active
# sheet.unmerge_cells('A1:D3')
# sheet.unmerge_cells('C5:D5')
# wb.save('mer.xlsx')


# 冻结窗格 
# 对于太大而不能一屏显示的电子表格，“冻结”顶部的几行或最左边的几列，是很有帮助的

# import openpyxl
# wb = openpyxl.load_workbook('produceSales.xlsx')
# sheet = wb.active
# sheet.freeze_panes = 'A2'
# wb.save('freeze.xlsx')


# 图表 
# openpyxl 支持利用工作表中单元格的数据，创建条形图、折线图、散点图和饼图。要创建图表，需要做下列事情： 
# 1．从一个矩形区域选择的单元格，创建一个 Reference 对象。 
# 2．通过传入 Reference 对象，创建一个 Series 对象。 
# 3．创建一个 Chart 对象。 
# 4．将 Series 对象添加到 Chart 对象。 
# 5．可选地设置 Chart 对象的 drawing.top、drawing.left、drawing.width 和 drawing.height变量。 
# 6．将 Chart 对象添加到 Worksheet 对象。 

# Reference对象

# 包含图表数据的 Worksheet 对象
# 两个整数的元组，代表矩形选择区域的左上角单元格，该区域包含图表数据：元组中第一个整数是行，第二个整数是列。请注意第一行是 1，不是 0。
#  两个整数的元组，代表矩形选择区域的右下角单元格，该区域包含图表数据：元组中第一个整数是行，第二个整数是列。 

# import openpyxl
# wb = openpyxl.Workbook()
# sheet = wb.active
# for i in range(1, 11):
#     sheet['A' + str(i)] = i
 
# ref = openpyxl.chart.Reference(sheet, min_row = 1, min_col = 1, max_row = 10, max_col = 1)
# series = openpyxl.chart.Series(ref, title = 'First series')
 
# charobj = openpyxl.chart.BarChart()
# charobj.append(series)
# sheet.add_chart(charobj)

# excel_path = Path(__file__).with_name('res.xlsx') 
# wb.save(excel_path)