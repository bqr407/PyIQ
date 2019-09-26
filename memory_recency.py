# -*- coding: utf-8 -*-
"""
Ben Roux
Missouri State University

A series of cognitive games built using Python

"""
from tkinter import *
import time
import random


class Game(Frame):

    def __init__(self):
        self.onMenu = False
        self.onInstructions = False
        self.onGame = False
        self.onProblem = False
        self.finishedGame = False
        self.menuItems = []
        self.instructionsItems = []
        self.score = 0
        self.problemtime = 5.0
        self.problem = ""
        self.ansSubmitted = ""
        self.zeroago = ''
        self.oneago = ''
        self.twoago = ''
        self.threeago = ''
        self.problemNumber = 0
        self.numProblems = 20
        self.optionArr = []
        self.avgtimeArr = []
        Frame.__init__(self)
        self.master.title("PyIQ - Memory Recency")
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
        if not self.finishedGame:
            if self.optionArr[0] == self.answer:
                # Correct
                if self.problemtime > 0:
                    self.score += 1
            self.ansSubmitted = "1"

    @staticmethod
    def rightAns(self):
        if not self.finishedGame:
            if self.optionArr[1] == self.answer:
                # Correct
                if self.problemtime > 0:
                    self.score += 1
            self.ansSubmitted = "1"

    @staticmethod
    def leftAns(self):
        if not self.finishedGame:
            if self.optionArr[2] == self.answer:
                # Correct
                if self.problemtime > 0:
                    self.score += 1
            self.ansSubmitted = "1"

    @staticmethod
    def downAns(self):
        if not self.finishedGame:
            if self.optionArr[3] == self.answer:
                # Correct
                if self.problemtime > 0:
                    self.score += 1
            self.ansSubmitted = "1"

    def drawMenu(self):
        self.canvas.create_rectangle(self.canvas_width * .35, self.canvas_height * .3, self.canvas_width * .65,
                                     self.canvas_height * .5, tags='mainMenu')
        self.canvas.create_text((self.canvas_width * .5, self.canvas_height * .4), text="PyIQ - Memory Recency",
                                font=("Arial", 26), tags='mainMenu')
        self.canvas.create_rectangle(self.canvas_width * .45, self.canvas_height * .65, self.canvas_width * .55,
                                     self.canvas_height * .75, tags='mainMenu')
        self.canvas.create_text((self.canvas_width * .5, self.canvas_height * .7), text="Press Enter",
                                font=("Arial", 18), tags='mainMenu')
        self.onMenu = True
        self.menuItems = ['mainTitle']

    def drawInstructions(self):
        self.canvas.create_rectangle(self.canvas_width * .35, self.canvas_height * .2, self.canvas_width * .65,
                                     self.canvas_height * .6, tags='instructions')
        self.canvas.create_text((self.canvas_width * .5, self.canvas_height * .4), text="Write Instructions Here",
                                font=("Arial", 16), tags='instructions')
        self.canvas.create_rectangle(self.canvas_width * .45, self.canvas_height * .65, self.canvas_width * .55,
                                     self.canvas_height * .75, tags='instructions')
        self.canvas.create_text((self.canvas_width * .5, self.canvas_height * .7), text="Press Enter",
                                font=("Arial", 18), tags='instructions')
        self.onInstructions = True
        self.instructionsItems = ['instructions']

    def drawGame(self):
        """Implement"""

        def startingCountdown(time):
            if time < 1:
                self.canvas.delete('startingTimer')
                genProblem()
            else:
                self.canvas.create_text((self.canvas_width * .5, self.canvas_height * .5), text=str(time),
                                        font=("Arial", 48), tags='startingTimer')
                time -= 1
                self.canvas.update()
                self.canvas.after(1000)
                self.canvas.delete('startingTimer')
                startingCountdown(time)

        def updateGamePanel():
            if self.onGame:
                self.canvas.delete('gamePanel')
            if self.problemNumber <= self.numProblems:
                self.canvas.create_rectangle(self.canvas_width * .4, 0, self.canvas_width * .6, 80, tags='gamePanel')
                self.canvas.create_text((self.canvas_width * .003, 15),
                                        text="Problem " + str(self.problemNumber) + "/" + str(self.numProblems),
                                        font=("Arial", 18),
                                        tags='gamePanel', anchor='w')
                self.canvas.create_text((self.canvas_width * .5, 25), text="Score: " + str(self.score),
                                        font=("Arial", 18), tags='gamePanel')
                self.canvas.create_text((self.canvas_width * .5, 55),
                                        text="Time: " + str("{0:.1f}".format(self.problemtime)), font=("Arial", 18),
                                        tags='gamePanel')
            self.onGame = True

        def problemTimer():
            if self.ansSubmitted != "":
                self.ansSubmitted = ""
                self.avgtimeArr.append(5.0 - self.problemtime)
                genProblem()
            if self.problemtime < .1:
                updateGamePanel()
                self.avgtimeArr.append(5.0-self.problemtime)
                self.problemtime = 5.0
                genProblem()
            else:
                self.problemtime -= .1
                self.canvas.update()
                self.canvas.after(100)
                updateGamePanel()
                problemTimer()

        def displayScore():
            if self.onProblem:
                self.canvas.delete('problem')
                self.problemNumber += 1;
            if self.onGame:
                self.canvas.delete('gamePanel')
            if not self.finishedGame:
                self.canvas.create_text((self.canvas_width * .5, self.canvas_height * .4),
                                        text="Final Score: " + str(self.score), font=("Arial", 18), tags='scorePanel')
                avgtime = 0.0
                for x in range(len(self.avgtimeArr)):
                    avgtime = avgtime + self.avgtimeArr[x]
                self.canvas.create_text((self.canvas_width * .5, self.canvas_height * .4),
                                        text="Final Score: " + str(self.score), font=("Arial", 18), tags='scorePanel')
                self.canvas.create_text((self.canvas_width * .5, self.canvas_height * .5),
                                        text="Total Time: " + str("{0:.1f}".format(avgtime)) + " seconds", font=("Arial", 18), tags='scorePanel')
                avgtime = avgtime / len(self.avgtimeArr)
                self.canvas.create_text((self.canvas_width * .5, self.canvas_height * .6),
                                        text="Average Time per Question: " + str("{0:.1f}".format(avgtime)) + " seconds", font=("Arial", 18), tags='scorePanel')
                self.finishedGame = True

        def displayProblem():
            # If there is a problem already displayed we need to remove it first
            if self.problemNumber <= self.numProblems:
                if self.onProblem:
                    self.canvas.delete('problem')
                # Display the problem here
                self.canvas.create_text((self.canvas_width * .5, self.canvas_height * .4), text=self.problem,
                                        font=("Arial", 30), tags='problem')
                # Display option A
                self.canvas.create_image(self.canvas_width * .3, self.canvas_height * .7, image=self.upImg,
                                         tags='problem')
                self.canvas.create_text((self.canvas_width * .3, self.canvas_height * .8), text=str(self.optionArr[0]),
                                        font=("Arial", 30), tags='problem')
                # Display option B
                self.canvas.create_image(self.canvas_width * .425, self.canvas_height * .7, image=self.rightImg,
                                         tags='problem')
                self.canvas.create_text((self.canvas_width * .425, self.canvas_height * .8), text=str(self.optionArr[1]),
                                        font=("Arial", 30), tags='problem')
                # Display option C
                self.canvas.create_image(self.canvas_width * .575, self.canvas_height * .7, image=self.leftImg,
                                         tags='problem')
                self.canvas.create_text((self.canvas_width * .575, self.canvas_height * .8), text=str(self.optionArr[2]),
                                        font=("Arial", 30), tags='problem')
                # Display option D
                self.canvas.create_image(self.canvas_width * .7, self.canvas_height * .7, image=self.downImg,
                                         tags='problem')
                self.canvas.create_text((self.canvas_width * .7, self.canvas_height * .8), text=str(self.optionArr[3]),
                                        font=("Arial", 30), tags='problem')
                self.onProblem = True

        def genProblem():
            self.problemtime = 5.0
            if self.problemNumber < self.numProblems:  # If the player still has more problems left
                updateGamePanel()
                self.problemNumber += 1
                randomnamesArr = ['Andrew', 'Parker', 'Ryan', 'Brendan']
                random.shuffle(randomnamesArr)
                ans = ''
                name = str(randomnamesArr[random.randint(0, len(randomnamesArr) - 1)])
                if self.problemNumber < 4:
                    problem = name + "\n (What's this name?)"
                    if self.zeroago == '':
                        self.zeroago = name
                    elif self.oneago == '':
                        self.oneago = self.zeroago
                        self.zeroago = name
                    elif self.twoago == '':
                        self.twoago = self.oneago
                        self.oneago = self.zeroago
                        self.zeroago = name
                    else:
                        self.threeago = self.twoago
                        self.twoago = self.oneago
                        self.oneago = self.zeroago
                        self.zeroago = name
                    ans = self.zeroago
                else:
                    backwards = random.randint(1, 3)
                    if backwards == 1:
                        problem = str(randomnamesArr[random.randint(0, len(randomnamesArr) - 1)]) + "\n (What was the previous name?)"
                        self.threeago = self.twoago
                        self.twoago = self.oneago
                        self.oneago = self.zeroago
                        self.zeroago = name
                        ans = self.oneago
                    if backwards == 2:
                        problem = str(randomnamesArr[random.randint(0, len(randomnamesArr) - 1)]) + "\n (What was the name two times ago?)"
                        self.threeago = self.twoago
                        self.twoago = self.oneago
                        self.oneago = self.zeroago
                        self.zeroago = name
                        ans = self.twoago
                    if backwards == 3:
                        problem = str(randomnamesArr[random.randint(0, len(randomnamesArr) - 1)]) + "\n (What was the name three times ago?)"
                        self.threeago = self.twoago
                        self.twoago = self.oneago
                        self.oneago = self.zeroago
                        self.zeroago = name
                        ans = self.threeago
                print(["Current: " + str(self.zeroago)], ["1 Ago: " + str(self.oneago)], ["2 Ago: " + str(self.twoago)], ["3 Ago: " + str(self.threeago)])
                self.problem = problem
                self.answer = ans
                self.optionArr = randomnamesArr
                displayProblem()
                problemTimer()
            else:  # Player has done all the problems, show score
                print('hi')
                displayScore()

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
