# from Tkinter import *
# import sys
# import random
# import pyttsx
# import os

# from bluetooth import b1, b2

# def LaunchCallBack():	
# 	os.system("ino build")
# 	os.system("ino upload")
# 	#os.system("ino serial")
# 	os.system("python voice.py "+ '\''+e1.get()+'\' ' + '\''+ e2.get() + '\' ' + '\'' + e3.get() + '\' ')

# def show_entry_fields():
#    print("Question: %s\nCorrectOption: %s\nWrongOption: %s" % (e1.get(), e2.get(), e3.get()))
#    # e1.delet	e(0,END)
#    # e2.delete(0,END)
#    # e3.delete(0,END)
from voice import readOut
from Tkinter import*
import tkMessageBox
from bluetooth import check_answers, initialize

def instructions():
    tkMessageBox.showinfo( "INSTRUCTIONS", "Click the start button to start recieving questions.                           Left switch is for option one, right switch is for option two.                 Each player can answer the readout question by pressing the switch.                                                                                               GOAL:                                        FASTEST ANSWER FETCHES A POINT.                                                   THE ONE WHO SCORES MAXIMUM POINTS WINS THE GAME.")

def test():
	global top

	p1_score = 0
	p2_score = 0
	f = open('questions.txt','r')
	all_ques = f.readlines()
	print all_ques
	for i in range(len(all_ques)/4):
		lines = all_ques[4*i:4*i+4]
		q = Question(lines[0].strip(), lines[1].strip(), lines[2].strip(), int(lines[3].strip()))
		buttonQuestion['text'] = q.question
		buttonOp1['text'] = q.option1
		buttonOp2['text'] = q.option2
		top.update_idletasks()

		readOut("The Question is")
		readOut(q.question)
		readOut("Option 1 is")
		readOut(q.option1)
		readOut("Option 2 is")
		readOut(q.option2)
		b1 = 0
		b2 = 0
		while not b1 and not b2:
			b1, b2 = check_answers()
			print b1, b2	
		if b1 == q.answer:
			readOut("Player 1 gave correct option")
			p1_score += 10
		elif b2 == q.answer:
			readOut("Player 2 gave correct option")
			p2_score += 10
		elif b1 != 0:
			readOut("Player 1 gave wrong option")
			p1_score -= 5
		elif b2 != 0:
			readOut("Player 2 gave wrong option")
			p2_score -= 5
		top.update_idletasks()
	f.close()


class Question():
	def __init__(self, question, option1, option2, answer):
		self.question = question
		self.option1 = option1
		self.option2 = option2
		self.answer = answer

# Gets data from both boards
b1 = 0
b2 = 0

top=Tk()
C = Canvas(top, bg="white", height=840, width=1600)
C.pack(side="top", fill="both", expand=True)
canvas_id = C.create_text(550, 20, anchor="nw")
C.itemconfig(canvas_id, text="LEARN AND PLAY",font=("Helvetica",48,"bold"))
C.grid()

if(initialize()):
	button4 = Button(None, text = "PLAYER 1",font=("Helvetica",24,"bold"), command = None, anchor = W)
	button4.configure(width = 15, activebackground = "green", bg="green",relief = FLAT)
	button5 = Button(None, text = "PLAYER 2",font=("Helvetica",24,"bold"), command = None, anchor = W)
	button5.configure(width = 15, activebackground = "green", bg="green",relief = FLAT)

else:
	button4 = Button(None, text = "PLAYER 1",font=("Helvetica",24,"bold"), command = None, anchor = W)
	button4.configure(width = 15, activebackground = "red", bg="red",relief = FLAT)
	button5 = Button(None, text = "PLAYER 2",font=("Helvetica",24,"bold"), command = None, anchor = W)
	button5.configure(width = 15, activebackground = "red", bg="red",relief = FLAT)
	tkMessageBox.showinfo("Error", "Unable to connect. Try resetting.")
button4_window = C.create_window(50, 180, anchor=NW, window=button4)
button5_window = C.create_window(1200, 180, anchor=NW, window=button5)

button3 = Button(None, text = "EXIT",font=("Helvetica",24,"bold"), command = top.quit, anchor = W)
button3.configure(width = 20, activebackground = "#ffc100", bg="red",relief = FLAT)
button3_window = C.create_window(650, 700, anchor=NW, window=button3)

buttonStart = Button(None, text = "           START",font=("Helvetica",24,"bold"), command=test, anchor = W)
buttonStart.configure(width = 20, activebackground = "#ffc100", bg="red",relief = FLAT)
buttonStart_window = C.create_window(580,180 , anchor=NW, window=buttonStart)

button_ins = Button(None, text = "    INSTRUCTIONS",font=("Helvetica",24,"bold"), command = instructions, anchor = W)
button_ins.configure(width = 20, activebackground = "#ffc100", bg="red",relief = FLAT)
button_ins_window = C.create_window(580, 240, anchor=NW, window=button_ins)

buttonQuestion = Button(None, text = "Question",font=("Helvetica",24,"bold"), anchor = W)
buttonQuestion.configure(width = 80, activebackground = "#ff6666", bg="#ff6666",relief = FLAT)
buttonQuestion_window = C.create_window(50,450 , anchor=NW, window=buttonQuestion)

buttonOp1 = Button(None, text = "Option1",font=("Helvetica",24,"bold"), anchor = W)
buttonOp1.configure(width = 40, activebackground = "#ff9999", bg="#ff9999",relief = FLAT)
buttonOp1_window = C.create_window(50,510 , anchor=NW, window=buttonOp1)

buttonOp2 = Button(None, text = "Options2",font=("Helvetica",24,"bold"), anchor = W)
buttonOp2.configure(width = 39, activebackground = "#ff9999", bg="#ff9999",relief = FLAT)
buttonOp2_window = C.create_window(790,510 , anchor=NW, window=buttonOp2)

C.pack()	
top.mainloop()
