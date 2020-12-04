from gui import *
from tkinter import messagebox
import random


class Game:
    def __init__(self):
        self.gui = Gui()
        self.gui.playerButtonRoll.configure(command=self.playerRoll)
        self.gui.playerButtonAccept.configure(command=self.botRoll)

        self.Round = 1
        self.Score = 0
        self.RollCount = 0
        self.botRollCount = 0
        self.playerHand = []
        self.botHand = []

    def diceRoll(self):
        return [random.randint(1, 6),
                random.randint(1, 6), random.randint(1, 6),
                random.randint(1, 6), random.randint(1, 6)]

    def playerRoll(self):
        self.RollCount += 1
        self.playerHand = self.diceRoll()
        self.gui.pushPlayerHist(self.playerHand)
        self.gui.playerButtonAccept.configure(state="normal")
        if self.RollCount == 3:
            self.gui.playerButtonRoll.configure(state="disabled")

    def botRoll(self):
        #Only one roll available => simple response
        if self.RollCount == 1:
            self.botRollCount += 1
            self.botHand = self.diceRoll()
            self.gui.pushBotHist(self.botHand)
        #More than one roll available, but on on first round => trying to keep up
        elif self.RollCount > 1 and self.Round == 1:
            self.botRollCount += 1
            self.botHand = self.diceRoll()
            self.gui.pushBotHist(self.botHand)
            if self.countScore() > 2:
                while self.botRollCount <= self.RollCount:
                    self.botRollCount += 1
                    self.botHand = self.diceRoll()
                    self.gui.pushBotHist(self.botHand)
                    if self.countScore() <= 2:
                        break
        #More than one roll available and its second or third round => minimax
        else:
            pass
        self.nextRound()

    def evalRoll(self, roll):
        unique = set(roll)
        if len(unique) == 1:
            return 6
        elif len(unique) == 2:
            present = list(unique)
            counter = 0
            for item in roll:
                if item == present[0]:
                    counter += 1
            if counter == 1 or counter == 4:
                return 5
            else:
                return 4
        elif len(unique) == 3:
            present = list(unique)
            counter = [0, 0, 0]
            for i in range(0, len(present)):
                for dice in roll:
                    if present[i] == dice:
                        counter[i] += 1
            if counter[0] == 2 or counter[1] == 2 or counter[2] == 2:
                return 2
            else:
                return 3
        elif len(unique) == 4:
            return 1
        else:
            return 0

    def countScore(self):
        return self.evalRoll(self.playerHand) - self.evalRoll(self.botHand)

    def nextRound(self):
        #Refresh Score
        self.Score += self.countScore()
        self.gui.pushScoreHist(self.Score, self.RollCount)
        self.gui.pushBotNewLine(self.RollCount - self.botRollCount)
        #If game ends
        if self.Round == 3:
            self.gui.playerButtonRoll.configure(state="disabled")
            self.gui.playerButtonAccept.configure(state="disabled")
            if self.Score > 0:
                result = "You won!"
            elif self.Score == 0:
                result = "Draw!"
            else:
                result = "You lost!"
            messagebox.showinfo("Results", result)
        #If game continues
        else:
            self.Round += 1
            self.RollCount = 0
            self.botRollCount = 0
            self.playerHand = []
            self.botHand = []
            self.gui.playerButtonRoll.configure(state="normal")
            self.gui.playerButtonAccept.configure(state="disabled")
