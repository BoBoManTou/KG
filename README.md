# KG
对于三元组中的实体首先通过实体链接维基百科获取实体描述信息，在经过停用词过滤等预处理后输入BERT模型获得句子级向量表示，然后通过卷积神经网络获取实体描述文本整体向量表示。
# 下载数据集
在[维基百科](https://dumps.wikimedia.org/enwiki/latest]下载enwiki-latest-pages-articles.xml.bz2数据集
# Corpus processing.py
Corpus processing.py是我们进行文件预处理的程序，利用gensim进行数据抽取，获取英文文本txt版，并去除一些杂文和无关语句。
