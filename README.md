# KG
对于三元组中的实体首先通过实体链接维基百科获取实体描述信息，在经过停用词过滤等预处理后输入BERT模型获得句子级向量表示，然后通过卷积神经网络获取实体描述文本整体向量表示。
# 下载数据集
在[维基百科](https://dumps.wikimedia.org/enwiki/latest)下载enwiki-latest-pages-articles.xml.bz2数据集
# 获取知识图谱三元组实体、关系集
在[三元组实体、关系集](https://github.com/thunlp/DKRL)下载DATA文件，里面含有FB15K、FB20K等文件，下载[映射文件](http://storage.googleapis.com/freebase-public/fb2w.nt.gz)。
# Corpus processing.py
Corpus processing.py是我们进行文件预处理的程序，利用gensim进行数据抽取，获取英文文本txt版，并去除一些杂文和无关语句，输出合适的wiki文本。
# Relationship matching.py
Relationship matching.py是我们用FB15K_description中三元组test集合对wiki文本进行遍历，以用来匹配wiki文本中同时含有头实体和尾实体的句子。
# 1G&959.py
1G&959.py是Relationship matching.py的一个样例，由于匹配完整的文本关系所需时长比较久。为了便于演示，我们取wiki的前1G文件，并且简化FB15K_description中的三元组test集合，去除相同关系的三元组之后，有959个三元组文件。用得到的这个1G和959的三元组文件的头实体和尾实体进行遍历匹配。
# TEST1.xlsx
为了方便计算，我们对其简化FB15K_description中的三元组test.txt，去除相同关系的三元组之后，有959个三元组文件，并对它进行由txt文件转换为xlsx格式，以方便查看。
# 1G&959.xlsx
它是1G&959.py运行的输出文件，第一列是关系，第二列是匹配相对应关系实体的wiki句子数目，后面的列是详细的句子。

