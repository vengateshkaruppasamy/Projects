import tkinter as tkr
from tkinter import *
import pygame
import os
from tkinter.filedialog import askdirectory

win = Tk()
win.title("Music Player")
win.geometry('500x490')
win.config(bg = "#6002EE")
win.resizable(False, False)
p1 = PhotoImage(file = 'img/icons/music.png')
win.iconphoto(False, p1)

directory = askdirectory()
os.chdir(directory)
songlist = os.listdir()
playlist = tkr.Listbox(win,border = 5 ,height=7, font=("Caliber", 15 ,'bold') , bg = '#C5CAE9' , fg = "black" , selectmode = tkr.SINGLE )

for item in songlist:
	pos = 0
	playlist.insert(pos , item)
	pos = + 1

pygame.init()
pygame.mixer.init()

def palysong():
	pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
	var.set(playlist.get(tkr.ACTIVE))
	pygame.mixer.music.play()

def stopplay():
	pygame.mixer.music.stop()

def pauseplay():
	pygame.mixer.music.pause()

def unpauseplay():
	pygame.mixer.music.unpause()

play_button = tkr.Button(win , command = palysong ,width=5,height=3,text="PLAY", font = ("Caliber", 12,"bold"),bg ="#5E35B1",fg = "ghostwhite")
stop_button = tkr.Button(win , command = stopplay,width=5,height=3, text="STOP",font = ("Caliber", 12,"bold"),bg ="#5E35B1",fg = "ghostwhite")
pause_button = tkr.Button(win , command = pauseplay,width=5,height=3,text="PAUSE", font = ("Caliber", 12,"bold"),bg ="#5E35B1",fg = "ghostwhite")
unpause_button = tkr.Button(win , command = unpauseplay,width=5,height=3,text="UNPAUSE", font = ("Caliber", 12,"bold"),bg ="#5E35B1",fg = "ghostwhite")

var = StringVar()
songtitle=Label(textvariable = var , font = ("Caliber", 12,"bold"),bg ="#6002EE",fg = "ghostwhite")

songtitle.pack( fill = 'x')
playlist.pack(fill = 'x' )
play_button.pack(fill = 'x')
stop_button.pack(fill = 'x')
pause_button.pack(fill = 'x')
unpause_button.pack(fill = 'x')


win.mainloop()