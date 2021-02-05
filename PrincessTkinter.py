#!/usr/bin/env python
# coding: utf-8
import tkinter as tk
from PIL import ImageTk, Image
from drawPicture import startDraw
import pandas as pd
import copy
app = tk.Tk()
app.title('Princess')
app.geometry('1400x900')
app.resizable(0, 0)

sk1 = '#FF0000'
sk2 = '#0000FF'
ub = '#008000'
default_color = 'white'

imgFrontNames = ['リマ',
 'ミヤコ',
 'クウカ',
 'ジュン',
 'ムイミ（ニューイヤー）',
 'クウカ（オーエド）',
 'カオリ',
 'サレン（クリスマス）',
 'ツムギ（ハロウィン）',
 'レイ（ニューイヤー）',
 'リン（デレマス）',
 'ペコリーヌ',
 'ペコリーヌ（プリンセス）',
 'ルカ',
 'コッコロ（ニューイヤー）',
 'ノゾミ',
 'ムイミ',
 'マコト',
 'カヤ',
 'ヒヨリ（ニューイヤー）',
 'ニノン（オーエド）',
 'アキノ',
 'マコト（サマー）',
 'ジュン（サマー）',
 'マツリ',
 'クロエ',
 'マツリ（ハロウィン）',
 'エリコ（バレンタイン）',
 'アキノ（クリスマス）',
 'アヤネ（クリスマス）',
 'ルカ（サマー）',
 'ツムギ',
 'イノリ',
 'ヒヨリ（プリンセス）',
 'ヒヨリ',
 'ミソギ',
 'アヤネ',
 'ミソギ（ハロウィン）',
 'タマキ',
 'トモ',
 'チエル',
 'タマキ（サマー）',
 'エリコ',
 'ペコリーヌ（サマー）',
 'クルミ',
 'ジータ',
 'ペコリーヌ（ニューイヤー）',
 'レイ',
 'イリヤ（クリスマス）',
 'アンナ（サマー）',
 'クリスティーナ（クリスマス）',
 'シズル',
 'クリスティーナ',
 'クルミ（クリスマス）']

imgMidNames = ['ミミ',
 'シノブ',
 'ミミ（ハロウィン）',
 'ウヅキ（デレマス）',
 'レイ（ハロウィン）',
 'シズル（バレンタイン）',
 'マヒル（レンジャー）',
 'マヒル',
 'トモ（マジカル）',
 'ユカリ',
 'ユカリ（クリスマス）',
 'モニカ',
 'ニノン',
 'ノゾミ（クリスマス）',
 'ミフユ',
 'リン（レンジャー）',
 'イリヤ',
 'カオリ（サマー）',
 'サレン',
 'アンナ',
 'シノブ（ハロウィン）',
 'ナナカ（サマー）',
 'ミフユ（サマー）',
 'コッコロ',
 'アユミ（ワンダー）',
 'アユミ',
 'グレア',
 'モニカ（マジカル）',
 'アカリ（エンジェル）',
 'ヨリ（エンジェル）',
 'コッコロ（サマー）',
 'レム',
 'ラム',
 'リン',
 'コッコロ（プリンセス）',
 'ラビリスタ',
 'ミツキ',
 'ハツネ（サマー）',
 'アカリ',
 'ヨリ',
 'サレン（サマー）',
 'ミヤコ（ハロウィン）']
imgBackNames = ['アリサ',
 'アン',
 'ルゥ',
 'ネネカ',
 'アオイ（編入生）',
 'キャル（ニューイヤー）',
 'ミオ（デレマス）',
 'ミサト（サマー）',
 'リノ',
 'スズナ',
 'スズナ（サマー）',
 'シオリ',
 'シオリ（マジカル）',
 'イオ',
 'イオ（サマー）',
 'スズメ',
 'スズメ（ニューイヤー）',
 'エミリア',
 'カスミ',
 'カスミ（マジカル）',
 'リノ（ワンダー）',
 'ミサト',
 'ナナカ',
 'ユイ（ニューイヤー）',
 'キャル',
 'ハツネ',
 'ミサキ',
 'ルナ',
 'ユイ（プリンセス）',
 'チカ（クリスマス）',
 'スズメ（サマー）',
 'キャル（サマー）',
 'アオイ',
 'チカ',
 'マホ（サマー）',
 'マホ',
 'ユイ',
 'ユキ',
 'ユニ',
 'キョウカ',
 'ミサキ（ハロウィン）',
 'キョウカ（ハロウィン）']

charactersButtons = []
showCharactersIndex = 0
originalTimeList = []
gntTimeList = []
buttons = []

entryLevel = None
notEnough = None

count = 0
charList = []
select1 = None
select2 = None
select3 = None
select4 = None
select5 = None
default = None
selectButton = None
countDefenseButton = None
recycleSkillButton = None
keepEditButton = None
output = None

def skillOk(app,gntTimeList,selectData,nameList):
    recycleSkillButton.destroy()
    global entryLevel
    #to zero
    for i in range(selectData.shape[0]):
        for j in range(1,selectData.shape[1]):
            selectData.iloc[i,j] = 0

    for i in range(len(gntTimeList)):
        for j in range(len(gntTimeList[i])):
            for k in range(len(gntTimeList[i][j])):
                if j == 0:
                    selectData.iloc[i,91 - gntTimeList[i][j][k]] = '技能1'
                elif j == 1:
                    selectData.iloc[i,91 - gntTimeList[i][j][k]] = '技能2'
                else:
                    selectData.iloc[i,91 - gntTimeList[i][j][k]] = 'UB'

    level = int(entryLevel.get())

    startDraw(level,selectData,nameList)
    
    global keepEditButton
    keepEditButton = tk.Button(app,text="繼續編輯",borderwidth=3,relief="solid",height = 2,  width=12,bg="White",command=keepEdit)
    keepEditButton.config(font=("Courier", 15))
    keepEditButton.place(x=400,y= 195)

    global output
    imgPath = 'combine.PNG'
    image = Image.open(imgPath)
    image = image.resize((1200, 500))
    outputimg = ImageTk.PhotoImage(image)
    output = tk.Label(app, image = outputimg)
    output.image = outputimg
    output.place(x=150,y= 350)
    return

def keepEdit():
    global gntTimeList,buttons,output,keepEditButton

    output.destroy()
    keepEditButton.destroy()
    
    global recycleSkillButton,originalTimeList
    recycleSkillButton = tk.Button(app,text="重置技能循環",borderwidth=3,relief="solid",height = 2,  width=12,bg="White",command=lambda:recycleSkill())
    recycleSkillButton.config(font=("Courier", 15))
    recycleSkillButton.place(x=575,y= 195)

    buttonsIndex = 0
    for i in range(5):
        for j in range(91):
            if j in gntTimeList[i][0]:
                buttons[buttonsIndex]['bg'] = sk1
            elif j in gntTimeList[i][1]:
                buttons[buttonsIndex]['bg'] = sk2
            elif j in gntTimeList[i][2]:
                buttons[buttonsIndex]['bg'] = ub
            else:
                buttons[buttonsIndex]['bg'] = default_color
            buttonsIndex += 1
    return

def click(i,j,button):
    global gntTimeList
    if(button["bg"] == sk1):
        button["bg"] = sk2
        gntTimeList[i][0].remove(j)
        gntTimeList[i][1].append(j)
    elif(button["bg"] == sk2):
        button["bg"] = ub
        gntTimeList[i][1].remove(j)
        gntTimeList[i][2].append(j)
    elif(button["bg"] == ub):
        button["bg"] = default_color
        gntTimeList[i][2].remove(j)
    else:
        button["bg"] = sk1
        gntTimeList[i][0].append(j)
    return

def getButton(app,team):
    if notEnough:
        notEnough.destroy()
    #read time data
    data = pd.read_csv('./data/timeData2.csv')
    del data['Unnamed: 0']
    selectData = pd.DataFrame(columns = data.columns)

    #add select rows
    for i in range(len(team)):
        for j in range(data.shape[0]):
            if team[i] == data.loc[j][0]:
                selectData.loc[i] = data.loc[j]

    nameList = selectData['Name'].tolist()

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
        for j in range(len(value)):
            if value[j][0][:3] == '技能1':
                skills1.append(value[j][1])
            else:
                skills2.append(value[j][1])
        timeDict[nameList[i]].append(skills1)
        timeDict[nameList[i]].append(skills2)

    global gntTimeList
    gntTimeList = []
    for i, (key, value) in enumerate(timeDict.items()):
        gntTimeList.append(value)

    for i in range(len(gntTimeList)):
        for j in range(len(gntTimeList[i])):
            for k in range(len(gntTimeList[i][j])):
                str = gntTimeList[i][j][k]
                m = str.split(':')[0]
                s = str.split(':')[-1]
                gntTimeList[i][j][k] = int(m) * 60 + int(s)
    #add UB
    for i in range(len(gntTimeList)):
        gntTimeList[i].append([])

    global originalTimeList
    originalTimeList = copy.deepcopy(gntTimeList)

    for i in range(5):
        for j in range(91):
            if j in gntTimeList[i][0]:
                btn = tk.Button(app, bg=sk1)
            elif j in gntTimeList[i][1]:
                btn = tk.Button(app, bg=sk2)
            else:
                btn = tk.Button(app, bg=default_color)
            btn.place(x= 1342.5 - 13.25 * j,y= 422 + 81 * i,height = 20,width = 13.25)
            buttons.append(btn)
            btn["command"] = lambda i=i,j=j,btn=btn: click(i,j,btn)

    global countDefenseButton
    countDefenseButton = tk.Button(app,text="計算破防量",borderwidth=3,relief="solid",height = 2,  width=12,bg="White",command=lambda: skillOk(app,gntTimeList,selectData,nameList))
    countDefenseButton.config(font=("Courier", 15))
    countDefenseButton.place(x=400,y= 195)

    
    global recycleSkillButton
    recycleSkillButton = tk.Button(app,text="重置技能循環",borderwidth=3,relief="solid",height = 2,  width=12,bg="White",command=lambda:recycleSkill())
    recycleSkillButton.config(font=("Courier", 15))
    recycleSkillButton.place(x=575,y= 195)

    return
def recycleSkill():
    global originalTimeList,gntTimeList,buttons
    #     output.configure(image = '')
    buttonsIndex = 0
    for i in range(5):
        for j in range(91):
            if j in originalTimeList[i][0]:
                buttons[buttonsIndex]['bg'] = sk1
            elif j in originalTimeList[i][1]:
                buttons[buttonsIndex]['bg'] = sk2
            else:
                buttons[buttonsIndex]['bg'] = default_color
            buttonsIndex += 1
    gntTimeList = copy.deepcopy(originalTimeList)
    return

def selectOk(charList):
    global output
    if len(charList) != 5:
        global notEnough
        notEnough = tk.Label(text="請選擇五隻角色!!!",fg = 'red')
        notEnough.config(font=("Courier", 30))
        notEnough.place(x=1000,y= 150)
    else:
        team = []
        for i in range(len(charList)):
            team.append(charList[i].split('/')[-1].split('.')[0])
        getButton(app,team)
    return

def selectChar(app,file):
    global count,charList
    if file not in charList:
        if count == 5:
            return
        charList.append(file)
        count += 1
        new(app,count)
    else:
        charList.remove(file)
        count -= 1
        delete()
        edit(app,count)
    return

def new(app,count):
    global select1,select2,select3,select4,select5
    if count == 1:
        imgPath = charList[0]
        image = Image.open(imgPath)
        image = image.resize((90, 90))
        selectimg = ImageTk.PhotoImage(image)
        select1 = tk.Label(app, image = selectimg)
        select1.image = selectimg
        select1.place(x=40,y=350)
    elif count == 2:
        imgPath = charList[1]
        image = Image.open(imgPath)
        image = image.resize((90, 90))
        selectimg = ImageTk.PhotoImage(image)
        select2 = tk.Label(app, image = selectimg)
        select2.image = selectimg
        select2.place(x=40,y=450)   
    elif count == 3:
        imgPath = charList[2]
        image = Image.open(imgPath)
        image = image.resize((90, 90))
        selectimg = ImageTk.PhotoImage(image)
        select3 = tk.Label(app, image = selectimg)
        select3.image = selectimg
        select3.place(x=40,y=550)
    elif count == 4:
        imgPath = charList[3]
        image = Image.open(imgPath)
        image = image.resize((90, 90))
        selectimg = ImageTk.PhotoImage(image)
        select4 = tk.Label(app, image = selectimg)
        select4.image = selectimg
        select4.place(x=40,y=650)
    else:
        imgPath = charList[4]
        image = Image.open(imgPath)
        image = image.resize((90, 90))
        selectimg = ImageTk.PhotoImage(image)
        select5 = tk.Label(app, image = selectimg)
        select5.image = selectimg
        select5.place(x=40,y=750)
    return

def edit(app,count):
    global select1,select2,select3,select4,select5
    if count >= 1:
        imgPath = charList[0]
        image = Image.open(imgPath)
        image = image.resize((90, 90))
        selectimg = ImageTk.PhotoImage(image)
        select1 = tk.Label(app, image = selectimg)
        select1.image = selectimg
        select1.place(x=40,y=350)
    if count >= 2:
        imgPath = charList[1]
        image = Image.open(imgPath)
        image = image.resize((90, 90))
        selectimg = ImageTk.PhotoImage(image)
        select2 = tk.Label(app, image = selectimg)
        select2.image = selectimg
        select2.place(x=40,y=450)   
    if count >= 3:
        imgPath = charList[2]
        image = Image.open(imgPath)
        image = image.resize((90, 90))
        selectimg = ImageTk.PhotoImage(image)
        select3 = tk.Label(app, image = selectimg)
        select3.image = selectimg
        select3.place(x=40,y=550)
    if count >= 4:
        imgPath = charList[3]
        image = Image.open(imgPath)
        image = image.resize((90, 90))
        selectimg = ImageTk.PhotoImage(image)
        select4 = tk.Label(app, image = selectimg)
        select4.image = selectimg
        select4.place(x=40,y=650)
    if count >= 5:
        imgPath = charList[4]
        image = Image.open(imgPath)
        image = image.resize((90, 90))
        selectimg = ImageTk.PhotoImage(image)
        select5 = tk.Label(app, image = selectimg)
        select5.image = selectimg
        select5.place(x=40,y=750)
    return

def delete():
    global select1,select2,select3,select4,select5
    selects = [select1,select2,select3,select4,select5]
    for select in selects:
        if select:
            select.configure(image = '')
def re():
    global count,charList,buttons,output
    count = 0
    charList = []
    delete()
    if default:
        default.configure(image = '')
    if output:
        output.destroy()
    if buttons:
        for i in range(len(buttons)):
            buttons[i].destroy()
        buttons = []
    if notEnough:
        notEnough.destroy()
    if countDefenseButton:
        countDefenseButton.destroy()
    if recycleSkillButton:
        recycleSkillButton.destroy()
    if keepEditButton:
        keepEditButton.destroy()
    return
def showCharacters():
    global imgFrontNames,imgMidNames,imgBackNames,showCharactersIndex,charactersButtons
    imgNames = [imgFrontNames,imgMidNames,imgBackNames]
    for i in range(len(imgNames[showCharactersIndex])):
        imgPath = './princess/' + imgNames[showCharactersIndex][i] + '.jpg'
        image = Image.open(imgPath)
        image = image.resize((60, 60))
        charImg = ImageTk.PhotoImage(image)
        btn = tk.Button(app, image = charImg)
        btn.image = charImg
        btn.place(x= 60 * (i % 20) + 100,y= (i // 20) * 60)
        charactersButtons.append(btn)
        btn["command"] = lambda app=app,imgPath=imgPath: selectChar(app,imgPath)
    return
def changeCharacters(x):
    global showCharactersIndex
    if  0 <= showCharactersIndex + x <= 2:
        showCharactersIndex += x
        if charactersButtons:
            for i in range(len(charactersButtons)):
                charactersButtons[i].destroy()
        showCharacters()
    return
def mainWindow():

    labelUrl = tk.Label(app, text = '輸入等級: ')
    labelUrl.config(font=("Courier", 15))
    labelUrl.place(x=150,y= 200)

    global entryLevel
    entryLevel = tk.Entry(app,width=5)
    entryLevel.insert(0, '175')
    entryLevel.config(font=("Courier", 15))
    entryLevel.place(x = 270,y= 200)

    showCharacters()
    # global imgFrontNames,frontButtons
    imgPath = './image/arrowLeft.png'
    image = Image.open(imgPath)
    image = image.resize((60, 60))
    leftArrowimg = ImageTk.PhotoImage(image)
    leftArrow = tk.Button(app, image = leftArrowimg,borderwidth = 0,command=lambda:changeCharacters(-1))
    leftArrow.image = leftArrowimg
    leftArrow.place(x=30,y= 60)

    imgPath = './image/arrowRight.png'
    image = Image.open(imgPath)
    image = image.resize((60, 60))
    rightArrowimg = ImageTk.PhotoImage(image)
    rightArrow = tk.Button(app, image = rightArrowimg,borderwidth = 0,command=lambda:changeCharacters(1))
    rightArrow.image = rightArrowimg
    rightArrow.place(x=1320,y= 60)


    global selectButton
    selectButton = tk.Button(app,text="確定角色",borderwidth=3,relief="solid",height = 2,  width=12,bg="White",command=lambda: selectOk(charList))
    selectButton.config(font=("Courier", 15))
    selectButton.place(x=400,y= 195)

    reButton = tk.Button(app,text="重新選擇角色",borderwidth=3,relief="solid",height = 2,  width=12,bg="White",command = re)
    reButton.config(font=("Courier", 15))
    reButton.place(x=750,y= 195)

    header = tk.Label(text="顯示破防堆疊狀態",borderwidth=3,relief="solid",height = 2,  width=75,bg="White")
    header.config(font=("Courier", 20))
    header.place(x=150,y= 270)

    sk1Label = tk.Label(app,text="技能1",relief="solid",bg=sk1,fg = 'white',width=5)
    sk1Label.config(font=("Courier", 20))
    sk1Label.place(x=1000,y= 210)

    sk2Label = tk.Label(app,text="技能2",relief="solid",bg=sk2,fg = 'white',width=5)
    sk2Label.config(font=("Courier", 20))
    sk2Label.place(x=1100,y= 210)

    ubLabel = tk.Label(app,text="UB",relief="solid",bg=ub,fg = 'white',width=5)
    ubLabel.config(font=("Courier", 20))
    ubLabel.place(x=1200,y= 210)

    imgPath = './image/default.PNG'
    image = Image.open(imgPath)
    image = image.resize((1200, 500))
    defaultimg = ImageTk.PhotoImage(image)
    default = tk.Label(app, image = defaultimg)
    default.image = defaultimg
    default.place(x=150,y= 350)

    app.mainloop()

    return
if __name__ == '__main__':
    mainWindow()