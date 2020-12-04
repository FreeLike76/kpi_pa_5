from tkinter import *
from game import *

class Gui:
    def __init__(self):
        self.Game= Game()
        self.root = Tk()
        self.root.geometry("340x440")
        headerFont = ("Times New Roman", 16, "bold")
        simpleFont = ("Times New Roman", 16)
        playerLabel = Label(self.root, text="Player", width=8, height=1, font=headerFont)\
            .grid(row=0, column=0)
        totalLabel = Label(self.root, text=":", width=4, height=1, font=headerFont)\
            .grid(row=0, column=1)
        botLabel = Label(self.root, text="AI", width=8, height=1, font=headerFont)\
            .grid(row=0, column=2)
        self.playerHist = Text(self.root, width=8, height=9, font=simpleFont, state="disabled")\
            .grid(row=1, column=0)
        self.resultHist = Text(self.root, width=4, heigh=9, font=headerFont, state="disabled")\
            .grid(row=1, column=1)
        self.botHist = Text(self.root, width=8, height=9, font=simpleFont, state="disabled")\
            .grid(row=1, column=2)
        self.playerRoll = Button(self.root, text="Roll Dice", font=simpleFont, width=21, command=self.playerRoll)\
            .grid(row=2, column=0, columnspan=3)
        self.playerAccept = Button(self.root, text="Accept Roll", font=simpleFont, width=21)\
            .grid(row=3, column=0, columnspan=3)

    def playerRoll(self):
        self.Game.playerHand = self.Game.diceRoll()
        self.playerHist.insert(END,"{}-{}-{}-{}-{}\n".format(self.Game.playerHand))
        if self.Game.RollCount == 3:
