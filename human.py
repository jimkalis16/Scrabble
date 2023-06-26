from player import Player


class Human(Player):

    def hplay(self, lexi, xeri):

        gram = Player.string_brake(self, lexi)
        helenxos1 = Player.elenxos1(self, gram, xeri, lexi)
        helenxos2 = Player.elenxos2(self, gram, xeri, lexi)
        helenxos = helenxos1 and helenxos2
        if (lexi == "pass"):
            print("πασο")
            return False
        if (helenxos == False):
            print("Δεν υπαρχει τετοια λεξη")
            return False
        if (helenxos == True):
            ppoints = Player.points(self, gram)
            self.pskor += ppoints
            print("Λέξη: ", lexi)
            print("Πόντοι λέξης: ", ppoints)
            print("*** Παίκτης: ", self.name, "   *** Σκορ: ", self.pskor)
            return True


    def hprint(self, xeri):
        print("*******************************************************")
        print("*** Παίκτης: ", self.name, "   *** Σκορ: ", self.pskor)
        print(">>> Γράμματα: ", xeri)

