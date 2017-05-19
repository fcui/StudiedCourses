# 朴素贝叶斯
- 可通过散点图了解数据的基本分布，了解决策面(Decision Surface)；
- 使用高斯贝叶斯(Gaussian Bayes)的[基本流程](http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html)：
```python
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X, Y)
clf.predict(newX)
```
- 完成2.19中的[有关地形数据的高斯NB部署]()
