# KG
对于三元组中的实体首先通过实体链接维基百科获取实体描述信息，在经过停用词过滤等预处理后输入BERT模型获得句子级向量表示，然后通过卷积神经网络获取实体描述文本整体向量表示。

# 下载数据集
在[维基百科](https://dumps.wikimedia.org/enwiki/latest)下载enwiki-latest-pages-articles.xml.bz2数据集

# 获取知识图谱三元组实体、关系集
在[三元组实体、关系集](https://github.com/thunlp/DKRL)下载DATA文件，里面含有FB15K、FB20K等文件。[映射文件](http://storage.googleapis.com/freebase-public/fb2w.nt.gz)

# Corpus processing.py
Corpus processing.py是我们进行文件预处理的程序，利用gensim进行数据抽取，获取英文文本txt版，并去除一些杂文和无关语句，输出合适的wiki文本。

# Relationship matching.py
Relationship matching.py是我们用FB15K_description中三元组test集合对wiki文本进行遍历，以用来匹配wiki文本中同时含有头实体和尾实体的句子。

# 1G&959.py
1G&959.py是Relationship matching.py的一个样例，取wiki的前1G文件。对FB15K中的test文件去除相同关系的三元组之后，有959个三元组文件。用得到的这个1G和959的三元组文件的头实体和尾实体进行遍历匹配。

