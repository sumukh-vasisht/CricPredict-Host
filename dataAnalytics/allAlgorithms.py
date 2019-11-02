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

arr1=[]
arr2=[]
arr3=[]
arr4=[]
arr5=[]
arr6=[]

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

print("arr1 : ",arr1)
print("arr2 : ",arr2)
print("arr3 : ",arr3)
print("arr4 : ",arr4)
print("arr5 : ",arr5)
print("arr6 : ",arr6)

features=np.array([arr1,arr3,arr4,arr5,arr6])
features=features.transpose()
arr2t=np.array(arr2)
arr2t=arr2t.transpose()
print(features)
print(arr2t)
# features.reshape
classLabelX=arr2t

clf=SVC(gamma='auto')
clf.fit(features,classLabelX)

clfDecisionTree=tree.DecisionTreeClassifier(max_depth=5)
clfDecisionTree.fit(features,classLabelX)

clfRandomForest=RandomForestClassifier(n_estimators=100,max_depth=2,random_state=0)
clfRandomForest.fit(features,classLabelX)

clfAdaBoost=AdaBoostClassifier(tree.DecisionTreeClassifier(max_depth=1),algorithm="SAMME",n_estimators=200)
clfAdaBoost.fit(features,classLabelX)

clfLinear=SGDClassifier()
clfLinear.fit(features,classLabelX)

clfGaussian=GaussianNB()
clfGaussian.fit(features,classLabelX)

pred=clf.predict(features)
predDt=clfDecisionTree.predict(features)
predRf=clfRandomForest.predict(features)
predAb=clfAdaBoost.predict(features)
predLn=clfLinear.predict(features)
predGlb=clfGaussian.predict(features)

print('Decision Tree Predictions : ', predDt)
print('Random Forest Predictions : ', predRf)
print('Adaboost Predictions : ', predAb)
print('Naive Bayes Classifier : ', predGlb)

total=len(arr2)
print("Total : ",total)

count=0
for i in range(len(arr2)):
    if arr2[i]==predDt[i]:
        count+=1
print("-----------------")
print("Decision Tree : ",count)
print("Decision Tree Accuracy : ",(count/total)*100)
print("--------------------------")

count=0
for i in range(len(arr2)):
    if arr2[i]==predRf[i]:
        count+=1
print("-----------------")
print("Random Forest : ",count)
print("Random Forest Accuracy : ",(count/total)*100)
print("--------------------------")

count=0
for i in range(len(arr2)):
    if arr2[i]==predAb[i]:
        count+=1
print("-----------------")
print("Adaptive Boost : ",count)
print("Adaptive Boost Accuracy : ",(count/total)*100)
print("--------------------------")

count=0
for i in range(len(arr2)):
    if arr2[i]==predGlb[i]:
        count+=1
print("-----------------")
print("Gaussian Naive Bayes : ",count)
print("Gaussian Naive Bayes Accuracy : ",(count/total)*100)
print("--------------------------")


# team1=input("Enter Team 1 : ")
# team2=input("Enter Team 2 : ")
# venue=input("Enter Venue : ")
# venueInt=0
# if venue==team1:
#     venueInt=-1
# elif venue==team2:
#     venueInt=1
# tossWinner=input("Enter Toss Winner : ")
# tWinner=0
# if tossWinner==team1:
#     tWinner=-1
# else:
#     tWinner=1
# tossDecision=input("Enter Toss Decision : ")
# tDecision=0
# if tossDecision=='bat':
#     tDecision=-1
# else:
#     tDecision=1
# arr=np.array([[venueInt,tWinner,tDecision,int(0),int(0)]])
# # arr=arr.transpose()
# # arrZeroes=array([int(0),int(0),int(0),int(0),int(0)])
# # print(arr.shape)
# # arr.reshape(1,-1)
# # print(arr.shape)
# finalPred=clfAdaBoost.predict(arr)
# print("Final Prediction : ",finalPred)


