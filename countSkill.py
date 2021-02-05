import pandas as pd
def getSkillTime(selectData,nameList):

	#skill name and time
    selectDict = {}
    noList = [0,'0','普通攻击']
    for i in range(selectData.shape[0]):
        selectDict[nameList[i]] = list()
        for j in range(1,selectData.shape[1]):
            if selectData.loc[i][j] not in noList:
                skill = selectData.loc[i][j]
                time = selectData.columns[j]
                selectDict[nameList[i]].append([skill,time])

    timeDict = {}
    for i, (key, value) in enumerate(selectDict.items()):
        timeDict[nameList[i]] = list()
        skills1 = []
        skills2 = []
        ubs = []
        for j in range(len(value)):
            if value[j][0][-2:] == 'UB':
                ubs.append(value[j][1])
            elif value[j][0][:3] == '技能1':
                skills1.append(value[j][1])
            else:
                skills2.append(value[j][1])
        timeDict[nameList[i]].append(skills1)
        timeDict[nameList[i]].append(skills2)
        timeDict[nameList[i]].append(ubs)

    #change to decimal time
    for i, (key, value) in enumerate(timeDict.items()):
        for j in range(len(value)):
            for k in range(len(value[j])):
                value[j][k] = int(value[j][k].split(':')[0]) * 60 + int(value[j][k].split(':')[1])


    gntTimeList = []
    for i, (key, value) in enumerate(timeDict.items()):
        gntTimeList.append(value)


    #預設技能經過時間 1秒
    for i in range(len(gntTimeList)):
        for j in range(len(gntTimeList[i])):
            for k in range(len(gntTimeList[i][j])):
                gntTimeList[i][j][k] = (gntTimeList[i][j][k],-1)

    return gntTimeList





    #Only skill time



    # timeDict = {}
    # for i, (key, value) in enumerate(selectDict.items()):
    #     timeDict[nameList[i]] = list()
    #     skills1 = []
    #     skills2 = []
    #     for j in range(len(value)):
    #         if value[j][0][:3] == '技能1':
    #             skills1.append(value[j][1])
    #         #wait to add UB
    #         if value[j][0][:3] == '技能2':
    #             skills2.append(value[j][1])
    #         # else:
    #         #     skills2.append(value[j][1])
    #     timeDict[nameList[i]].append(skills1)
    #     timeDict[nameList[i]].append(skills2)

    # #change to decimal time
    # for i, (key, value) in enumerate(timeDict.items()):
    #     for j in range(len(value)):
    #         for k in range(len(value[j])):
    #             value[j][k] = int(value[j][k].split(':')[0]) * 60 + int(value[j][k].split(':')[1])


    # gntTimeList = []
    # for i, (key, value) in enumerate(timeDict.items()):
    #     gntTimeList.append(value)


    # #預設技能經過時間 1秒
    # for i in range(len(gntTimeList)):
    #     for j in range(len(gntTimeList[i])):
    #         for k in range(len(gntTimeList[i][j])):
    #             gntTimeList[i][j][k] = (gntTimeList[i][j][k],-1)

    # return gntTimeList