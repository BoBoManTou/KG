import re

from nltk import word_tokenize, pos_tag
from nltk.book import *
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import xlrd
import xlsxwriter  # 导入模块
from tqdm import tqdm
workBook = xlrd.open_workbook('1G&959.xlsx');    #查找数据集
sheet1_content1 = workBook.sheet_by_index(0);  # sheet索引从0开始
workBook2 = xlrd.open_workbook('TEST1.xlsx');    #查找数据集
sheet1_content2 = workBook2.sheet_by_index(0);  # sheet索引从0开始

workbook = xlsxwriter.Workbook('1G&959_Text filter.xlsx')  # 结果存放数据集
sheet = workbook.add_worksheet('sheet1')  # 新建sheet（sheet的名称为"sheet1"）
row = 0

set(stopwords.words('english'))
stop_words = set(stopwords.words('english'))  #停用词集合


# 获取单词的词性函数
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None


for R in tqdm(range(959)):
    sum = 0
    col= 0
    if sheet1_content1.cell(R, 1).value ==0:
        sheet.write(R,0, sheet1_content1.cell(R, 0).value)
        sheet.write(R,1, sheet1_content1.cell(R, 1).value)
        continue
    else:
        sheet.write(R, 0, sheet1_content1.cell(R, 0).value)
        sheet.write(R, 1, sheet1_content1.cell(R, 1).value)
        for i in range(int(sheet1_content1.cell(R, 1).value)):
            #去除头实体和尾实体
            text= sheet1_content1.cell(R, i+2).value
            A=sheet1_content2.cell(R, 0).value
            B=sheet1_content2.cell(R, 1).value
            text = re.sub(A, "", text)
            text = re.sub(B, "", text)
            text = line = str.lower(text)    #大写转换小写
            word_tokens = word_tokenize(text) #分词
            #进行去除停用词语
            filtered_sentence = []
            for w in word_tokens:
                if w not in stop_words:
                    filtered_sentence.append(w)
            text=" ".join(filtered_sentence)
            #进行词性还原
            tokens = word_tokenize(text)  # 分词
            tagged_sent = pos_tag(tokens)  # 获取单词词性
            wnl = WordNetLemmatizer()
            lemmas_sent = []
            for tag in tagged_sent:
                wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN
                lemmas_sent.append(wnl.lemmatize(tag[0], pos=wordnet_pos))  # 词形还原
                text = " ".join(lemmas_sent)
            sheet.write(R, i+2, text)
workbook.close()  # 将excel文件保存关闭，如果没有这一行运行代码会报错





