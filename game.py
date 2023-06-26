from computer import Computer
from human import Human
from player import words, highskors
from sak import SakClass
import json

class Game:

    def __init__(self):
        self.pxeri = []
        self.pskor = 0
        self.cxeri = []
        self.cskor = 0
        self.con = "pc"

    def setup(self):
        self.pln = input("Ονομα παικtη:")
        self.sak = SakClass()
        self.sak.randomize_sak()
        self.pxeri = self.sak.getletters()
        self.cxeri = self.sak.getletters()
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

    def run(self):
        self.pl1.hprint(self.pxeri)
        self.lex = input("Λεξη: ")
        while (self.lex != "q" or len(self.sak) < 7):
            # code for player turn
            flagp = self.pl1.hplay(self.lex, self.pxeri)
            if (flagp == True):
                psak = len(self.lex)
                self.pxeri = self.pxeri + self.sak.getletters2(self.pxeri, self.lex)
                self.pskor += self.pl1.points(self.pl1.string_brake(self.lex))
            else:
                self.sak.putbackletters(self.pxeri)
                self.pxeri = self.sak.getletters()
            flagp = False

            # code for computer turn
            flagc = self.com.cplay(self.cxeri)
            if (flagc == True):
                cl = self.com.alg(self.cxeri, words)
                self.cxeri =self.sak.getletters2(self.cxeri, cl)
                self.cskor += self.com.points(self.pl1.string_brake(cl))
            else:
                self.sak.putbackletters(self.cxeri)
                self.cxeri = self.sak.getletters()
            flagc = False
            # code for player turn and end of while
            self.pl1.hprint(self.pxeri)
            self.lex = input("Λεξη: ")

        self.end()

    def end(self):
        print("Παικτης: ", self.pln, " συγκέντροσε: ", self.pskor)
        print("Παικτης: ", self.con, " συγκέντροσε: ", self.cskor)
        if (self.pskor > self.cskor):
            print("Νικητης του παιχνιδιου: ", self.pln)
        elif (self.pskor < self.cskor):
            print("Νικητης του παιχνιδιου: ", self.con)
        else:
            print("ισοπαλια")
        print("ευχαριστουμε που παιξατε το παιχνιδι αυτο")
        highskors[self.pln] = self.pskor

        with open('scraHS.json', 'w') as fout:
            json.dump(highskors, fout)
        exit(404)