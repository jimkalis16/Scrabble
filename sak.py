import random
import lets


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

    def getletters(self, gra):
        plst = []
        for i in range(gra):
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
