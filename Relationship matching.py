
import xlrd
import xlsxwriter  # 导入模块
from tqdm import tqdm
workBook = xlrd.open_workbook('TEST.xlsx');    #查找数据集
sheet1_content1 = workBook.sheet_by_index(0);  # sheet索引从0开始
workbook = xlsxwriter.Workbook('new_excel.xlsx')  # 结果存放数据集
sheet = workbook.add_worksheet('sheet1')  # 新建sheet（sheet的名称为"sheet1"）
col = 0
row = -1
for R in tqdm(range(57289)):
    if sheet1_content1.cell(R, 3).value == 0:
        for line in open("new2-wiki.txt", "r", encoding="utf-8"):
            list = line.split()
            if sheet1_content1.cell(R, 0).value in list and sheet1_content1.cell(R, 1).value in list:
                sum = sum + 1
                sheet.write(col+2, row, line)  # 输出第一次关系出现的那一行
                col = col + 1
                sheet.write(1, row, sum)
    else:
        sum = 0
        col=0
        row=row+1
        sheet.write(0, row, sheet1_content1.cell(R, 2).value)
        for line in open("new2-wiki.txt", "r", encoding="utf-8"):
            list = line.split()
            if sheet1_content1.cell(R, 0).value in list and sheet1_content1.cell(R, 1).value in list:
                sum=sum+1
                sheet.write(col+2, row, line)  # 输出和row tip在同一行
                col = col + 1
                sheet.write(1, row, sum)
workbook.close()  # 将excel文件保存关闭，如果没有这一行运行代码会报错
