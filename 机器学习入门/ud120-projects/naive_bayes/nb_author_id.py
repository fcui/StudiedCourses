#!/usr/bin/python
"""
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project.

    Use a Naive Bayes Classifier to identify emails by their authors

    authors and labels:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

t0 = time()
clf = GaussianNB()
clf.fit(features_train, labels_train)
print('Training time: ', round(time() - t0, 3), 's')
# training time: 3.036s

t1 = time()
pred = clf.predict(features_test)
print('Predicting time: ', round(time() - t1, 3), 's')
print('accuracy score: ', accuracy_score(pred, labels_test))
# predicting time: 0.484s
# print('accuracy score: ', clf.score(features_train, labels_train))
#########################################################
