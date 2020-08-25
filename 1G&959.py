import xlrd
import xlsxwriter  # 导入模块
from tqdm import tqdm
workBook = xlrd.open_workbook('TEST1.xlsx');    #查找数据集
sheet1_content1 = workBook.sheet_by_index(0);  # sheet索引从0开始
workbook = xlsxwriter.Workbook('1G&959.xlsx')  # 结果存放数据集
sheet = workbook.add_worksheet('sheet1')  # 新建sheet（sheet的名称为"sheet1"）
row = 0
for R in tqdm(range(959)):
    sum = 0
    col= 0
    sheet.write(row,0,  sheet1_content1.cell(R, 2).value)
    for line in open("1G.txt", "r", encoding="utf-8"):
        list = line.split()

        if sheet1_content1.cell(R, 0).value in list and sheet1_content1.cell(R, 1).value in list:
            sum=sum+1
            col = col + 1
            sheet.write(row,col+1,  line)  # 输出和row tip在同一行
    sheet.write(row,1,  sum)   #计数
    row = row + 1
workbook.close()  # 将excel文件保存关闭，如果没有这一行运行代码会报错
