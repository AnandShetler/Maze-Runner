'''
Created on Oct 10, 2015

@author: Anand Shetler
'''
import time
import random

print("Welcome to MAZE RUNNER. Complete the maze as fast as you can. Try to go over the * to reduce your time.\nYou move the 0 with WASD and pressing enter. Avoid the H's.")
columns = int(input("How many rows and columns should the maze have?"))
gmode = input("Would you like to play on hard or easy mode?").lower()
multi = int(input("Would you like to play with 1 or 2 players? If you choose two players you will race against each other."))
while gmode != "easy" and gmode != "hard":
    gmode = input("Enter easy or hard for the game mode.")
bonuscol = random.randint(0,columns-1)
bonusrow = random.randint(0,columns-1)
claimedbonus = False
bonus = columns
rows = columns
user1 = "1"
start = time.time()
matrix = [[0 for x in range(columns)]for x in range(rows)]

for y in range(columns):
    for i in range(rows):
        matrix[i][y] = random.randint(0,2)
        if matrix[i][y] == 1 or matrix[i][y] == 0:
            matrix[i][y] = " "
        elif matrix[i][y] == 2:
            matrix[i][y] = "H"
matrix[0][rows-1] = user1
if multi == 2:
    user2 = "2"
    matrix[0][0] = user2
    userpos2 = matrix[0][0]
col2 = 0
ro2 = 0
userpos = matrix[0][rows-1]
col = 0
ro = rows-1
turn = 1
matrix[bonuscol][bonusrow] = "*"
for row in matrix:
    print(row)
while col != rows-1:
    direction = input("Use WASD and press enter to move\n")
    while direction != "w" and direction != "a" and direction != "s" and direction != "d":
        direction = input("Enter WASD, YOU JERK!!!!!!\n")
    if direction == "w" and ((matrix[col-1][ro] != "H" and turn == 1) or (matrix[col2-1][ro2] != "H" and turn == 2)):
        if multi == 2:
            if turn == 1:
                if gmode == "easy":
                    matrix[col][ro] = " "
                elif gmode == "hard":
                    matrix[col][ro] = "H"
                col -= 1
                userpos = matrix[col][ro]
                turn = 2
            else:
                if gmode == "easy":
                    matrix[col2][ro2] = " "
                elif gmode == "hard":
                    matrix[col2][ro2] = "H"
                col2 -= 1
                userpos2 = matrix[col2][ro2]
                turn = 1
        else:
            if gmode == "easy":
                    matrix[col][ro] = " "
            elif gmode == "hard":
                matrix[col][ro] = "H"
            col -= 1
            userpos = matrix[col][ro]
    elif direction == "a" and ((matrix[col][ro-1] != "H" and turn == 1) or (matrix[col2][ro2-1] != "H" and turn == 2)):
        if multi == 2:
            if turn == 1:
                if gmode == "easy":
                    matrix[col][ro] = " "
                elif gmode == "hard":
                    matrix[col][ro] = "H"
                ro -= 1
                userpos = matrix[col][ro]
                turn = 2
            else:
                if gmode == "easy":
                    matrix[col2][ro2] = " "
                elif gmode == "hard":
                    matrix[col2][ro2] = "H"
                ro2 -= 1
                userpos2 = matrix[col2][ro2]
                turn = 1
        else:
            if gmode == "easy":
                    matrix[col][ro] = " "
            elif gmode == "hard":
                matrix[col][ro] = "H"
            ro -= 1
            userpos = matrix[col][ro]
    elif direction == "s" and ((matrix[col+1][ro] != "H" and turn == 1) or (matrix[col2+1][ro2] != "H" and turn == 2)):
        if multi == 2:
            if turn == 1:
                if gmode == "easy":
                    matrix[col][ro] = " "
                elif gmode == "hard":
                    matrix[col][ro] = "H"
                col += 1
                userpos = matrix[col][ro]
                turn = 2
            else:
                if gmode == "easy":
                    matrix[col2][ro2] = " "
                elif gmode == "hard":
                    matrix[col2][ro2] = "H"
                col2 += 1
                userpos2 = matrix[col2][ro2]
                turn = 1
        else:
            if gmode == "easy":
                    matrix[col][ro] = " "
            elif gmode == "hard":
                matrix[col][ro] = "H"
            col += 1
            userpos = matrix[col][ro]
    elif direction == "d" and ((matrix[col][ro+1] != "H" and turn == 1) or (matrix[col2][ro2+1] != "H" and turn == 2)):
        if multi == 2:
            if turn == 1:
                if gmode == "easy":
                    matrix[col][ro] = " "
                elif gmode == "hard":
                    matrix[col][ro] = "H"
                ro += 1
                userpos = matrix[col][ro]
                turn = 2
            else:
                if gmode == "easy":
                    matrix[col2][ro2] = " "
                elif gmode == "hard":
                    matrix[col2][ro2] = "H"
                ro2 += 1
                userpos2 = matrix[col2][ro2]
                turn = 1
        else:
            if gmode == "easy":
                    matrix[col][ro] = " "
            elif gmode == "hard":
                matrix[col][ro] = "H"
            ro += 1
            userpos = matrix[col][ro]
    else:
        print("You can't move there.")
    matrix[col][ro] = user1
    if multi == 2:
        matrix[col2][ro2] = user2
        user2 = matrix[col2][ro2]
    user1 = matrix[col][ro]
    for row in matrix:
        print(row)
end = time.time()
if matrix[col][ro] == "*" or matrix[col2][ro2] == "*":
        claimedbonus = True
if claimedbonus == True:
    print("U DA TRUE MVP!! Good job collecting the bonus. Your time is "+str(round(end-start-bonus,0))+" seconds.")
else:
    print("Great job, you finished in " + str(round(end-start,1)) + " seconds.")