import random
import lets
import remove_used_letters

class SakClass:

    # κατασκευαστης σακουλι με γραμματα
    def __init__(self):
        self.sak = []
        for i, x in lets.lets.items():
            tm = lets.lets[i]
            for j in range(tm):
                self.sak.append(i)

    def __len__(self):
        return len(self.sak)

    # ανακατευει το σακουλι με γραμματα
    def randomize_sak(self):
        random.shuffle(self.sak)
        return self.sak

    # δινει 7 γραμματα στο χερι (hand)
    def getletters(self):
        plist = []
        for i in range(7):
            plist.append(self.sak[i])
            self.sak.pop(i)
        return plist

    # δεχεται το χερι (hand) και την λεξη που παιχτηκε (word) και αντικαταστει στο χερι (hand) γραμματα που εχουν παιχτει
    def getletters2(self, hand, word):
        plist= remove_used_letters.Remove_letters.remove_letters(hand, word)
        elipsh=7-len(plist)
        for i in range(elipsh):
            plist.append(self.sak[i])
            self.sak.pop(i)
        return plist

    # χρεισιμοποιειται κυριως στο πασω και αλλαζει ολα τα γραμματα απο το χερι
    def putbackletters(self, list):
        plist = []
        for i in range(len(list)):
            plist.append(self.sak[i])
            self.sak.pop(i)
            self.sak.append(list[i])
        return plist