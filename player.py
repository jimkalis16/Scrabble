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
        self.skor = 0
        self.xeri = []
        self.name = name
        self.pskor = 0
        self.cskor = 0

    def string_brake(self, lexi):

        self.lex = [char for char in lexi]
        return self.lex

    def elenxos1(self, lex, xeri, lexi):
        flag1 = False
        # elenxos 1 an ta grammata iparxoun sto xeri
        result = all(elem in xeri for elem in lex)
        if (result):
            flag1 = True
        return flag1

    def elenxos2(self, lex, xeri, lexi):
        flag2 = False
    # elenxos 2 elenxei tin lexi sto arxio
        for i in words:
            if (lexi == i):
                flag2 = True
        return flag2

    def points(self, lex):
        pods = 0
        for i in range(len(lex)):
            for e, p in points.points.items():
                if (lex[i] == e):
                    ww = p
                    pods += ww
        self.skor += pods

        return pods

    def pscore(self):

        return self.pscore

    def cscore(self):

        return self.cscore