import pandas as pd
from princessClass import *

def getDefenseTime(level,selectData,nameList):
    
    data = pd.read_csv('./data/defense_0125.csv')

    defenseDict = {}
    for i in range(data.shape[0]):
        value = []
        for j in range(1,data.shape[1]):
            value.append(data.loc[i][j])
        defenseDict[data.loc[i]['Name']] = value

    char1,char2,char3,char4,char5 = None,None,None,None,None
    objList = [char1,char2,char3,char4,char5]
    for i in range(len(nameList)):
        if nameList[i] in defenseDict:
            objList[i] = Characters(level,defenseDict[nameList[i]])
        else:
            objList[i] = Characters(level)

    #count defense time
    countList = [0]
    count = 0
    for j in range(1,selectData.shape[1]):
        for obj in objList:
            count -= obj.checkHit()
        for i in range(selectData.shape[0]):
            count += objList[i].checkSkill(selectData.loc[i][j])
        countList.append(count)
    timeList = selectData.columns.tolist()
    timeList = timeList[1:]
    countList = countList[1:]

    return countList
