import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

def customAccuracy(yTest, yPred, threshold):
    count=0
    length=len(yPred)
    for i in range(length):
        if(abs(yPred[i]-yTest[i]) <= threshold):
            count += 1
    return ((count/length)*100)

#Import the dataset
dataSet = pd.read_csv('Data-allMatches/odi.csv')
x = dataSet.iloc[:,[7,8,9,12,13]].values #iloc is used to select and index rows and columns from Pandas dataframes
y = dataSet.iloc[:,14].values
# print(x)
# print(y)

#Split train and test set
#from sklearn.model_selection import train_test_split
xTrain, xTest, yTrain, yTest = train_test_split(x,y,test_size=0.25, random_state=0)

#Feature Scaling - used to normalize the range of independent variables of features of data
#from sklearn.preprocessing import StandardScaler
StandardScaler=StandardScaler()
xTrain=StandardScaler.fit_transform(xTrain)
xTest=StandardScaler.transform(xTest)

#Train
#from sklearn.linear_model import LinearRegression
linearRegression=LinearRegression()
linearRegression.fit(xTrain,yTrain)

#Test on trained model
yPred=linearRegression.predict(xTest)
score=linearRegression.score(xTest,yTest)*100
# print("-----------------")
print("R Square Value : ", score)
print("Custom accuracy : ", customAccuracy(yTest, yPred,20))
# print("-----------------")

#Test with custom input
# newPrediction = linearRegression.predict(StandardScaler.transform(np.array([[100,0,13,50,50]])))
# print("Prediction score : ", newPrediction)
