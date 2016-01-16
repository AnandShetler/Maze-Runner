'''
Created on Jan 9, 2016

@author: Anand Shetler
'''

import tkinter
from MainScreen import MainSc
from mazePage import MazePage
from finishedMaze import LastSc

class MazeManager(object):
    def __init__(self):
        self.root = tkinter.Tk()
    def setupMainScreen(self):
        self.root.title("Welcome To Maze Runner!")
        self.mainsc = MainSc(self.root, self.oncloseMainSc)
    def oncloseMainSc(self, cols, multi, gmode):
        cols = int(cols)
        self.mainsc.destroy()
        self.root.title("Maze Runner")
        self.maze = MazePage(self.root, cols, multi, gmode, self.oncloseMaze)
    def oncloseMaze(self, start, end, claimed, cols, multi):
        self.maze.destroy()
        self.root.title("Maze Runner")
        self.done = LastSc(self.root, start, end, claimed, cols, multi, self.oncloseLastSc)
    def oncloseLastSc(self):
        self.done.destroy()
        self.setupMainScreen()
def main():
    maze = MazeManager()
    maze.setupMainScreen()
    maze.root.mainloop()
main()
