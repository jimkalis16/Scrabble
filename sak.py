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
        plist = []
        for i in range(7):
            plist.append(self.sak[i])
            self.sak.pop(i)
        return plist

    def getletters2(self, hand, word):
        plist= remove_used_letters.Remove_letters.remove_letters(hand, word)
        elipsh=7-len(plist)
        for i in range(elipsh):
            plist.append(self.sak[i])
            self.sak.pop(i)
        return plist

    def putbackletters(self, list):
        plist = []
        for i in range(len(list)):
            plist.append(self.sak[i])
            self.sak.pop(i)
            self.sak.append(list[i])
        return plist