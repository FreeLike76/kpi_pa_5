from node import *

class Tree:
    def __init__(self, playerRollCount, botRollCount, currentbotScore):
        self.root = Node(0, playerRollCount, botRollCount, currentbotScore)
        self.chances = [720, 3600, 1800, 1200, 300, 150, 6]
        self.currentbotScore = currentbotScore
        self.build(self.root)

    def build(self, node):
        if node.type == 0 and node.playerRollCount > node.botRollCount:
            node.nextNode.append(Node(node.type, 2, node.playerRollCount, node.botRollCount + 1))
            self.build(node.nextNode[0])

        elif node.type == 2:
            for i in range(0, len(self.chances)):
                node.nextNode.append(Node(node.type, node.playerRollCount, node.botRollCount, i))
                self.build(node.nextNode[i])

    def evaluate(self, node):
        for child in node.nextNode:
            self.evaluate(child)
        if node.type == 0:
            if not node.nextNode:
                return node.givenScore
            else:
                return max(node.givenScore, node.nextNode[0].givenScore)
        elif node.type == 1:
            for i in range(0, len(self.chances)):
                node.givenScore += node.nextNode[i].givenScore * self.chances[i] / 7776
            return node.givenScore

    def decide(self):
        if self.currentbotScore >= self.evaluate(self.root):
            return 0
        else:
            return 1
