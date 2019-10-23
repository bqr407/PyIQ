from tkinter import *
import random
import bubble

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
        self.master.title("Bubble Math")
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
        self.genBubble()

    def drawBubble(self, genbub):
        rect1 = self.canvas.create_oval(genbub.getX(), genbub.getY(), genbub.getX2(), genbub.getY2())
        y = genbub.getY()
        print(y)

    def genBubble(self):
        genbub = bubble.Bubble(1, 50, 50, 100, 100, 20)
        self.drawBubble(genbub)



def main():
    Game().mainloop()

main()