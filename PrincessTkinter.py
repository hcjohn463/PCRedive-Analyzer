#!/usr/bin/env python
# coding: utf-8
import tkinter as tk
from PIL import ImageTk, Image
from drawPicture import startDraw
app = tk.Tk()
app.title('Princess')
app.geometry('1400x900')
app.resizable(0, 0)

active="red"
default_color="white"

clickList = []

count = 0
charList = []
select1 = None
select2 = None
select3 = None
select4 = None
select5 = None
output = None
def ok(charList):
	global output
	if len(charList) != 5:
		notEnough = tk.Label(text="請選擇五隻角色!!!",fg = 'red')
		notEnough.config(font=("Courier", 30))
		notEnough.place(x=1000,y= 100)
	else:
		team = []
		for i in range(len(charList)):
			team.append(charList[i].split('/')[-1].split('.')[0])
		startDraw(team,clickList)

		imgPath = 'combine.PNG'
		image = Image.open(imgPath)
		image = image.resize((1200, 500))
		outputimg = ImageTk.PhotoImage(image)
		output = tk.Label(app, image = outputimg)
		output.image = outputimg
		output.place(x=150,y= 350)
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
    global select1,select2,select3,select4,select5,output
    if select1:
        select1.configure(image = '')
    if select2:
        select2.configure(image = '')
    if select3:
        select3.configure(image = '')
    if select4:
        select4.configure(image = '')
    if select5:
        select5.configure(image = '')
    if output:
       	output.configure(image = '')
    return

def re():
	global count,charList
	count = 0
	charList = []
	delete()
	return
def click(x,y,button):
	if(button["bg"] == active):
		button["bg"] = default_color
		clickList.remove([x,y])
	else:
		button["bg"] = active
		clickList.append([x,y])
	return

def mainWindow():

	imgNames = ['ヒヨリ（ニューイヤー）','レイ','ジータ','クリスティーナ','シズル（バレンタイン）','マコト','ムイミ','マコト（サマー）']

	for i in range(len(imgNames)):
		imgPath = './princess/' + imgNames[i] + '.jpg'
		image = Image.open(imgPath)
		image = image.resize((60, 60))
		charImg = ImageTk.PhotoImage(image)
		btn = tk.Button(app, image = charImg)
		btn.image = charImg
		btn.place(x= 60 * i,y=0)
		btn["command"] = lambda app=app,imgPath=imgPath: selectChar(app,imgPath)


	# No use
	# imgPath1 = './princess/ヒヨリ（ニューイヤー）.jpg'
	# image = Image.open(imgPath1)
	# image = image.resize((60, 60))
	# char1img = ImageTk.PhotoImage(image)
	# char1 = tk.Button(app, image = char1img,command= lambda: selectChar(app,imgPath1))
	# char1.place(x=0,y=0)

	enter = tk.Button(app,text="確定",borderwidth=3,relief="solid",height = 2,  width=10,bg="White",command=lambda: ok(charList))
	enter.config(font=("Courier", 15))
	enter.place(x=550,y= 150)

	reButton = tk.Button(app,text="重新選擇",borderwidth=3,relief="solid",height = 2,  width=10,bg="White",command = re)
	reButton.config(font=("Courier", 15))
	reButton.place(x=700,y= 150)

	header = tk.Label(text="顯示破防堆疊狀態",borderwidth=3,relief="solid",height = 2,  width=73,bg="White")
	header.config(font=("Courier", 20))
	header.place(x=150,y= 240)


	imgPath = 'default.PNG'
	image = Image.open(imgPath)
	image = image.resize((1200, 500))
	outputimg = ImageTk.PhotoImage(image)
	output = tk.Label(app, image = outputimg)
	output.image = outputimg
	output.place(x=150,y= 350)

	for i in range(91):
		for j in range(5):
			btn = tk.Button(app, bg=default_color)
			btn.place(x= 150 + 13.25 * i,y= 422 + 81 * j,height = 20,width = 13.25)
			btn["command"] = lambda i=i,j=j,btn=btn: click(j,i,btn)

	for i in range(91):
		tk.Grid.columnconfigure(app, i, weight=1)

	for i in range(5):
		tk.Grid.rowconfigure(app, i, weight=1)


	app.mainloop()

	return
if __name__ == '__main__':
	mainWindow()