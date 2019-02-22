# intro


<p>
reference：<br>
https://blog.csdn.net/u012249992/article/details/79525396<br>
https://blog.csdn.net/github_36326955/article/details/54891204<br>
<p>
关于tf-idf权值<br>
https://www.cnblogs.com/likai198981/p/3344060.html<br>
https://blog.csdn.net/hyman_yx/article/details/51745920<br>
</p>
<p>
文本特征提取：将文本数据转化成特征向量的过程，比较常用的文本特征表示法为词袋法

什么是词袋：<br>
1.不考虑词语出现的顺序<br>
2.每个出现过的词汇单独作为一列特征<br>
3.这些不重复的特征词汇集合为词表<br>
4.每一个文本都可以在很长的词表上统计出一个很多列的特征向量，如果每个文本都出现的词汇，一般被标记为 停用词 不计入特征向量<br>

主要有两个api来实现 CountVectorizer 和 TfidfVectorizer

CountVectorizer：

    只考虑词汇在文本中出现的频率
TfidfVectorizer：

    除了考量某词汇在文本出现的频率，还关注包含这个词汇的所有文本的数量

    能够削减高频没有意义的词汇出现带来的影响, 挖掘更有意义的特征

具体例子：https://www.cnblogs.com/Lin-Yi/p/8974108.html
</p>
</p>
