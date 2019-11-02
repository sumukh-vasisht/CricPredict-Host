from flask import Flask, request, render_template, redirect, url_for
import os
import pandas as pd
import numpy as np
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

app = Flask(__name__)

teams = ["",""]
arr=[]
features=[]
classLabelX=[]
maxValue=''

def setPath(arr):
    t1=teams[0]
    t2=teams[1]
    tt1=t1[:3]
    tt2=t2[:3]
    t=[]
    t.append(tt1)
    t.append(tt2)
    t.sort()
    tt1=t[0]
    tt1=tt1[:3]
    tt2=t[1]
    tt2=tt2[:3]
    path="./dataAnalytics/Matches/"+tt1+tt2+".txt"

    try:
        f=open(path,"r")
    except:
        winnerMessage="Invalid teams selected!"
        return winnerMessage
    print("File OPEN")
    # a=f.readline()
    arr1=[int(s) for s in f.readline().split()]
    arr2=[int(s) for s in f.readline().split()]
    arr3=[int(s) for s in f.readline().split()]
    arr4=[int(s) for s in f.readline().split()]
    arr5=[int(s) for s in f.readline().split()]
    arr6=[float(s) for s in f.readline().split()]
    for i in range(len(arr6)):
        arr6[i]=round(arr6[i],2)
    
    features=np.array([arr1,arr3,arr4,arr5,arr6])
    features=features.transpose()
    arr2t=np.array(arr2)
    arr2t=arr2t.transpose()
    classLabelX=np.array(arr2t)

    print(features)
    print(classLabelX)
    classLabelX=classLabelX.astype(np.int8)
    print(np.unique(classLabelX))

    # clf=SVC(gamma='auto')
    # clf.fit(features,classLabelX)

    try:
        clf=SVC(gamma='auto')
        clf.fit(features,classLabelX)
    except:
        classLabelX[0]=-1
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

    total=len(arr2)

    countDt=0
    for i in range(len(arr2)):
        if arr2[i]==predDt[i]:
            countDt+=1

    countRf=0
    for i in range(len(arr2)):
        if arr2[i]==predRf[i]:
            countRf+=1

    countAb=0
    for i in range(len(arr2)):
        if arr2[i]==predAb[i]:
            countAb+=1

    countGlb=0
    for i in range(len(arr2)):
        if arr2[i]==predGlb[i]:
            countGlb+=1

    data = {
        'dt' : countDt,
        'rf' : countRf,
        'ab' : countAb,
        'glb' : countGlb 
    }
    maxValue = max(data,key=data.get)

    print(maxValue)

    print("---------------")

    print(arr)

    print("---------------")

    if maxValue=='ab':
        finalPred=clfAdaBoost.predict(arr)
    elif maxValue=='dt':
        finalPred=clfDecisionTree.predict(arr)
    elif maxValue=='rf':
        finalPred=clfRandomForest.predict(arr)
    else:
        finalPred=clfGaussian.predict(arr)
    # print(finalPred[0])
    winner=""
    if finalPred[0]==1:
        winner=teams[1]
    elif finalPred[0]==-1:
        winner=teams[0]
    else:
        winner="Draw"
    if winner!="Draw":
        winnerMessage="Final Prediction : "+winner+" will win!"
    else:
        winnerMessage="It'll be a Draw!"
    return winnerMessage

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=="POST":
        global team1, team2
        teams[0] = request.form['team1']
        teams[1] = request.form['team2']
        # setPath()
        return redirect(url_for('predicc'))
    return render_template("index.html")


@app.route('/predicc', methods=['GET','POST'])
def predicc():
    if request.method=="POST":
        venue=request.form['venue']
        tossWinner=request.form['tossWinner']
        tossDecision=request.form['tossDecision']
        if venue==teams[0]:
            venue=-1
        elif venue==teams[1]:
            venue=1
        else:
            venue=0
        if tossWinner==teams[0]:
            tossWinner=-1
        else:
            tossWinner=1
        if tossDecision=='bat':
            tossDecision=-1
        else:
            tossDecision=1
        arr=np.array([[venue,tossWinner,tossDecision,int(0),int(0)]])
        message=setPath(arr)
        return render_template("result.html", confirm=message)
    return render_template("predicc.html", teams = teams)

@app.route('/result', methods=['GET','POST'])
def result():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)