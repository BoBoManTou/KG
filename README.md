# KG
对于三元组中的实体首先通过实体链接维基百科获取实体描述信息，在经过停用词过滤等预处理后输入BERT模型获得句子级向量表示，然后通过卷积神经网络获取实体描述文本整体向量表示。<br>
For the entities in the triples, first obtain the entity description information through the entity link Wikipedia, enter the BERT model after preprocessing such as stop word filtering to obtain the sentence-level vector representation, and then obtain the overall vector representation of the entity description text through. the convolutional neural network .
# 下载数据集
在[维基百科](https://dumps.wikimedia.org/enwiki/latest)下载enwiki-latest-pages-articles.xml.bz2数据集<br>
Download the enwiki-latest-pages-articles.xml.bz2 dataset at [Wikipedia](https://dumps.wikimedia.org/enwiki/latest)

# 获取知识图谱三元组实体、关系集
在[三元组实体、关系集](https://github.com/thunlp/DKRL)下载DATA文件，里面含有FB15K、FB20K等文件，下载[映射文件](http://storage.googleapis.com/freebase-public/fb2w.nt.gz)。<br>
Download the DATA file in [Triple Entity, Relation Set](https://github.com/thunlp/DKRL), which contains FB15K, FB20K and other files, download [mapping file](http://storage.googleapis.com/freebase-public/fb2w.nt.gz).
# Corpus processing.py
Corpus processing.py是我们进行文件预处理的程序，利用gensim进行数据抽取，获取英文文本txt版，并去除一些杂文和无关语句，输出合适的wiki文本。<br>
Corpus processing.py is our file preprocessing program. It uses gensim to extract data, get the txt version of English text, remove some essays and irrelevant sentences, and output appropriate wiki text.
# Relationship matching.py
Relationship matching.py是我们用FB15K_description中三元组test集合对wiki文本进行遍历，以用来匹配wiki文本中同时含有头实体和尾实体的句子。<br>
Relationship matching.py is where we traverse the wiki text with the test set of triples in FB15K_description to match sentences that contain both a head entity and a tail entity in the wiki text.
# 1G&959.py
1G&959.py是Relationship matching.py的一个样例，由于匹配完整的文本关系所需时长比较久。为了便于演示，我们取wiki的前1G文件，并且简化FB15K_description中的三元组test集合，去除相同关系的三元组之后，有959个三元组文件。用得到的这个1G和959的三元组文件的头实体和尾实体进行遍历匹配。1G.txt文件下载地址：链接: [百度云] (https://pan.baidu.com/s/1Xnctz8C0PtL7Skzly8L9_Q) 提取码: myhu<br>
1G&959.py is an example of Relationship matching.py, because it takes a long time to match a complete text relationship. For demonstration purposes, we take the first 1G files of the wiki and simplify the test set of triples in FB15K_description. After removing the triples with the same relationship, there are 959 triple files. Use the head entity and tail entity of the 1G and 959 triple files to traverse and match.link:[Baidu Netdisk](https://pan.baidu.com/s/1Xnctz8C0PtL7Skzly8L9_Q)Extraction code:myhu<br>
# TEST1.xlsx
为了方便计算，我们对其简化FB15K_description中的三元组test.txt，去除相同关系的三元组之后，有959个三元组文件，并对它进行由txt文件转换为xlsx格式，以方便查看。<br>
For the convenience of calculation, we simplify the triplet test.txt in FB15K_description. After removing the triples with the same relationship, there are 959 triples files, and convert them from txt files to xlsx format for easy viewing .
# 1G&959.xlsx
它是1G&959.py运行的输出文件，第一列是关系，第二列是匹配相对应关系实体的wiki句子数目，后面的列是详细的句子。<br>
It is the output file of 1G&959.py. The first column is the relationship, the second column is the number of wiki sentences matching the corresponding relationship entity, and the following column is the detailed sentence.
# 1G&959_Text filter.py
它主要的工作是在词汇层面针对每个关系的文本，进行去除停用词（其中三元组中对应的头实体、尾实体也当作停用词），英文大写转小写，进行词形还原的工作。采用的数据集输入依旧是1G&959.xlsx和TEST1.xlsx。输出是过滤之后的1G&959_Text filter.xlsx的文件。<br>
Its main work is to remove stop words at the vocabulary level for the text of each relationship (the corresponding head entity and tail entity in the triple are also used as stop words), convert English uppercase to lowercase, and perform morphological restoration work. The data set input used is still 1G&959.xlsx and TEST1.xlsx. The output is the filtered 1G&959_Text filter.xlsx file.
# 1G&959_Text filter.xlsx
1G&959_Text filter.py的输出文件。<br>
1G&959_Text filter.py output file.
