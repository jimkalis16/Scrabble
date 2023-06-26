from computer import Computer
from human import Human
from player import words, highskors
from sak import SakClass
import json


# κατασκευαστης μιας παρτιδας παιχνιδιου
class Game:

    def __init__(self):
        self.phand = []
        self.pscore = 0
        self.chand = []
        self.cscore = 0
        self.con = "pc"

    # αρχικοποιει το sak και παιρνει το ονομα του παικτη
    def setup(self):
        self.pln = input("Ονομα παικtη:")
        self.sak = SakClass()
        self.sak.randomize_sak()
        self.phand = self.sak.getletters()
        self.chand = self.sak.getletters()
        self.pl1 = Human(self.pln)
        self.com = Computer("pc")
        print(
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        )
        print(
            "Καλοσορισες", self.pln,
            " σε παιχνιδι scrambble εναντια σε εναν υπολογιστη, καλη διασκεδαση")
        print(
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        )
        self.run()

    # τρεχει μεχρι να κλεισει ή να τελιοσουν τα γραμματα με ολους τους κανονες του παιχνιδιου
    def run(self):
        self.pl1.hprint(self.phand)
        self.word = input("Λεξη: ")
        while (self.word != "q" or len(self.sak) < 7):
            # code for player turn
            flagp = self.pl1.hplay(self.word, self.phand)
            if (flagp == True):
                self.phand = self.phand + self.sak.getletters2(self.phand, self.word)
                self.pscore += self.pl1.points(self.pl1.string_brake(self.word))
            else:
                self.sak.putbackletters(self.phand)
                self.phand = self.sak.getletters()

            # code for computer turn
            flagc = self.com.cplay(self.chand)
            if (flagc == True):
                cl = self.com.alg(self.chand, words)
                self.chand =self.sak.getletters2(self.chand, cl)
                self.cscore += self.com.points(self.pl1.string_brake(cl))
            else:
                self.sak.putbackletters(self.chand)
                self.chand = self.sak.getletters()

            # code for player turn and end of while
            self.pl1.hprint(self.phand)
            self.word = input("Λεξη: ")

        self.end()

    #μετραει ποντους βρισκει και ανακηρισει νικητη μετα παιρνει τα δεδομενα και τα αποθηκευει στο score.json
    def end(self):
        print("Παικτης: ", self.pln, " συγκέντροσε: ", self.pscore)
        print("Παικτης: ", self.con, " συγκέντροσε: ", self.cscore)
        if (self.pscore > self.cscore):
            print("Νικητης του παιχνιδιου: ", self.pln)
        elif (self.pscore < self.cscore):
            print("Νικητης του παιχνιδιου: ", self.con)
        else:
            print("ισοπαλια")
        print("ευχαριστουμε που παιξατε το παιχνιδι αυτο")
        highskors[self.pln] = self.pscore

        with open('score.json', 'w') as fout:
            json.dump(highskors, fout)
        exit(404)