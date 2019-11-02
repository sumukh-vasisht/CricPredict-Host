import pandas as pd
import numpy as np
import os
import random
import yaml as y
import tensorflow as tf
from sklearn.svm import SVC
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import GaussianNB
from keras.models import Sequential
from keras.layers import Dense

f=open("./Matches/IndPak.txt","r")
# a=f.readline()
arr1=[int(s) for s in f.readline().split()]
arr2=[int(s) for s in f.readline().split()]
arr3=[int(s) for s in f.readline().split()]
arr4=[int(s) for s in f.readline().split()]
arr5=[int(s) for s in f.readline().split()]
arr6=[float(s) for s in f.readline().split()]
for i in range(len(arr6)):
    arr6[i]=round(arr6[i],2)

# print("arr1 : ",arr1)
# print("arr2 : ",arr2)
# print("arr3 : ",arr3)
# print("arr4 : ",arr4)
# print("arr5 : ",arr5)
# print("arr6 : ",arr6)

features=np.array([arr1,arr3,arr4,arr5,arr6])
features=features.transpose()
arr2t=np.array(arr2)
arr2t=arr2t.transpose()
# print(features)
# print(arr2t)
# features.reshape
classLabelX=arr2t

clf=SVC(gamma='auto')
clf.fit(features,classLabelX)

clfGaussian=GaussianNB()
clfGaussian.fit(features,classLabelX)

pred=clf.predict(features)
predGlb=clfGaussian.predict(features)

# print('Naive Bayes Classifier : ', predGlb)

total=len(arr2)
# print("Total : ",total)

count=0
for i in range(len(arr2)):
    if arr2[i]==predGlb[i]:
        count+=1
print("Gaussian Naive Bayes accurate predictions : ",count,"/",total)
print("Gaussian Naive Bayes Accuracy : ",(count/total)*100)
# print("--------------------------")