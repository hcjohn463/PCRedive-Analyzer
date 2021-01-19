#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
from countDefense import getDefenseTime
from countSkill import getSkillTime
import warnings
warnings.filterwarnings("ignore")

# In[2]:

def startDraw(team,clickList):

    #read time data
    data = pd.read_csv('timeData2.csv')
    del data['Unnamed: 0']
    selectData = pd.DataFrame(columns = data.columns)

    #add select rows
    for i in range(len(team)):
        for j in range(data.shape[0]):
            if team[i] == data.loc[j][0]:
                selectData.loc[i] = data.loc[j]

    #add UB
    for click in clickList:
        value = selectData.loc[click[0]][click[1] + 1]
        if value == '0' or value == 0:
            value = 'UB'
        else:
            value += ' + UB'
        selectData.iloc[click[0],click[1] + 1] = value
    # for i in range(data.shape[0]):
    #     if data.loc[i][0] in team:
    #         selectData.loc[i] = data.loc[i]

    #rename index
    selectData.index = [0,1,2,3,4]
    nameList = selectData['Name'].tolist()

    countList = getDefenseTime(selectData,nameList)

    gntTimeList = getSkillTime(selectData,nameList)

    #用来正常显示中文标签、负号
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus']=False


    spaceList = nameList.copy()
    spaceList.reverse()
    spaceList.append('-')


     
    fig, gnt = plt.subplots(figsize=(25,10)) 

    plot = gnt.twinx()

    hits = countList
    plot.set_xlabel('剩餘時間') 

    #plot.ylabel('破防量')
    plot.set_ylabel('破防量')

    # Setting X-axis limits
    my_x_ticks = np.arange(90, -1, -1)

    plot.plot(my_x_ticks, hits)

    # Setting Y-axis limits 
    gnt.set_ylim(0, 50)
  

    plt.xticks(my_x_ticks)

    gnt.set_xlim(90,0)
      
    # Setting ticks on y-axis 
    gnt.set_yticks([10, 20, 30, 40, 50, 60]) 
    # Labelling tickes of y-axis 
    gnt.axes.yaxis.set_ticklabels([])
      
    # Setting graph attribute 
    gnt.grid(True) 
      
    # Declaring a bar in schedule 
    gnt.broken_barh(gntTimeList[0][0], (49, 2), facecolors =('#ff7f0e'))

    gnt.broken_barh(gntTimeList[0][1], (49, 2), facecolors =('#bcbd22'))

    gnt.broken_barh(gntTimeList[0][2], (49, 2), facecolors =('red'))

    gnt.broken_barh(gntTimeList[1][0], (39, 2), facecolors =('#ff7f0e'))

    gnt.broken_barh(gntTimeList[1][1], (39, 2), facecolors =('#bcbd22'))

    gnt.broken_barh(gntTimeList[1][2], (39, 2), facecolors =('red'))
      
    gnt.broken_barh(gntTimeList[2][0], (29, 2), facecolors =('#ff7f0e'))

    gnt.broken_barh(gntTimeList[2][1], (29, 2), facecolors =('#bcbd22'))

    gnt.broken_barh(gntTimeList[2][2], (29, 2), facecolors =('red'))
                     
    gnt.broken_barh(gntTimeList[3][0], (19, 2), facecolors =('#ff7f0e'))

    gnt.broken_barh(gntTimeList[3][1], (19, 2), facecolors =('#bcbd22'))

    gnt.broken_barh(gntTimeList[3][2], (19, 2), facecolors =('red'))
        
    gnt.broken_barh(gntTimeList[4][0], (9, 2), facecolors =('#ff7f0e'))

    gnt.broken_barh(gntTimeList[4][1], (9, 2), facecolors =('#bcbd22'))

    gnt.broken_barh(gntTimeList[4][2], (9, 2), facecolors =('red'))

    plt.savefig("combine.png",bbox_inches='tight',
                pad_inches=0,
                format='png',
                dpi=300)

    return