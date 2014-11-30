from Tkinter import *
import sys
import random
import shutil
import pyttsx
import serial
import os

def LaunchCallBack():	
	os.system("ino build")
	os.system("ino upload")
	#os.system("ino serial")
	os.system("python voice.py "+ '\''+e1.get()+'\' ' + '\''+ e2.get() + '\' ' + '\'' + e3.get() + '\' ')

def show_entry_fields():
   print("Question: %s\nCorrectOption: %s\nWrongOption: %s" % (e1.get(), e2.get(), e3.get()))
   # e1.delete(0,END)
   # e2.delete(0,END)
   # e3.delete(0,END)

master = Tk()
Label(master, text="Question").grid(row=0)
Label(master, text="CorrectOption").grid(row=1)
Label(master, text="WrongOption").grid(row=2)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)

e1.insert(10,"Type the Question here.")
e2.insert(10,"Type the CorrectOption here.")
e3.insert(10,"Type the WrongOption here.")

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

Button(master, text='Confirm', command=show_entry_fields).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Launch', command=LaunchCallBack).grid(row=3, column=1, sticky=W, pady=4)

mainloop()