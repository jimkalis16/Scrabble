import json


# code pou pernei lexeis apo to greek7.txt kai tis bazei se lista
import points

with open('score.json', 'r', encoding="utf-8") as fin:
    highskors = json.load(fin)

words = []
with open('greek7.txt', 'r', encoding="utf-8") as f7:
    for line in f7:
        words.append(line.strip('\n'))


class Player:

    def __init__(self, name):
        self.score = 0
        self.hand = []
        self.name = name
        self.pscore = 0
        self.cscore = 0

    def string_brake(self, word):

        self.word = [char for char in word]
        return self.word

    def elenxos1(self, letters, hand):
        flag1 = False
        # elenxos 1 an ta grammata iparxoun sto xeri
        result = all(elem in hand for elem in letters)
        if (result):
            flag1 = True
        return flag1

    def elenxos2(self, word):
        flag2 = False
    # elenxos 2 elenxei tin lexi sto arxio
        for i in words:
            if (word == i):
                flag2 = True
        return flag2

    def points(self, word):
        point = 0
        for i in range(len(word)):
            for e, p in points.points.items():
                if (word[i] == e):
                    ww = p
                    point += ww
        self.score += point

        return point

    def pscore(self):

        return self.pscore

    def cscore(self):

        return self.cscore