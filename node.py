
class Node:
    def __init__(self, type, playerRollCount, botRollCount, givenScore=-1):
        #0-bot, 1 -roll
        self.type = type
        self.playerRollCount = playerRollCount
        self.botRollCount = botRollCount
        self.nextNode = []
        self.givenScore = 0
        if givenScore != -1:
            self.givenScore = givenScore
