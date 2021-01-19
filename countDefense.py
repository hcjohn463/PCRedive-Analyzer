import pandas as pd
from princessClass import *

def getDefenseTime(selectData,nameList):

    #setting level and class
    level = 172
    char1,char2,char3,char4,char5 = None,None,None,None,None
    objList = [char1,char2,char3,char4,char5]
    for i in range(len(nameList)):
        if nameList[i] == 'レイ':
            #level,skillComponet,skillHitTime,upSkillComponent,upSkillHitTime,skill,ubComponent.ubHitTime
            objList[i] = Special(level,0.6,12,1.2,24,'技能1：ウィンドスラスト',0,18)
        elif nameList[i] == 'クリスティーナ':
            #level,skillComponet,skillHitTime,skill,ubComponent.ubHitTime  
            objList[i] = General(level,0.6,12,'技能2：インジェクション',0,0)
        elif nameList[i] == 'シズル（バレンタイン）':
            objList[i] = Special(level,0.15,12,0.25,12,'技能1：ウィンドスラスト',0,16)
        elif nameList[i] == 'マコト':
            objList[i] = General(level,0.8,12,'技能2：ブレイブハウリング',0.9,18)
        else:
            objList[i] = Character(level)

    #count defense time
    countList = [0]
    count = 0
    for j in range(1,selectData.shape[1]):
        for i in range(selectData.shape[0]):
            count += objList[i].checkSkill(selectData.loc[i][j])
        for obj in objList:
            count -= obj.checkSkillHit()
            count -= obj.checkUbHit()
        countList.append(count)
    timeList = selectData.columns.tolist()
    timeList = timeList[1:]
    countList = countList[1:]

    return countList