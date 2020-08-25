from gensim.corpora.wikicorpus import extract_pages,filter_wiki
import bz2file
import re
import codecs

from tqdm import tqdm
import codecs
wiki = extract_pages(bz2file.open('enwiki-latest-pages-articles.xml.bz2'))
#对 enwiki-latest-pages-articles.xml.bz2 文件进行解压并且读取内容，输出为wiki.txt
def wiki_replace(d):
    s = d[1]
    s = re.sub(':*{\|[\s\S]*?\|}', '', s)
    s = re.sub('<gallery>[\s\S]*?</gallery>', '', s)
    s = re.sub('(.){{([^{}\n]*?\|[^{}\n]*?)}}', '\\1[[\\2]]', s)
    s = filter_wiki(s)
    s = re.sub('\* *\n|\'{2,}', '', s)
    s = re.sub('\n+', '\n', s)
    s = re.sub('\n[:;]|\n +', '\n', s)
    s = re.sub('\n==', '\n\n==', s)
    s = u'【' + d[0] + u'】\n' + s
    return s.strip()

i = 0
f = codecs.open('wiki.txt', 'w', encoding='utf-8')
w = tqdm(wiki, desc=u'已获取0篇文章')
for d in w:
    if not re.findall('^[a-zA-Z]+:', d[0]) and d[0] and not re.findall(u'^#', d[1]):
        s = wiki_replace(d)
        f.write(s+'\n\n\n')
        i += 1
        if i % 100 == 0:
            w.set_description(u'已获取%s篇文章'%i)

f.close()

#去除wiki文件中的标题等无用的字符，输出到new-wiki.txt
file = open("wiki.txt",encoding='utf-8')
f = codecs.open('new-wiki.txt', 'w', encoding='utf-8')
for line in file:
  a = re.sub(u"\\(.*?\\)|\\{.*?}|\\[.*?]|\\====.*?====|\\===.*?===|\\==.*?==|\\【.*?】", "", line)
  f.write(a)
f.close()



#一句话为一行，输出到new2-wiki.txt
def cut_sentences(content):
    # 结束符号
    end_flag = ['?', '!', '.', '？', '！', '。', '…']
    content_len = len(content)
    sentences = []
    tmp_char = ''
    for idx, char in enumerate(content):
        # 拼接字符
        tmp_char += char
        # 判断是否已经到了最后一位
        if (idx + 1) == content_len:
            sentences.append(tmp_char)
            break
        # 判断此字符是否为结束符号
        if char in end_flag:
            # 再判断下一个字符是否为结束符号，如果不是结束符号，则切分句子
            next_idx = idx + 1
            if not content[next_idx] in end_flag:
                sentences.append(tmp_char)
                tmp_char = ''
    return sentences


f = codecs.open('new2-wiki.txt', 'w', encoding='utf-8')
for line in  tqdm(open("new-wiki.txt", "r", encoding="utf-8") ):
    sentences = cut_sentences(line)
    a='\n'.join(sentences)
    f.write(a)
f.close()