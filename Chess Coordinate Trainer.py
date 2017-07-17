from Tkinter import *
import tkFont
import random
import os 
from pathlib import Path

lbFileStr = ("%s\Data" %os.getcwd())
lbFilePath = Path(lbFileStr)

iconsStr = ("%s\Icons" %os.getcwd())

if not os.path.exists(lbFileStr):
	os.makedirs(lbFileStr)

lbValues = []

if Path(lbFileStr + "\data.txt").is_file():
	lbFile = open(os.path.join(lbFileStr, "data.txt"), 'r')
	with open(os.path.join(lbFileStr, "data.txt"), 'r') as f:
		lbValues = f.read().splitlines()
		lbValues[0] = eval(lbValues[0])
		lbValues[1] = eval(lbValues[1])
		lbValues[2] = eval(lbValues[2])
else:
	lbFile = open(lbFileStr + "\data.txt", 'w+')
	for i in range(3):
		lbValues.append(0)
	lbFile.write('0\n0\n0')

top = Tk()
top.configure(bg = "gray80")
top.wm_title("Chess Coordinate Trainer")
top.resizable(width=FALSE, height=FALSE)
top.wm_iconbitmap(iconsStr, "\CCT.ico")


helv8 = tkFont.Font(family='Helvetica', size=8)
helv50 = tkFont.Font(family='Helvetica', size=50)
bottomLabelFont10 = tkFont.Font(family='Helvetica', size=10)

squares = ["A1","A2","A3","A4","A5","A6","A7","A8","B1","B2","B3","B4","B5","B6","B7","B8","C1","C2","C3","C4","C5","C6","C7","C8","D1","D2","D3","D4","D5","D6","D7","D8","E1","E2","E3","E4","E5","E6","E7","E8","F1","F2","F3","F4","F5","F6","F7","F8","G1","G2","G3","G4","G5","G6","G7","G8","H1","H2","H3","H4","H5","H6","H7","H8"]

showCoords = 0

A1 = Button(top, height = 5, width = 12, command = lambda: click("A1"), bg = "Olive Drab", anchor = "sw", text = "A1")
A2 = Button(top, height = 5, width = 12, command = lambda: click("A2"), bg = "Light Yellow", anchor = "sw", text = "2")
A3 = Button(top, height = 5, width = 12, command = lambda: click("A3"), bg = "Olive Drab", anchor = "sw", text = "3")
A4 = Button(top, height = 5, width = 12, command = lambda: click("A4"), bg = "Light Yellow", anchor = "sw", text = "4")
A5 = Button(top, height = 5, width = 12, command = lambda: click("A5"), bg = "Olive Drab", anchor = "sw", text = "5")
A6 = Button(top, height = 5, width = 12, command = lambda: click("A6"), bg = "Light Yellow", anchor = "sw", text = "6")
A7 = Button(top, height = 5, width = 12, command = lambda: click("A7"), bg = "Olive Drab", anchor = "sw", text = "7")
A8 = Button(top, height = 5, width = 12, command = lambda: click("A8"), bg = "Light Yellow", anchor = "sw", text = "8")
B1 = Button(top, height = 5, width = 12, command = lambda: click("B1"), bg = "Light Yellow", anchor = "sw", text = "B")
B2 = Button(top, height = 5, width = 12, command = lambda: click("B2"), bg = "Olive Drab", anchor = "sw")
B3 = Button(top, height = 5, width = 12, command = lambda: click("B3"), bg = "Light Yellow", anchor = "sw")
B4 = Button(top, height = 5, width = 12, command = lambda: click("B4"), bg = "Olive Drab", anchor = "sw")
B5 = Button(top, height = 5, width = 12, command = lambda: click("B5"), bg = "Light Yellow", anchor = "sw")
B6 = Button(top, height = 5, width = 12, command = lambda: click("B6"), bg = "Olive Drab", anchor = "sw")
B7 = Button(top, height = 5, width = 12, command = lambda: click("B7"), bg = "Light Yellow", anchor = "sw")
B8 = Button(top, height = 5, width = 12, command = lambda: click("B8"), bg = "Olive Drab", anchor = "sw")
C1 = Button(top, height = 5, width = 12, command = lambda: click("C1"), bg = "Olive Drab", anchor = "sw", text = "C")
C2 = Button(top, height = 5, width = 12, command = lambda: click("C2"), bg = "Light Yellow", anchor = "sw")
C3 = Button(top, height = 5, width = 12, command = lambda: click("C3"), bg = "Olive Drab", anchor = "sw")
C4 = Button(top, height = 5, width = 12, command = lambda: click("C4"), bg = "Light Yellow", anchor = "sw")
C5 = Button(top, height = 5, width = 12, command = lambda: click("C5"), bg = "Olive Drab", anchor = "sw")
C6 = Button(top, height = 5, width = 12, command = lambda: click("C6"), bg = "Light Yellow", anchor = "sw")
C7 = Button(top, height = 5, width = 12, command = lambda: click("C7"), bg = "Olive Drab", anchor = "sw")
C8 = Button(top, height = 5, width = 12, command = lambda: click("C8"), bg = "Light Yellow", anchor = "sw")
D1 = Button(top, height = 5, width = 12, command = lambda: click("D1"), bg = "Light Yellow", anchor = "sw", text = "D")
D2 = Button(top, height = 5, width = 12, command = lambda: click("D2"), bg = "Olive Drab", anchor = "sw")
D3 = Button(top, height = 5, width = 12, command = lambda: click("D3"), bg = "Light Yellow", anchor = "sw")
D4 = Button(top, height = 5, width = 12, command = lambda: click("D4"), bg = "Olive Drab", anchor = "sw")
D5 = Button(top, height = 5, width = 12, command = lambda: click("D5"), bg = "Light Yellow", anchor = "sw")
D6 = Button(top, height = 5, width = 12, command = lambda: click("D6"), bg = "Olive Drab", anchor = "sw")
D7 = Button(top, height = 5, width = 12, command = lambda: click("D7"), bg = "Light Yellow", anchor = "sw")
D8 = Button(top, height = 5, width = 12, command = lambda: click("D8"), bg = "Olive Drab", anchor = "sw")
E1 = Button(top, height = 5, width = 12, command = lambda: click("E1"), bg = "Olive Drab", anchor = "sw", text = "E")
E2 = Button(top, height = 5, width = 12, command = lambda: click("E2"), bg = "Light Yellow", anchor = "sw")
E3 = Button(top, height = 5, width = 12, command = lambda: click("E3"), bg = "Olive Drab", anchor = "sw")
E4 = Button(top, height = 5, width = 12, command = lambda: click("E4"), bg = "Light Yellow", anchor = "sw")
E5 = Button(top, height = 5, width = 12, command = lambda: click("E5"), bg = "Olive Drab", anchor = "sw")
E6 = Button(top, height = 5, width = 12, command = lambda: click("E6"), bg = "Light Yellow", anchor = "sw")
E7 = Button(top, height = 5, width = 12, command = lambda: click("E7"), bg = "Olive Drab", anchor = "sw")
E8 = Button(top, height = 5, width = 12, command = lambda: click("E8"), bg = "Light Yellow", anchor = "sw")
F1 = Button(top, height = 5, width = 12, command = lambda: click("F1"), bg = "Light Yellow", anchor = "sw", text = "F")
F2 = Button(top, height = 5, width = 12, command = lambda: click("F2"), bg = "Olive Drab", anchor = "sw")
F3 = Button(top, height = 5, width = 12, command = lambda: click("F3"), bg = "Light Yellow", anchor = "sw")
F4 = Button(top, height = 5, width = 12, command = lambda: click("F4"), bg = "Olive Drab", anchor = "sw")
F5 = Button(top, height = 5, width = 12, command = lambda: click("F5"), bg = "Light Yellow", anchor = "sw")
F6 = Button(top, height = 5, width = 12, command = lambda: click("F6"), bg = "Olive Drab", anchor = "sw")
F7 = Button(top, height = 5, width = 12, command = lambda: click("F7"), bg = "Light Yellow", anchor = "sw")
F8 = Button(top, height = 5, width = 12, command = lambda: click("F8"), bg = "Olive Drab", anchor = "sw")
G1 = Button(top, height = 5, width = 12, command = lambda: click("G1"), bg = "Olive Drab", anchor = "sw", text = "G")
G2 = Button(top, height = 5, width = 12, command = lambda: click("G2"), bg = "Light Yellow", anchor = "sw")
G3 = Button(top, height = 5, width = 12, command = lambda: click("G3"), bg = "Olive Drab", anchor = "sw")
G4 = Button(top, height = 5, width = 12, command = lambda: click("G4"), bg = "Light Yellow", anchor = "sw")
G5 = Button(top, height = 5, width = 12, command = lambda: click("G5"), bg = "Olive Drab", anchor = "sw")
G6 = Button(top, height = 5, width = 12, command = lambda: click("G6"), bg = "Light Yellow", anchor = "sw")
G7 = Button(top, height = 5, width = 12, command = lambda: click("G7"), bg = "Olive Drab", anchor = "sw")
G8 = Button(top, height = 5, width = 12, command = lambda: click("G8"), bg = "Light Yellow", anchor = "sw")
H1 = Button(top, height = 5, width = 12, command = lambda: click("H1"), bg = "Light Yellow", anchor = "sw", text = "H")
H2 = Button(top, height = 5, width = 12, command = lambda: click("H2"), bg = "Olive Drab", anchor = "sw")
H3 = Button(top, height = 5, width = 12, command = lambda: click("H3"), bg = "Light Yellow", anchor = "sw")
H4 = Button(top, height = 5, width = 12, command = lambda: click("H4"), bg = "Olive Drab", anchor = "sw")
H5 = Button(top, height = 5, width = 12, command = lambda: click("H5"), bg = "Light Yellow", anchor = "sw")
H6 = Button(top, height = 5, width = 12, command = lambda: click("H6"), bg = "Olive Drab", anchor = "sw")
H7 = Button(top, height = 5, width = 12, command = lambda: click("H7"), bg = "Light Yellow", anchor = "sw")
H8 = Button(top, height = 5, width = 12, command = lambda: click("H8"), bg = "Olive Drab", anchor = "sw")

Alist = [A1,A2,A3,A4,A5,A6,A7,A8]
Blist = [B1,B2,B3,B4,B5,B6,B7,B8]
Clist = [C1,C2,C3,C4,C5,C6,C7,C8]
Dlist = [D1,D2,D3,D4,D5,D6,D7,D8]
Elist = [E1,E2,E3,E4,E5,E6,E7,E8]
Flist = [F1,F2,F3,F4,F5,F6,F7,F8]
Glist = [G1,G2,G3,G4,G5,G6,G7,G8]
Hlist = [H1,H2,H3,H4,H5,H6,H7,H8]

columnlist = [Alist,Blist,Clist,Dlist,Elist,Flist,Glist,Hlist]
alpha = ["A","B","C","D","E","F","G","H"]

for i in range(8):
	for j in range(8):
		columnlist[i][j].grid(row=8-j,column=i)

def whiteButtons():
	global A1,A2,A3,A4,A5,A6,A7,A8,B1,B2,B3,B4,B5,B6,B7,B8,C1,C2,C3,C4,C5,C6,C7,C8,D1,D2,D3,D4,D5,D6,D7,D8,E1,E2,E3,E4,E5,E6,E7,E8,F1,F2,F3,F4,F5,F6,F7,F8,G1,G2,G3,G4,G5,G6,G7,G8,H1,H2,H3,H4,H5,H6,H7,H8
	
	for i in range(8):
		for j in range(8):
			columnlist[i][j].configure(text = "%s" %squares[8*(i) + j], command = lambda i=i, j=j: click("%s" %squares[8*(i) + j]), anchor = "sw")
	
	if showCoords == 0:
		for i in range(1, 8):
			for j in range(1, 8):
				columnlist[i][j].configure(text = "")
		A1.configure(text = "A1")
		for i in range(1, 8):
			Alist[i].configure(text = i+1)
		for i in range(1, 8):
			columnlist[i][0].configure(text = alpha[i])
	
	for i in range(8):
		for j in range(8):
			columnlist[i][j].grid(row=8-j,column=i)

def blackButtons():
	global A1,A2,A3,A4,A5,A6,A7,A8,B1,B2,B3,B4,B5,B6,B7,B8,C1,C2,C3,C4,C5,C6,C7,C8,D1,D2,D3,D4,D5,D6,D7,D8,E1,E2,E3,E4,E5,E6,E7,E8,F1,F2,F3,F4,F5,F6,F7,F8,G1,G2,G3,G4,G5,G6,G7,G8,H1,H2,H3,H4,H5,H6,H7,H8
	
	for i in range(8):
		for j in range(8):
			columnlist[i][j].configure(text = "%s" %squares[8*(7-i) + 7-j], command = lambda i=i, j=j: click("%s" %squares[8*(7-i) + 7-j]), anchor = "ne")
	
	if showCoords == 0:
		for i in range(8):
			for j in range(8):
				columnlist[i][j].configure(text = "")
		H8.configure(text = "A1")
		for i in range(7):
			Hlist[i].configure(text = 8-i)
		for i in range(7):
			columnlist[i][7].configure(text = alpha[7-i])

colour = 1
time = 30.0

menuframe = Frame(top, width = 200, height = 1, bg = "gray70")
menuframe.grid(row =0, column = 0, columnspan = 8, sticky = W)

menuFont = tkFont.Font(family='Helvetica', size=10, weight = 'bold')

startbutton = Button(menuframe, width = 14, height = 1, command = lambda: start(), text = "Start", font = 20, bg = "gray94")
prefbutton = Button(menuframe, width = 29, height = 1, command = lambda: showoptions(), text = "Preferences", bg = "gray94")
lbbutton = Button(menuframe, width = 30, height = 1, command = lambda: showLB(), text = "Leaderboards", bg = "gray94")
aboutbutton = Button(menuframe, width = 14, height = 1, command = lambda: showAbout(), text = "About", bg = "gray94")
exitbutton = Button(menuframe, width = 12, height = 1, command = sys.exit, text = "Exit", bg = "gray94")

startbutton.grid(row=0, column=0)
prefbutton.grid(row=0,column=2)
lbbutton.grid(row=0,column=4)
aboutbutton.grid(row=0,column=6)
exitbutton.grid(row=0,column=8)

menuframe.grid_columnconfigure(7, minsize = 93)


for i in range(3):
	separator = Frame(menuframe, height=25, width = 2, bd = 2, relief=SUNKEN, bg = "gray88").grid(row=0,column=2*i+1)
separator = Frame(menuframe, height = 25, width = 90, bd = 2, relief=RAISED, bg = "gray94").grid(row=0,column=7)

aimbox = Label(top, width = 3, height = 1, bg = "White", text = "...")
scorebox = Label(top, width = 5, height = 1, text = "0/0", bg = "White", anchor = "w")
timebox = Label(top, width = 4, height = 1, text = "30.0", bg = "White", anchor = "w")
bestbox = Label(top, width = 3, height = 1, text = "0", bg = "White")

colourlabel = Label(top, width = 37, height = 1, fg = "Black", bg = "White", text = "White")
scorelabel  = Label(top, width = 12, height = 1, text = "Current Score:", anchor = "e", bg = "Orange")
bestlabel = Label(top, width = 12, height = 1, text = "Session Best:", anchor = "e", bg = "Orange")
timelabel = Label(top, width = 8, height = 1, text = "Time Left:", anchor = "e", bg = "Orange")
newRecordLabel = Label(top , width = 11, height = 1, bg = "gray80")

recordcolour = 0

def newRecordChanger():
	global recordcolour
	if recordcolour == 1:
		recordcolour = 2
		newRecordLabel.configure(text = "New Record!", bg = "Dodger Blue")
		top.after(600, newRecordChanger)
	elif recordcolour == 2:
		recordcolour = 1
		newRecordLabel.configure(bg = "White")
		top.after(600, newRecordChanger)
	elif recordcolour == 0:
		newRecordLabel.configure(bg = "gray80", text = "")

aimbox.grid(row=11,column=3,rowspan=4,columnspan=2)
scorebox.grid(row=11,column=1, sticky = "e", padx = 10)
timebox.grid(row=11,column=7, sticky = "w")
bestbox.grid(row=12,column=1, sticky = "w", padx = 24)
colourlabel.grid(row=9,column=2,columnspan=4)
scorelabel.grid(row=11,column=0, sticky = "w", columnspan = 2)
bestlabel.grid(row=12,column=0, sticky = "w", columnspan = 2)
timelabel.grid(row=11,column=6, sticky = "e")
newRecordLabel.grid(row=12,column=1,columnspan=2, sticky = "e")

top.grid_rowconfigure(9, minsize = 43)
top.grid_rowconfigure(10, minsize = 1)
top.grid_rowconfigure(15, minsize = 9)

bottomBoxFont = tkFont.Font(family='Helvetica', size=13)
bottomLabelFont = tkFont.Font(family='Helvetica', size=13, weight = 'bold')

aimbox['font'] = helv50
startbutton['font'] = helv8
prefbutton['font'] = helv8
lbbutton['font'] = helv8
aboutbutton['font'] = helv8

colourlabel['font'] = bottomLabelFont
scorelabel['font'] = bottomLabelFont
bestlabel['font'] = bottomLabelFont
timelabel['font'] = bottomLabelFont
newRecordLabel['font'] = bottomLabelFont
scorebox['font'] = bottomBoxFont
timebox['font'] = bottomBoxFont
bestbox['font'] = bottomBoxFont

def showLB():
	global LBWindow
	try:
		LBWindow.winfo_exists()
	except:
		LBWindow = Tk()
		LBWindow.wm_title("Leaderboards")
		LBWindow.resizable(width=FALSE, height=FALSE)
		LBWindow.wm_iconbitmap(iconsStr + "\leaderboards.ico")
		LBWindow.configure(bg = "gray95")
		
		recordsLabel = Label(LBWindow, width = 38, height = 1, text = "Records:", bg = "Orange")
		time10HeaderLabel = Label(LBWindow, width = 12, height = 1, text = "10 Seconds", bg = "Orange")
		time30HeaderLabel = Label(LBWindow, width = 12, height = 1, text = "30 Seconds", bg = "Orange")
		time60HeaderLabel = Label(LBWindow, width = 12, height = 1, text = "60 Seconds", bg = "Orange")
		time10ScoreLabel = Label(LBWindow, width = 12, height = 1, text = "%d" %(lbValues[0]))
		time30ScoreLabel = Label(LBWindow, width = 12, height = 1, text = "%d" %(lbValues[1]))
		time60ScoreLabel = Label(LBWindow, width = 12, height = 1, text = "%d" %(lbValues[2]))
	
		def close():
			LBWindow.destroy()
	
		closeButton = Button(LBWindow, width = 11, height = 1, text = "Close", command = lambda: close())
		
		horSeparator = Frame(LBWindow, width = 274, height = 2, relief = FLAT, bd = 4, bg = "Black").grid(row=1,column=0,columnspan=5)
		verSeparator = Frame(LBWindow, width = 2, height = 56, relief = FLAT, bd = 1, bg = "Black").grid(row=2,column=1,rowspan=3)
		verSeparator = Frame(LBWindow, width = 2, height = 56, relief = FLAT, bd = 1, bg = "Black").grid(row=2,column=3,rowspan=3)
		horSeparator = Frame(LBWindow, width = 274, height = 2, relief = FLAT, bd = 4, bg = "Black").grid(row=3,column=0,columnspan=5)
		horSeparator = Frame(LBWindow, width = 274, height = 2, relief = FLAT, bd = 4, bg = "Black").grid(row=5,column=0,columnspan=5)
	
		recordsLabel.grid(row=0,column=0, columnspan = 5, ipadx = 1)
		time10HeaderLabel.grid(row=2,column=0, ipady = 3)
		time30HeaderLabel.grid(row=2,column=2, ipady = 3)
		time60HeaderLabel.grid(row=2,column=4, ipady = 3)
		time10ScoreLabel.grid(row=4,column=0, ipady = 3)
		time30ScoreLabel.grid(row=4,column=2, ipady = 3)
		time60ScoreLabel.grid(row=4,column=4, ipady = 3)
	
		closeButton.grid(row=6,column=4, padx = 2, sticky = "e")
	

nextColour = ""

def showAbout():
	global aboutWindow
	try:
		aboutWindow.winfo_exists()
	except:
		aboutWindow = Tk()
		aboutWindow.resizable(width=FALSE, height=FALSE)
		aboutWindow.configure(bg = "gray96")
		aboutWindow.wm_title("About")
		aboutWindow.wm_iconbitmap(iconsStr + "\\about.ico")
		
		def close():
			aboutWindow.destroy()
		
		closeButton = Button(aboutWindow, width = 10, height = 1, text = "Close", command = lambda: close(), bg = "Gray")
		
		aboutText = Label(aboutWindow, text = ' Created by Stephen Ryan during the summer of 2017. \n \n \n Chess is a beautiful mistress. \n\n -Larsen \n\n Of chess it has been said that life is not long enough for it,\n but that is the fault of life, not chess. \n\n -Chernev', width = 48, height = 12, bg = "White")
		
		colourList = ["light blue","brown","yellow","light green","orange","turquoise","pink", "rosy brown", "gold", "cyan", "PeachPuff2", "PaleGreen1", "RosyBrown1", "orchid1", "wheat", "lavender", "mint cream", "honeydew", "light cyan", "gainsboro", "LightGoldenrod2", "yellow3", "LightSteelBlue2"]
		
		def colourChanger():
			global aboutWindow
			global nextColour
			previousColour = nextColour
			while previousColour == nextColour:
				nextColour = random.choice(colourList)
				
			aboutWindow.configure(bg = nextColour)
			print nextColour
			aboutWindow.after(500, colourChanger)
		
		colourChanger()
		aboutText.config(font=("Helvetica", 12))
		
		aboutText.grid(row=1,column=1, columnspan = 2)
		
		closeButton.grid(row=2,column=1, sticky = "e")
		aboutWindow.grid_columnconfigure(0, minsize = 22)
		aboutWindow.grid_columnconfigure(3, minsize = 22)
		aboutWindow.grid_rowconfigure(0, minsize = 22)
		aboutWindow.grid_rowconfigure(2, minsize = 22)

def showoptions():
	global prefWindow
	global stopTimer
	try:
		prefWindow.winfo_exists()
	except:
		prefWindow = Tk()
		prefWindow.configure(bg = "gray96")
		prefWindow.wm_title("Preferences")
		prefWindow.resizable(width=FALSE, height=FALSE)
		prefWindow.wm_iconbitmap(iconsStr + "\gears.ico")
		
		stopTimer = 1
		
		colourChosen = Label(prefWindow, text = "Colour:", width = 16, height = 1, bg = "Orange", anchor = "e")
		timeLabel = Label(prefWindow, text = "Game Duration:", width = 16, height = 1, bg = "Orange", anchor = "e")
		coords = Label(prefWindow, text = "Show coordinates:", width = 16, height = 1, bg = "Orange", anchor = "e")
		
		def changeToWhite():
			global colour 
			whiteButton.configure(bg = "gray76")
			blackButton.configure(bg = "gray95")
			randomButton.configure(bg = "gray95")
			colour = 1

		def changeToBlack():
			global colour
			blackButton.configure(bg = "gray76")
			whiteButton.configure(bg = "gray95")
			randomButton.configure(bg = "gray95")
			colour = 2

		def changeToRandom():
			global colour
			randomButton.configure(bg = "gray76")
			whiteButton.configure(bg = "gray95")
			blackButton.configure(bg = "gray95")
			colour = 3

		def changeTo10():
			global time
			time10.configure(bg = "gray76")
			time30.configure(bg = "gray95")
			time60.configure(bg = "gray95")
			time = 10.0

		def changeTo30():
			global time
			time10.configure(bg = "gray95")
			time30.configure(bg = "gray76")
			time60.configure(bg = "gray95")
			time = 30.0

		def changeTo60():
			global time
			time10.configure(bg = "gray95")
			time30.configure(bg = "gray95")
			time60.configure(bg = "gray76")
			time = 60.0
	
		def changeToCoords():
			global showCoords
			showCoordsButton.configure(bg = "gray76")
			dontshowCoordsButton.configure(bg = "gray95")
			showCoords = 1

		def changeToNoCoords():
			global showCoords
			showCoordsButton.configure(bg = "gray95")
			dontshowCoordsButton.configure(bg = "gray76")
			showCoords = 0
		
		whiteButton = Button(prefWindow, text = "White", width = 11, height = 1, command = lambda: changeToWhite(), bg = "gray95")
		blackButton = Button(prefWindow, text = "Black", width = 11, height = 1, command = lambda: changeToBlack(), bg = "gray95")
		randomButton = Button(prefWindow, text = "Random", width = 11, height = 1, command = lambda: changeToRandom(), bg = "gray95")
		time10 = Button(prefWindow, text = "10 seconds", width = 11, height = 1, command = lambda: changeTo10(), bg = "gray95")
		time30 = Button(prefWindow, text = "30 seconds", width = 11, height = 1, command = lambda: changeTo30(), bg = "gray95")
		time60 = Button(prefWindow, text = "60 seconds", width = 11, height = 1, command = lambda: changeTo60(), bg = "gray95")
		showCoordsButton = Button(prefWindow, text = "Yes", width = 11, height = 1, command  = lambda: changeToCoords(), bg = "gray95")
		dontshowCoordsButton = Button(prefWindow, text = "No", width = 11, height = 1, command = lambda: changeToNoCoords(), bg = "gray95")
		applyButton = Button(prefWindow, text = "Apply", width = 11, height = 1, command = lambda: applyPref(), bg = "gray95")
		
		
		
		optionLabelFont = tkFont.Font(family='Helvetica', size=19, weight = 'bold')
		#colourChosen['font'] = optionLabelFont
		
		outerHorSeparator = Frame(prefWindow, width = 205, height = 4, relief = FLAT, bd = 1, bg = "gray95").grid(row=13,column=0,columnspan=4)
		innerHorSeparator = Frame(prefWindow, width = 200, height = 4, relief = GROOVE, bd = 1, bg = "gray95").grid(row=4,column=1,columnspan=2)
		innerHorSeparator = Frame(prefWindow, width = 200, height = 4, relief = GROOVE, bd = 1, bg = "gray95").grid(row=8,column=1,columnspan=2)
		innerHorSeparator = Frame(prefWindow, width = 200, height = 20, bg = "gray96").grid(row=11,column=1,columnspan=2)
		
		colourChosen.grid(row=1,column=1)
		whiteButton.grid(row=1,column=2)
		blackButton.grid(row=2,column=2)
		randomButton.grid(row=3,column=2)
		timeLabel.grid(row=5,column=1)
		time10.grid(row=5,column=2)
		time30.grid(row=6,column=2)
		time60.grid(row=7,column=2)
		coords.grid(row=9,column=1)
		showCoordsButton.grid(row=9,column=2)
		dontshowCoordsButton.grid(row=10,column=2)
		applyButton.grid(row=12,column=2)
		
		if colour == 1:
			changeToWhite()
		if colour == 2:
			changeToBlack()
		if colour == 3:
			changeToRandom()
		if time == 10.0:
			changeTo10()
		if time == 30.0:
			changeTo30()
		if time == 60.0:
			changeTo60()
		if showCoords == 0:
			changeToNoCoords()
		if showCoords == 1:
			changeToCoords()

def applyPref():
	global prefWindow
	if colour == 1:
		whiteButtons()
		colourlabel.configure(fg = "Black", bg = "White", text = "White")
		aimbox.configure(fg = "Black", bg = "White")
	elif colour == 2:
		blackButtons()
		colourlabel.configure(fg = "White", bg = "Black", text = "Black")
		aimbox.configure(fg = "White", bg = "Black")
	else:
		colours = [1,2]
		if random.choice(colours) == 1:
			whiteButtons()
			colourlabel.configure(fg = "Black", bg = "White", text = "White")
			aimbox.configure(fg = "Black", bg = "White")
		else:
			blackButtons()
			colourlabel.configure(fg = "White", bg = "Black", text = "Black")
			aimbox.configure(fg = "White", bg = "Black")
		timebox.configure(text = time)
	if time == 10.0:
		bestbox.configure(text = sessionbest10)
	if time == 30.0:
		bestbox.configure(text = sessionbest30)
	if time == 60.0:
		bestbox.configure(text = sessionbest60)
	timebox.configure(text = time)
	aimbox.configure(text = "...")
	prefWindow.destroy()

total = 0
score = 0
chosensquare = 0
begun = 0
k = 0
sessionbest10 = 0
sessionbest30 = 0
sessionbest60 = 0
newrecordtimer = 0
gameOver = 1

def scorechecker(score):
	global sessionbest10, sessionbest30, sessionbest60, newrecordtimer
	global recordcolour
	if score > sessionbest10 and time == 10.0:
		newrecordtimer = 1
		sessionbest10 = score
		bestbox.configure(text = sessionbest10)
		if sessionbest10 > lbValues[0]:
			recordcolour = 1
			newRecordChanger()
			lbValues[0] = sessionbest10
			lbFile = open(lbFileStr + "\data.txt", 'w')
			lbFile.write("%d\n%d\n%d" %(lbValues[0],lbValues[1],lbValues[2]))
	if score > sessionbest30 and time == 30.0:
		newrecordtimer = 1
		sessionbest30 = score
		bestbox.configure(text = sessionbest30)
		if sessionbest30 > lbValues[1]:
			recordcolour = 1
			newRecordChanger()
			lbValues[1] = sessionbest30
			lbFile = open(lbFileStr + "\data.txt", 'w')
			lbFile.write("%d\n%d\n%d" %(lbValues[0],lbValues[1],lbValues[2]))
	if score > sessionbest60 and time == 60.0:
		newrecordtimer = 1
		sessionbest60 = score
		bestbox.configure(text = sessionbest60)
		if sessionbest60 > lbValues[2]:
			recordcolour = 1
			newRecordChanger()
			lbValues[2] = sessionbest60
			lbFile = open(lbFileStr + "\data.txt", 'w')
			lbFile.write("%d\n%d\n%d" %(lbValues[0],lbValues[1],lbValues[2]))

stopTimer = 0

def timeupdater():
	global k
	global gameOver
	global recordcolour
	if stopTimer == 0:
		if k < (time/0.1) - 1:
			timebox.configure(text = "%s" %(time - 0.1 -0.1*k))
			k += 1
			top.after(88, timeupdater)
		elif k == (time/0.1) - 1: #fixes weird timerbox bug
			timebox.configure(text = "0.0")
			recordcolour = 0
			newRecordLabel.configure(bg = "gray80", text = "")
			scorechecker(score)
			gameOver = 1
			aimbox.configure(text = "...")

def scoreupdater(score):
	global total
	total += 1
	scorebox.configure(text = "%d/%d" %(score, total))

def countdownTimer3():
	aimbox.configure(text = "3")
	top.after(500, countdownTimer2)

def countdownTimer2():
	aimbox.configure(text = "2")
	top.after(500, countdownTimer1)

def countdownTimer1():
	aimbox.configure(text = "1")
	top.after(500, countdownTimer0)

def countdownTimer0():
	global begun
	global stopTimer
	timebox.configure(text = time)
	begun = 1
	top.after(88, timeupdater)
	stopTimer = 0
	aimbox.configure(text = randomsquarereturner())

def start():
    global stopTimer
    global k
    global begun
    global score
    global total
    global newrecordtimer
    global gameOver
    global recordcolour
    gameOver = 0
    begun = 0
    if newrecordtimer == 1:
        if time == 10.0:
            recordcolour = 0
            newRecordLabel.configure(bg = "gray80", text = "")
        if time == 30.0:
            recordcolour = 0
            newRecordLabel.configure(bg = "gray80", text = "")
        if time == 60.0:
            recordcolour = 0
            newRecordLabel.configure(bg = "gray80", text = "")
        newrecordtimer = 0
    scorechecker(score)
    score = 0
    total = 0
    stopTimer = 1
    scorebox.configure(text = "0/0")
    timebox.configure(text = time)
    k = 0
    countdownTimer3()

def randomsquarereturner():
    global chosensquare
    chosensquare = (random.choice(squares))
    return chosensquare

def click(square):
    global score
    global chosensquare
    global total
    if gameOver == 0:
        if square == chosensquare and begun == 1:
            score += 1
            randomsquarereturner()
            aimbox.configure(text = chosensquare)
        elif begun == 1:
            randomsquarereturner()
            aimbox.configure(text = chosensquare)
        if begun == 1:
            scoreupdater(score)
        if colour == 3:
            list = [1,2]
            if random.choice(list) == 1:
                whiteButtons()
                colourlabel.configure(fg = "Black", bg = "White", text = "White")
                aimbox.configure(fg = "Black", bg = "White")
            else:
                blackButtons()
                colourlabel.configure(fg = "White", bg = "Black", text = "Black")
                aimbox.configure(fg = "White", bg = "Black")

top.mainloop()

