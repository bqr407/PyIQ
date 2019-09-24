# -*- coding: utf-8 -*-
"""
Ben Roux
Missouri State University

A series of cognitive games built using Python

"""
from tkinter import *
import tkinter.font
import time
import random


class Bubble():
    """Class for bubble objects"""

    def __init__(self, id, x, y, x2, y2, color):
        """each bubble object has these values associated with it"""
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
        self.id = id
        self.color = color

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

    def getColor(self):
        return self.color


class Game(Frame):

    def __init__(self):
        self.onMenu = False
        self.onInstructions = False
        self.menuItems = []
        self.instructionsItems = []
        Frame.__init__(self)
        self.master.title("Just a Math Game")
        self.grid()
        self.canvas_width = 800
        self.canvas_height = 400
        self.canvas = Canvas(self, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.grid(row=1, column=0)
        self.master.bind('<Left>', lambda event: self.leftAns(self))  # guess left key answer
        self.master.bind('<Right>', lambda event: self.rightAns(self))  # guess right key answer
        self.master.bind('<Up>', lambda event: self.upAns(self))  # guess up key answer
        self.master.bind('<Down>', lambda event: self.downAns(self))  # guess down key answer
        self.master.bind('<Return>', lambda event: self.returnEvent())  # guess down key answer
        self.drawMenu()

    def drawMenu(self):
        self.canvas.create_rectangle(130, 80, 670, 170, fill="orange", tags='mainMenu')
        self.canvas.create_text((400, 125), text="Just a Math Game", font=("Arial", 26), tags='mainMenu')
        self.canvas.create_rectangle(320, 230, 480, 280, fill="purple", tags='mainMenu')
        self.canvas.create_text((400, 255), text="Press Enter", font=("Arial", 18), tags='mainMenu')
        self.onMenu = True
        self.menuItems = ['mainTitle']

    def drawInstructions(self):
        self.canvas.create_rectangle(130, 50, 670, 250, fill="orange", tags='instruction')
        self.canvas.create_text((400, 145), text="Write Instructions Here", font=("Arial", 16), tags='instructions')
        self.canvas.create_rectangle(320, 290, 480, 340, fill="purple", tags='instructions')
        self.canvas.create_text((400, 315), text="Press Enter", font=("Arial", 18), tags='instructions')
        self.onInstructions = True
        self.instructionsItems = ['instructions']

    def drawGame(self):
        """Implement"""

    def startGame(self):
            self.canvas.delete('mainMenu')
            self.drawInstructions()

    def returnEvent(self):
        if self.onMenu:
            self.startGame()
            self.onMenu = False
        if self.onInstructions:
            self.drawGame()
            self.onInstructions = False

    # Check if the selected answer is right by comparing currentAnswer to the index of the selection in answerOptions
    # answerOptions = [leftOption, rightOption, upOption, downOption]
'''
    @staticmethod
    def leftAns(event):
        if answerOptions[0] == currentAnswer:
            #correct
        else:
            #wrong

    @staticmethod
    def rightAns(event):
        if answerOptions[1] == currentAnswer:
            #correct
        else:
            #wrong

    @staticmethod
    def upAns(event):
        if answerOptions[2] == currentAnswer:
            #correct
        else:
            #wrong

    @staticmethod
    def downAns(event):
        if answerOptions[3] == currentAnswer:
            #correct
        else:
            #wrong
'''

def main():
    Game().mainloop()

main()
