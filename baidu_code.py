import requests
import csv
from pyquery import PyQuery as pq
from os import listdir
import jieba

from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
base_url = 'https://www.baidu.com/s?wd=%E6%A2%81%E8%8A%B3&pn={}&oq=%E6%A2%81%E8%8A%B3&tn=baiduhome_pg&ie=utf-8&usm=1'
#网页请求初始网址

#header为网页的请求头，防止网站被封
header = {'Accept':'*/*',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7',
'Connection':'keep-alive',
'Cookie':'BAIDUID=13F7D4EB54EE002AB8495C98582EEED9:FG=1; BIDUPSID=13F7D4EB54EE002AB8495C98582EEED9; PSTM=1528978495; BD_UPN=12314753; MCITY=-%3A; BDUSS=hIWHhUSVlLTUQ2aGNhUzlBaE5Rb2wwaE1VZVZsdVlDOWhVUXpLMWNVckZ1UXRjQVFBQUFBJCQAAAAAAAAAAAEAAADEnKGAsKHBwc7etdDLp7ChMQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMUs5FvFLORbRn; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BD_HOME=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; BD_CK_SAM=1; PSINO=2; H_PS_PSSID=1463_25809_21091_20691_28413; H_PS_645EC=e483NitDWSlweRvSPuW5buaXhhcRRUGQDKfFrf5I8odLgpdZSqPon75VkY%2Fn2KrOHKHV; BDSVRTM=156',
'Host':'www.baidu.com',
'is_pbs':'%E6%A2%81%E8%8A%B3',
'is_referer':'https://www.baidu.com/s?wd=%E6%A2%81%E8%8A%B3&rsv_spt=1&rsv_iqid=0xcfe351440008b0db&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=1&oq=%25E5%25A4%25A9%25E5%25A4%25A9%25E5%259F%25BA%25E9%2587%2591%25E7%25BD%2591&rsv_t=4287KaiqCSZQFkHQxan5sAJu0b%2F7L2DPyxmP8jY1%2F2Hk6ttcfFMGUXKUw6HXbOTKXeNo&rsv_pq=c7b32e9b000705af&rsv_sug3=19&rsv_sug1=18&rsv_sug7=101&bs=%E5%A4%A9%E5%A4%A9%E5%9F%BA%E9%87%91%E7%BD%91',
'is_xhr':'1',
'Referer':'https://www.baidu.com/s?wd=%E6%A2%81%E8%8A%B3&pn=10&oq=%E6%A2%81%E8%8A%B3&tn=baiduhome_pg&ie=utf-8&usm=1&rsv_idx=2&rsv_pq=f32a0a0800003c69&rsv_t=e483NitDWSlweRvSPuW5buaXhhcRRUGQDKfFrf5I8odLgpdZSqPon75VkY%2Fn2KrOHKHV',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
'X-Requested-With':'XMLHttpRequest',
}

def get_content():
    for num in range(0,10):#对页数进行循环获取
        print('第{}页正在获取'.format(num))
        page = num*10
        url = base_url.format(page)
        print(url)
        resp = requests.get(url,headers = header).text#使用requests库对网页进行请求
        doc = pq(resp)#利用pyquery库对网页进行解析
        data_list = doc("div#content_left div.result.c-container")#根据标签提取内容
        for item in data_list.items():
            title = item("h3 a").text().strip()#提取
            with open('baidu_result.csv','a',encoding='utf8',newline='') as f:#把获取的数据进行保存
                writer = csv.writer(f)
                writer.writerow((title,))
            print(title)


def get_stop():
    labels = []
    data_adj = ''
    delete_word = []
    corpus = []
    texts = ['\u3000', '\n', ' ','-','_...']#爬取的文本中未处理的特殊字符
    with open('stopWord.txt','r',encoding='utf8') as f:
        '''停用词库的建立'''
        file = f.readlines()
        for item in file:
            texts.append(item.strip())

    '''语料库的建立'''
    read_file = csv.reader(open('baidu_result.csv','r',encoding='utf8'))
    for info in read_file:
        labels.append(info)
        data = jieba.cut(info[0])
        for item in data:
            if item not in texts:
                data_adj += item + ' '
            else:
                delete_word.append(item)
        
            # print(item)#停用词过滤

        corpus.append(data_adj)
    vectorizer = TfidVectorizer()  # 词频向量化并进行TF-IDF预处理 
    tfidf = vectorizer.fit_transform(corpus) # 通过 fit_transform 函数计算各个词语出现的次数
    weight = tfidf.toarray()  # 将tf-idf矩阵抽取出来，可看到词频矩阵的结果
    print(weight)
    word = vectorizer.get_feature_names()  # 可获取词袋中所有文本的关键字
    print(word)

    mykms = KMeans(n_clusters=10)
    y = mykms.fit_predict(weight)
    for i in range(0, 10):
        label_i = []
        for j in range(0, len(y)):
            if y[j] == i:
                label_i.append(labels[j])
        print('梁芳_' + str(i) + ':' + str(label_i))



if __name__ == '__main__':
    get_stop()