# Referances＋学习笔记
整体实现参考：
https://blog.csdn.net/weixin_41276745/article/details/79611259
<p>
关于tf-idf权值<br>
https://www.cnblogs.com/likai198981/p/3344060.html<br>
https://blog.csdn.net/hyman_yx/article/details/51745920<br>
</p>
<p>
文本特征提取：将文本数据转化成特征向量的过程，比较常用的文本特征表示法为词袋法

#什么是词袋：<br>
1.不考虑词语出现的顺序<br>
2.每个出现过的词汇单独作为一列特征<br>
3.这些不重复的特征词汇集合为词表<br>
4.每一个文本都可以在很长的词表上统计出一个很多列的特征向量，如果每个文本都出现的词汇，一般被标记为 停用词 不计入特征向量<br>
<p>
#词袋模型：<br>
    词袋模型假设我们不考虑文本中词与词之间的上下文关系，仅仅只考虑所有词的权重。而权重与词在文本中出现的频率有关。
    词袋模型首先会进行分词，在分词之后，通过统计每个词在文本中出现的次数，我们就可以得到该文本基于词的特征，如果将各个文本样本的这些词与对应的词频放在一起，就是我们常说的向量化。向量化完毕后一般也会使用 TF-IDF 进行特征的权重修正，再将特征进行标准化。
</p>
<p>
#具体步骤：<br>
    1.词频向量化<br>
    CountVectorizer 类会将文本中的词语转换为词频矩阵，例如矩阵中包含一个元素a[i][j]，它表示j词在i类文本下的词频。它通过 fit_transform 函数计算各个词语出现的次数，通过get_feature_names()可获取词袋中所有文本的关键字，通过 toarray()可看到词频矩阵的结果。<br>
    2.用sklearn进行TF-IDF预处理<br>
    第一种方法是在用 CountVectorizer 类向量化之后再调用 TfidfTransformer 类进行预处理。第二种方法是直接用 TfidfVectorizer 完成向量化与 TF-IDF 预处理。<br>
    3.代码参考：https://blog.csdn.net/m0_37324740/article/details/79411651<br>
</p>

CountVectorizer：

    只考虑词汇在文本中出现的频率
TfidfVectorizer：

    除了考量某词汇在文本出现的频率，还关注包含这个词汇的所有文本的数量

    能够削减高频没有意义的词汇出现带来的影响, 挖掘更有意义的特征

具体例子：https://www.cnblogs.com/Lin-Yi/p/8974108.html
</p>
</p>
