# 朴素贝叶斯(Naive Bayes)
- 可通过散点图了解数据的基本分布，了解决策面(Decision Surface)。
- 使用高斯贝叶斯(Gaussian Bayes)的[基本流程](http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html)：
```python
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X, Y)
clf.predict(newX)
```
- 完成2.19中的练习[有关地形数据的高斯NB部署](https://github.com/fcui/StudiedCourses/blob/master/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%85%A5%E9%97%A8/gaussian_naive_bayes/ClassifyNB.py)，已按照python 3做了修改，但原程序`class_vis.py`中的最后一句还是有点问题，不影响使用。
- 完成2.20中的练习[计算 NB 准确性](https://github.com/fcui/StudiedCourses/blob/master/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%85%A5%E9%97%A8/gaussian_naive_bayes/classify.py)，直接利用到的分类器计算准确度
```python
accuracy = clf.score(features_test, labels_test)
```
或调用`accuracy_score`来计算分类的准确度：
```python
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred, labels_test)
```
- 关于贝叶斯，可以查看两篇博文：[贝叶斯推断](http://www.ruanyifeng.com/blog/2011/08/bayesian_inference_part_one.html)和[如何使用贝叶斯推断过滤垃圾邮件](http://www.ruanyifeng.com/blog/2011/08/bayesian_inference_part_two.html)。
- 
