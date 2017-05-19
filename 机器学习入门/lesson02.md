# 朴素贝叶斯
- 可通过散点图了解数据的基本分布，了解决策面(Decision Surface)。
- 使用高斯贝叶斯(Gaussian Bayes)的[基本流程](http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html)：
```python
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X, Y)
clf.predict(newX)
```
- 完成2.19中的[有关地形数据的高斯NB部署](https://github.com/fcui/StudiedCourses/tree/master/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%85%A5%E9%97%A8/gaussian_naive_bayes)，已按照python 3做了修改，但原程序`class_vis.py`中的最后一句还是有点问题，不影响使用。
