import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

def customAccuracy(yTest, yPred, threshold):
    count=0
    length=len(yPred)
    for i in range(length):
        if(abs(yPred[i]-yTest[i]) <= threshold):
            count += 1
    return ((count/length)*100)

# Importing the dataset
# import pandas as pd
dataSet = pd.read_csv('Data-allMatches/odi.csv')
x = dataSet.iloc[:,[7,8,9,12,13]].values
y = dataSet.iloc[:, 14].values

#Split train and test set
#from sklearn.model_selection import train_test_split
xTrain, xTest, yTrain, yTest = train_test_split(x,y,test_size=0.25, random_state=0)

#Feature Scaling - used to normalize the range of independent variables of features of data
#from sklearn.preprocessing import StandardScaler
StandardScaler=StandardScaler()
xTrain=StandardScaler.fit_transform(xTrain)
xTest=StandardScaler.transform(xTest)

#Train
# from sklearn.ensemble import RandomForestRegressor
regressor=RandomForestRegressor()
regressor.fit(xTrain,yTrain)

#Testing on trained model
yPred=regressor.predict(xTest)
score=regressor.score(xTest,yTest)*100
# print("-----------------")
print("R Square Value : ", score)
print("Custom accuracy : ", customAccuracy(yTest, yPred, 20))
# print("-----------------")

#Testing with custom input
# newPrediction=regressor.predict(StandardScaler.transform(np.array([[100,0,13,50,50]])))
# print("Prediction Score : ", newPrediction)