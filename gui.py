from tkinter import *


class Gui:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("340x440")
        headerFont = ("Times New Roman", 16, "bold")
        simpleFont = ("Times New Roman", 16)

        playerLabel = Label(self.root, text="Player", width=8, height=1, font=headerFont)
        playerLabel.grid(row=0, column=0)
        totalLabel = Label(self.root, text=":", width=4, height=1, font=headerFont)
        totalLabel.grid(row=0, column=1)
        botLabel = Label(self.root, text="AI", width=8, height=1, font=headerFont)
        botLabel.grid(row=0, column=2)

        self.playerHist = Text(self.root, width=8, height=9, font=simpleFont, state="disabled")
        self.playerHist.grid(row=1, column=0)
        self.scoreHist = Text(self.root, width=4, heigh=9, font=headerFont, state="disabled")
        self.scoreHist.grid(row=1, column=1)
        self.botHist = Text(self.root, width=8, height=9, font=simpleFont, state="disabled")
        self.botHist.grid(row=1, column=2)

        self.playerButtonRoll = Button(self.root, text="Roll Dice", font=simpleFont, width=21)
        self.playerButtonRoll.grid(row=2, column=0, columnspan=3)
        self.playerButtonAccept = Button(self.root, width=21, font=simpleFont, text="Accept Roll", state="disabled")
        self.playerButtonAccept.grid(row=3, column=0, columnspan=3)

    def pushPlayerHist(self, array):
        self.playerHist.configure(state="normal")
        self.playerHist.insert(END, "{}-{}-{}-{}-{}"
                               .format(array[0], array[1], array[2], array[3], array[4]))
        self.playerHist.configure(state="disabled")

    def pushBotHist(self, array):
        self.botHist.configure(state="normal")
        self.botHist.insert(END, "{}-{}-{}-{}-{}"
                            .format(array[0], array[1], array[2], array[3], array[4]))
        self.botHist.configure(state="disabled")

    def pushScoreHist(self, score, rollCount):
        scoreStr = ""
        for i in range(1, rollCount):
            scoreStr += "  --\n"
        if score > 0:
            scoreStr += " +"
        elif score == 0:
            scoreStr += "  "
        else:
            scoreStr += " "
        scoreStr += "{}\n".format(score)
        self.scoreHist.configure(state="normal")
        self.scoreHist.insert(END, scoreStr)
        self.scoreHist.configure(state="disabled")
