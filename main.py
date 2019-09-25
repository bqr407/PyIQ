# -*- coding: utf-8 -*-
"""
Ben Roux
Missouri State University

A series of cognitive games built using Python

"""
from tkinter import *
import time
import random


class Bubble():
    """Class for bubble objects"""

    def __init__(self, id, x, y, x2, y2, value):
        """each bubble object has these values associated with it"""
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
        self.id = id
        self.value = value

    def getX(self):
        """returns x1 of tkinter shape"""
        return self.x

    def getY(self):
        """returns y1 of tkinter shape"""
        return self.y

    def getX2(self):
        """returns x2 pos of tkinter shape"""
        return self.x2

    def getY2(self):
        """returns y2 of tkinter shape"""
        return self.y2

    def getID(self):
        """returns unique object identifier"""
        return self.id

    def getValue(self):
        """returns value of the bubble"""
        return self.value

class Choice():
    """Class for choice objects"""

    def __init__(self, id, x, y, x2, y2, value):
        """each choice object has these values associated with it"""
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
        self.id = id
        self.value = value

    def getX(self):
        """returns x1 of tkinter shape"""
        return self.x

    def getY(self):
        """returns y1 of tkinter shape"""
        return self.y

    def getX2(self):
        """returns x2 pos of tkinter shape"""
        return self.x2

    def getY2(self):
        """returns y2 of tkinter shape"""
        return self.y2

    def getID(self):
        """returns unique object identifier"""
        return self.id

    def getValue(self):
        """returns answer the object represents"""
        return self.value

class Game(Frame):

    def __init__(self):
        self.onMenu = False
        self.onInstructions = False
        self.onGame = False
        self.onProblem = False
        self.menuItems = []
        self.instructionsItems = []
        self.score = 0
        self.problemtime = 5.0
        self.smallBubbleSize = 50
        self.bigBubbleSize = 200
        self.problem = ""
        self.ansSubmitted = ""
        self.answer = 0
        self.optionArr = []
        Frame.__init__(self)
        self.master.title("Just a Math Game")
        self.grid()
        self.canvas_width = 1366
        self.canvas_height = 702
        self.canvas = Canvas(self, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.grid(row=1, column=0)
        self.master.bind('<Left>', lambda event: self.leftAns(self))  # guess left key answer
        self.master.bind('<Right>', lambda event: self.rightAns(self))  # guess right key answer
        self.master.bind('<Up>', lambda event: self.upAns(self))  # guess up key answer
        self.master.bind('<Down>', lambda event: self.downAns(self))  # guess down key answer
        self.master.bind('<Return>', lambda event: self.returnEvent())  # guess down key answer
        self.answerBoxSize = 75
        self.upImg = PhotoImage(file='upImg.png')
        self.downImg = PhotoImage(file='downImg.png')
        self.leftImg = PhotoImage(file='leftImg.png')
        self.rightImg = PhotoImage(file='rightImg.png')
        self.drawMenu()

    # Check if the selected answer is right by comparing currentAnswer to the index of the selection in answerOptions
    # answerOptions = [leftOption, rightOption, upOption, downOption]
    @staticmethod
    def upAns(self):
        print('up')
        if self.optionArr[0] == self.answer:
            # Correct
            print("correct")
            if self.problemtime > 0:
                self.score += 1
        else:
            # Wrong
            print("wrong")
        self.ansSubmitted = "1"

    @staticmethod
    def rightAns(self):
        print('right')
        if self.optionArr[1] == self.answer:
            # Correct
            print("correct")
            if self.problemtime > 0:
                self.score += 1
        else:
            # Wrong
            print("wrong")
        self.ansSubmitted = "1"
            
    @staticmethod
    def leftAns(self):
        print('left')
        if self.optionArr[2] == self.answer:
            # Correct
            print("correct")
            if self.problemtime > 0:
                self.score += 1
        else:
            # Wrong
            print("wrong")
        self.ansSubmitted = "1"

    @staticmethod
    def downAns(self):
        print('down')
        if self.optionArr[3] == self.answer:
            # Correct
            print("correct")
            if self.problemtime > 0:
                self.score += 1
        else:
            # Wrong
            print("wrong")
        self.ansSubmitted = "1"

    def drawMenu(self):
        self.canvas.create_rectangle(self.canvas_width*.35, self.canvas_height*.3, self.canvas_width*.65, self.canvas_height*.5, tags='mainMenu')
        self.canvas.create_text((self.canvas_width*.5, self.canvas_height*.4), text="Just a Math Game", font=("Arial", 26), tags='mainMenu')
        self.canvas.create_rectangle(self.canvas_width*.45, self.canvas_height*.65, self.canvas_width*.55, self.canvas_height*.75, tags='mainMenu')
        self.canvas.create_text((self.canvas_width*.5, self.canvas_height*.7), text="Press Enter", font=("Arial", 18), tags='mainMenu')
        self.onMenu = True
        self.menuItems = ['mainTitle']

    def drawInstructions(self):
        self.canvas.create_rectangle(self.canvas_width*.35, self.canvas_height*.2, self.canvas_width*.65, self.canvas_height*.6, tags='instructions')
        self.canvas.create_text((self.canvas_width*.5, self.canvas_height*.4), text="Write Instructions Here", font=("Arial", 16), tags='instructions')
        self.canvas.create_rectangle(self.canvas_width*.45, self.canvas_height*.65, self.canvas_width*.55, self.canvas_height*.75, tags='instructions')
        self.canvas.create_text((self.canvas_width*.5, self.canvas_height*.7), text="Press Enter", font=("Arial", 18), tags='instructions')
        self.onInstructions = True
        self.instructionsItems = ['instructions']

    def drawGame(self):
        """Implement"""

        def startingCountdown(time):
            if time < 1:
                self.canvas.delete('startingTimer')
                genProblem()
            else:
                self.canvas.create_text((self.canvas_width*.5, self.canvas_height*.5), text=str(time), font=("Arial", 48), tags='startingTimer')
                time -= 1
                self.canvas.update()
                self.canvas.after(1000)
                self.canvas.delete('startingTimer')
                startingCountdown(time)

        def updateGamePanel():
            if self.onGame:
                self.canvas.delete('gamePanel')
            self.canvas.create_rectangle(self.canvas_width*.4, 0, self.canvas_width*.6, 80, tags='gamePanel')
            self.canvas.create_text((self.canvas_width*.5, 25), text="Score: " + str(self.score), font=("Arial", 18), tags='gamePanel')
            self.canvas.create_text((self.canvas_width*.5, 55), text="Time: " + str("{0:.1f}".format(self.problemtime)), font=("Arial", 18),
                                    tags='gamePanel')
            self.onGame = True

        def problemTimer():
            if self.ansSubmitted != "":
                self.ansSubmitted = ""
                genProblem()
            if self.problemtime < .1:
                updateGamePanel()
                self.problemtime = 5.0
                genProblem()
            else:
                self.problemtime -= .1
                self.canvas.update()
                self.canvas.after(100)
                updateGamePanel()
                problemTimer()

        def displayProblem():
            # If there is a problem already displayed we need to remove it first
            if self.onProblem:
                self.canvas.delete('problem')
            # Display the problem here
            self.canvas.create_text((self.canvas_width*.5, self.canvas_height*.4), text=self.problem, font=("Arial", 30), tags='problem')
            # Display option A
            self.canvas.create_image(self.canvas_width*.35, self.canvas_height*.7, image=self.upImg, tags='problem')
            self.canvas.create_text((self.canvas_width*.35, self.canvas_height*.8), text=str(self.optionArr[0]), font=("Arial", 30), tags='problem')
            # Display option B
            self.canvas.create_image(self.canvas_width*.45, self.canvas_height*.7, image=self.rightImg, tags='problem')
            self.canvas.create_text((self.canvas_width*.45, self.canvas_height*.8), text=str(self.optionArr[1]), font=("Arial", 30), tags='problem')
            # Display option C
            self.canvas.create_image(self.canvas_width*.55, self.canvas_height*.7, image=self.leftImg, tags='problem')
            self.canvas.create_text((self.canvas_width*.55, self.canvas_height*.8), text=str(self.optionArr[2]), font=("Arial", 30), tags='problem')
            # Display option D
            self.canvas.create_image(self.canvas_width*.65, self.canvas_height*.7, image=self.downImg, tags='problem')
            self.canvas.create_text((self.canvas_width*.65, self.canvas_height*.8), text=str(self.optionArr[3]), font=("Arial", 30), tags='problem')
            self.onProblem = True

        def genProblem():
            self.problemtime = 5.0
            updateGamePanel()
            x = 0
            y = 0
            type = random.randint(1, 3)
            problem = ""
            optionArr = []
            if type == 1:
                x = random.randint(1, 50)
                y = random.randint(1, 50)
                ans = x+y
                problem = str(x) + "+" + str(y)
                optionArr = [ans, ans+random.randint(-20, 20),  ans+random.randint(-20, 20),  ans+random.randint(-20, 20)]
            if type == 2:
                x = random.randint(1, 50)
                y = random.randint(1, 50)
                ans = x-y
                problem = str(x) + "-" + str(y)
                optionArr = [ans, ans+random.randint(-20, 20),  ans+random.randint(-20, 20),  ans+random.randint(-20, 20)]
            if type == 3:
                x = random.randint(1, 10)
                y = random.randint(1, 10)
                ans = x*y
                problem = str(x) + "x" + str(y)
                optionArr = [ans, ans+random.randint(-20, 20),  ans+random.randint(-20, 20),  ans+random.randint(-20, 20)]
            optionArr.sort()
            self.problem = problem
            self.answer = ans
            self.optionArr = optionArr
            displayProblem()
            problemTimer()

        if self.onInstructions:
            self.onInstructions = False
        self.canvas.delete('instructions')
        updateGamePanel()
        startingCountdown(5)


    def startGame(self):
        if self.onMenu:
            self.onMenu = False
        self.canvas.delete('mainMenu')
        self.drawInstructions()



    def returnEvent(self):
        if self.onInstructions:
            self.drawGame()
        if self.onMenu:
            self.startGame()




def main():
    Game().mainloop()

main()
