'''
Created on Jan 10, 2016

@author: Anand Shetler
'''
from tkinter import *

class LastSc(Frame):
    def __init__(self, master, start, end, claimed, cols, multi, callNext):
        super(LastSc, self).__init__(master)
        self.callNext = callNext
        self.start = start
        self.end = end
        self.master = master
        self.claimed = claimed
        self.multi = multi
        self.bonus = round(cols * 0.75, 0)
        self.grid()
        self.createWidgets()
    def createWidgets(self):
        Frame.config(self, highlightbackground="purple", highlightthickness=5, bg="#ccffff")
        Label(self, bg="#ccffff").grid(row=0, column=0)
        Label(self, text="Maze Runner", font=("Verdana", 24, "bold"), fg="blue", highlightbackground="purple", highlightthickness=5, bg="green").grid(row=1, column=1, columnspan=2, sticky=N)
        Label(self, bg="#ccffff").grid(row=2, column=2)
        results = Label(self, text="", bg="#ccffff")
        results.grid(row=3, column=1, sticky=N)
        if self.claimed:
            results["text"] = "Good job, you collected the bonus and your final time is "+str(round(self.end-self.start-self.bonus, 0))+" seconds."
        else:
            results["text"] = "It took you "+str(round(self.end-self.start, 0))+" to finish the maze."
        Button(self, text="Play again" , command=self.playAgain, highlightbackground="green", highlightthickness=5).grid(row=4, column=0, sticky=N)
        Button(self, text="Exit", command=self.exit, highlightbackground="green", highlightthickness=5).grid(row=4, column=2, sticky=N)
    def playAgain(self):
        self.callNext()
    def exit(self):
        self.master.destroy()
