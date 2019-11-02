import pandas as pd
import numpy as np
import yaml
import csv
import os
import glob

venueList=[]
venueFactorList=[]
team1List=[]
team2List=[]
tipeList=[]
marginList=[]
winnerList=[]
tossWinner=[]
tossDecision=[]

with open('stadiums.csv','rt')as fi:
    data1 = csv.reader(fi)
    for row in data1:
            venueList.append(row)

TEAM1=input("Enter Team 1 : ")
TEAM2=input("Enter Team 2 : ")

path = 'Teams/'+TEAM1+'/*.yaml'
files=glob.glob(path)
for file in files:

    # with open(path+"/filename",'r') as f:
    #     docs = yaml.load_all(f, Loader=yaml.FullLoader)
    #     print("Opened")
    #     for doc in docs:
    #         for k,v in doc.items():
    #             if(k=='info'):
    #                 a=v

    if file.endswith(".yaml"):
        print("File open")
        try:
            with open(file,'r') as f:
                docs=yaml.load_all(f,Loader=yaml.FullLoader)
                for doc in docs:
                    for k,v in doc.items():
                        if(k=='info'):
                            a=v

            # winner = a['outcome']['winner']
            # margin = a['outcome']['by']
            # for k,v in margin.items():
            #     tipe=k
            #     margins=v
                
            # for key,value in a.items():
            #     if(key=='city'):
            #         city=value
            #     if(key=='teams'):
            #         teams=value

            # team1=teams[0]
            # team2=teams[1]

            print("Teams are : ")
            print(a['teams'])

            if(TEAM2 in a['teams']):

                print("Entered")

                winner = a['outcome']['winner']
                if winner==TEAM1:
                    winner=-1
                elif winner==TEAM2:
                    winner=1
                else:
                    winner=0
                tWinner= a['toss']['winner']
                if tWinner==TEAM1:
                    tWinner=-1
                else:
                    tWinner=1
                tDecision=a['toss']['decision']
                if tDecision=="bat":
                    tDecision=-1
                else:
                    tDecision=1
                margin = a['outcome']['by']
                for k,v in margin.items():
                    tipe=k
                    margins=v
                    if tipe=='runs':
                        tipe=1
                        margins=margins/300
                    elif tipe=='wickets':
                        tipe=-1
                        margins=(0-(margins/10))
                
                for key,value in a.items():
                    if(key=='city'):
                        city=value
                    if(key=='teams'):
                        teams=value

                team1=teams[0]
                team2=teams[1]

                for i in range(len(venueList)):
                    if(venueList[i][0]==city):
                        if(venueList[i][1]==team1):
                            venueFactor=-1
                        elif(venueList[i][1]==team2):
                            venueFactor=1
                        else:
                            venueFactor=0
                print("-----------------------------")
                print('Team 1 : ',end=" ")
                print(team1)
                print('Team 2 : ',end=" ")
                print(team2)
                print('Venue : ',end=" ")
                print(city)
                print('Venue Factor : ',end=" ")
                print(venueFactor)
                print("Winner : ",end="")
                print(winner)
                print("Toss Winner : ",end="")
                print(tWinner)
                print("Toss Decision : ",end="")
                print(tDecision)
                print("Margin : ",end="")
                print("By ",margins,tipe)
                team1List.append(team1)
                team2List.append(team2)
                venueFactorList.append(str(venueFactor))
                winnerList.append(str(winner))
                tossWinner.append(str(tWinner))
                tossDecision.append(str(tDecision))
                tipeList.append(str(tipe))
                marginList.append(str(margins))
        except:
            pass

# print(team1List)
# print(team2List)
print(venueFactorList)
print(winnerList)
print(tossWinner)
print(tossDecision)
print(tipeList)
print(marginList)

teamOne=TEAM1[:3]
teamTwo=TEAM2[:3]
fileName="Matches/"+teamOne+teamTwo+".txt"
print(fileName)

strVenueFactorList=""
strWinnerList=""
strTossWinnerList=""
strTossDecisionList=""
strTipeList=""
strMarginList=""

strVenueFactorList=' '.join([str(ele) for ele in venueFactorList])
strWinnerList=' '.join([str(ele) for ele in winnerList])
strTossWinnerList=' '.join([str(ele) for ele in tossWinner])
strTossDecisionList=' '.join([str(ele) for ele in tossDecision])
strTipeList=' '.join([str(ele) for ele in tipeList])
strMarginList=' '.join([str(ele) for ele in marginList])


# fileToBeWritten=open(fileName,"w+")
# fileToBeWritten.write(strVenueFactorList)
# fileToBeWritten.write(strWinnerList)
# fileToBeWritten.write(strTipeList)
# fileToBeWritten.write(strMarginList)
# fileToBeWritten.close()

print(strVenueFactorList)
print(strMarginList)
print(strTipeList)
print(strWinnerList)
print(strTossWinnerList)
print(strTossDecisionList)

with open(fileName,'w+') as fileToBeWritten:
    fileToBeWritten.write(strVenueFactorList+'\n')
    fileToBeWritten.write(strWinnerList+'\n')
    fileToBeWritten.write(strTossWinnerList+'\n')
    fileToBeWritten.write(strTossDecisionList+'\n')
    fileToBeWritten.write(strTipeList+'\n')
    fileToBeWritten.write(strMarginList+'\n')
    fileToBeWritten.close()