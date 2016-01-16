'''
Created on Jan 9, 2016

@author: Anand Shetler
'''
from tkinter import *
import random
import time

class MazePage(Frame):
    def __init__(self, master, cols, multi, gmode, callNext):
        super(MazePage, self).__init__(master)
        self.callNext = callNext
        self.master = master
        self.cols = cols
        self.gmode = gmode
        self.multi = multi
        self.space = PhotoImage(file="images/space.gif")
        self.wall = PhotoImage(file="images/wall.gif")
        self.user1im = PhotoImage(file="images/user.gif")
        self.user2im = PhotoImage(file="images/user2.gif")
        self.bonusim = PhotoImage(file="images/bonus.gif")
        self.generateMaze()
        self.printableMaze()
        self.grid()
        self.createWidgets()
    def generateMaze(self):
        self.turn = 1
        self.bonuscol = random.randint(0, self.cols-1)
        self.bonusrow = random.randint(0, self.cols-1)
        self.claimedbonus = False
        self.user1 = "1"
        self.cols1 = 0
        self.rows1 = self.cols - 1
        self.user2 = "2"
        self.cols2 = 0
        self.rows2 = 0
        self.matrix = [[0 for x in range(self.cols)]for x in range(self.cols)]
        for y in range(self.cols):
            for i in range(self.cols):
                self.matrix[i][y] = random.randint(0,2)
                if self.matrix[i][y] == 1 or self.matrix[i][y] == 0:
                    self.matrix[i][y] = " "
                elif self.matrix[i][y] == 2:
                    self.matrix[i][y] = "H"
        self.matrix[0][self.cols-1] = self.user1
        self.matrix[self.bonuscol][self.bonusrow] = "*"
        if self.multi == "2":
            self.matrix[0][0] = self.user2
        self.start = time.time()
    def replace(self, c,r):
        if self.gmode == "Easy":
            self.matrix[c][r] = " "
            self.labels[c][r].configure(image=self.space)
            self.labels[c][r].image = self.space
        elif self.gmode == "Hard":
            self.matrix[c][r] = "H"
            self.labels[c][r].configure(image=self.wall)
            self.labels[c][r].image = self.wall
    def printableMaze(self):
        '''
        self.printedmaze = ""
        for y in self.matrix:
            for i in y:
                self.printedmaze += "'" + i + "',"
            self.printedmaze += "\n"
        '''
        self.labels = [[0 for x in range(self.cols)] for i in range(self.cols)]
        for y in range(len(self.matrix)):
            for i in range(len(self.matrix)):
                if self.matrix[i][y] == " ":
                    x = Label(self, image=self.space)
                    x.image = self.space
                elif self.matrix[i][y] == "H":
                    x = Label(self, image=self.wall)
                    x.image = self.wall
                elif self.matrix[i][y] == "1":
                    x = Label(self, image=self.user1im)
                    x.image = self.user1im
                elif self.matrix[i][y] == "2":
                    x = Label(self, image=self.user2im)
                    x.image = self.user2im
                else:
                    x = Label(self, image=self.bonusim)
                    x.image = self.bonusim
                self.labels[i][y] = x
                x.grid(row=i+3, column=y+1, sticky=W)
    def createWidgets(self):
        Frame.configure(self, highlightbackground="purple", highlightthickness=5, bg="#ccffff")
        Label(self, bg="#ccffff").grid(row=0, column=1)
        Label(self, text="Maze Runner", font=("Verdana", 24, "bold"), fg="blue", highlightbackground="purple", highlightthickness=5, bg="green").grid(row=1, column=self.cols//2-2, columnspan=7, sticky=N)
        Label(self, bg="#ccffff").grid(row=2, column=1)
        Label(self, width=10, bg="#ccffff").grid(row=1, column=0)
        Label(self, width=10, bg="#ccffff").grid(row=1, column=self.cols)
        Button(self, text="Λ", command=self.moveUp, highlightbackground="green", highlightthickness=5).grid(row=self.cols+4, column=self.cols//2, columnspan=2, sticky=S)
        Button(self, text="<", command=self.moveLeft, highlightbackground="green", highlightthickness=5).grid(row=self.cols+5, column=self.cols//2, sticky=E)
        Button(self, text=">", command=self.moveRight, highlightbackground="green", highlightthickness=5).grid(row=self.cols+5, column=self.cols//2+1, sticky=W)
        Button(self, text="V", command=self.moveDown, highlightbackground="green", highlightthickness=5).grid(row=self.cols+6, column=self.cols//2, columnspan=2, sticky=N)
        Button(self, text="Generate maze", command=self.generateNewMaze, highlightbackground="green", highlightthickness=5).grid(row=self.cols+7, column=0, sticky=N)
        Button(self, text="Exit", command=self.exit, highlightbackground="green", highlightthickness=5).grid(row=self.cols+7, column=self.cols+2, sticky=N)
    def exit(self):
        self.master.destroy()
    def generateNewMaze(self):
        self.generateMaze()
        self.printableMaze()
    def things(self):
        if self.matrix[self.cols1][self.rows1] == "*" or self.matrix[self.cols2][self.rows2] == "*":
            self.claimedbonus = True
        self.matrix[self.cols1][self.rows1] = self.user1
        self.labels[self.cols1][self.rows1].configure(image=self.user1im)
        self.labels[self.cols1][self.rows1].image = self.user1im
        if self.multi == "2":
            self.matrix[self.cols2][self.rows2] = self.user2
            self.labels[self.cols2][self.rows2].configure(image=self.user2im)
            self.labels[self.cols2][self.rows2].image = self.user2im
        #self.printableMaze()
        if self.cols1 == self.cols-1 or (self.multi == "2" and self.cols2 == self.cols):
            self.callNext(self.start, time.time(), self.claimedbonus, self.cols, self.multi)
    def moveUp(self):
        if self.multi == "2":
            if self.turn == 1:
                if self.matrix[self.cols1-1][self.rows1] == " " or self.matrix[self.cols1-1][self.rows1] == "*":
                    self.replace(self.cols1, self.rows1)
                    self.cols1 -= 1
                    self.turn = 2
            else:
                if self.matrix[self.cols2-1][self.rows2] == " " or self.matrix[self.cols2-1][self.rows2] == "*":
                    self.replace(self.cols2,self.rows2)
                    self.cols2 -= 1
                    self.turn = 1
        else:
            if self.matrix[self.cols1-1][self.rows1] == " " or self.matrix[self.cols1-1][self.rows1] == "*":
                self.replace(self.cols1,self.rows1)
                self.cols1 -= 1
        self.things()
    def moveDown(self):
        if self.multi == "2":
            if self.turn == 1:
                if self.matrix[self.cols1+1][self.rows1] == " " or self.matrix[self.cols1+1][self.rows1] == "*":
                    self.replace(self.cols1, self.rows1)
                    self.cols1 += 1
                    self.turn = 2
            else:
                if self.matrix[self.cols2+1][self.rows2] == " " or self.matrix[self.cols2+1][self.rows2] == "*":
                    self.replace(self.cols2, self.rows2)
                    self.cols2 += 1
                    self.turn = 1
        else:
            if self.matrix[self.cols1+1][self.rows1] == " " or self.matrix[self.cols1+1][self.rows1] == "*":
                self.replace(self.cols1, self.rows1)
                self.cols1 += 1
        self.things()
    def moveLeft(self):
        if self.multi == "2":
            if self.turn == 1:
                if self.matrix[self.cols1][self.rows1-1] == " " or self.matrix[self.cols1][self.rows1-1] == "*":
                    self.replace(self.cols1, self.rows1)
                    self.rows1 -= 1
                    self.turn = 2
            else:
                if self.matrix[self.cols2][self.rows2-1] == " " or self.matrix[self.cols2][self.rows2-1] == "*":
                    self.replace(self.cols2,self.rows2)
                    self.rows2 -= 1
                    self.turn = 1
        else:
            if self.matrix[self.cols1][self.rows1-1] == " " or self.matrix[self.cols1][self.rows1-1] == "*":
                self.replace(self.cols1,self.rows1)
                self.rows1 -= 1
        self.things()
    def moveRight(self):
        if self.multi == "2":
            if self.turn == 1:
                if self.matrix[self.cols1][self.rows1+1] == " " or self.matrix[self.cols1][self.rows1+1] == "*":
                    self.replace(self.cols1,self.rows1)
                    self.rows1 += 1
                    self.turn = 2
            else:
                if self.matrix[self.cols2][self.rows2+1] == " " or self.matrix[self.cols2][self.rows2+1] == "*":
                    self.replace(self.cols2,self.rows2)
                    self.rows2 += 1
                    self.turn = 1
        else:
            if self.matrix[self.cols1][self.rows1+1] == " " or self.matrix[self.cols1][self.rows1+1] == "*":
                self.replace(self.cols1,self.rows1)
                self.rows1 += 1
        self.things()
