import random
import lets
import remove_used_letters

class SakClass:

    def __init__(self):
        self.sak = []
        for i, x in lets.lets.items():
            tm = lets.lets[i]
            for j in range(tm):
                self.sak.append(i)

    def __len__(self):
        return len(self.sak)

    def randomize_sak(self):
        random.shuffle(self.sak)
        return self.sak

    def getletters(self):
        plst = []
        for i in range(7):
            plst.append(self.sak[i])
            self.sak.pop(i)
        return plst

    def getletters2(self, xer, word):
        plst= remove_used_letters.Remove_letters.remove_letters(xer, word)
        elipsh=7-len(plst)
        for i in range(elipsh):
            plst.append(self.sak[i])
            self.sak.pop(i)
        return plst

    def putbackletters(self, lst):
        plst = []
        for i in range(len(lst)):
            plst.append(self.sak[i])
            self.sak.pop(i)
            self.sak.append(lst[i])
        return plst