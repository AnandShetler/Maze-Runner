'''
Created on Jan 9, 2016

@author: Anand Shetler
'''
from tkinter import *

class MainSc(Frame):
    def __init__(self, master, callNext):
        super(MainSc, self).__init__(master)
        self.callNext = callNext
        self.grid()
        self.createWidgets()
    def createWidgets(self):
        Frame.config(self, highlightbackground="purple", highlightthickness=5, bg="#ccffff")
        Label(self, bg="#ccffff").grid(row=0, column=1)
        Label(self, text="Maze Runner", font=("Verdana", 24, "bold"), fg="blue", highlightbackground="purple", highlightthickness=5, bg="green").grid(row=1, column=0, columnspan=2, sticky=N)
        Label(self, bg="#ccffff").grid(row=2, column=0)
        Label(self, bg="#ccffff", text="Welcome to MAZE RUNNER. Complete the maze as fast as you can. Try to go over the * to reduce your time. You move the 1 by clicking the direction buttons.\nAvoid the H's. Enter the number of rows/columns, the number of players, and the game mode and click 'Play' to begin.").grid(row=3, column=0, columnspan=2, sticky=N)
        Label(self, bg="#ccffff").grid(row=4, column=0)
        Label(self, bg="#ccffff", text="Enter the number of rows and columns:", fg="#606060").grid(row=5, column=0, sticky=N)
        self.cols = Entry(self)
        self.cols.grid(row=5, column=1, sticky=N)
        Label(self, bg="#ccffff", text="Number of players:", fg="#606060").grid(row=6, column=0, sticky=N)
        self.multi = StringVar()
        self.multi.set("1")
        m = OptionMenu(self, self.multi, "1", "2")
        m.grid(row=6, column=1, sticky=N)
        Label(self, bg="#ccffff", text="Game Mode (in hard mode you cannot cross your own path):", fg="#606060").grid(row=7, column=0, sticky=N)
        self.gmode = StringVar()
        self.gmode.set("Easy")
        g = OptionMenu(self, self.gmode, "Easy", "Hard")
        g.grid(row=7, column=1, sticky=N)
        Button(self, text="Play!", highlightbackground="green", highlightthickness=5, command=self.continueClicked).grid(row=8, column=0, columnspan=2, sticky=N)
        g.config(bg="#ccffff")
        m.config(bg="#ccffff")
        self.cols.config(highlightbackground="#ccffff", highlightthickness=2)
    def continueClicked(self):
        if self.cols.get() != "":
            self.callNext(self.cols.get(), self.multi.get(), self.gmode.get())
        else:
            self.cols.insert(0, "Enter the number of rows and columns")
