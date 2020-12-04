import random

class Game:
    def __int__(self):
        self.Round = 1
        self.Score = 0
        self.RollCount = 0
        self.playerHand = []
        self.botHand = []

    def diceRoll(self):
        return [random.randint(1, 6),
                random.randint(1, 6), random.randint(1, 6),
                random.randint(1, 6), random.randint(1, 6)]

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

    def nextRound(self):
        self.Round += 1
        self.Score = 0
        self.RollCount = 0
        self.playerHand = []
        self.botHand = []