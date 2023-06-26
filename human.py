from player import Player


class Human(Player):

    def hplay(self, word, hand):

        letters = Player.string_brake(self, word)
        elenxos1 = Player.elenxos1(self, letters, hand)
        elenxos2 = Player.elenxos2(self, word)
        elenxos = elenxos1 and elenxos2
        if (word == "pass" or word == "PASS"):
            print("πασο")
            return False
        if (elenxos is False):
            print("Δεν υπαρχει τετοια λεξη")
            return False
        if (elenxos is True):
            points = Player.points(self, letters)
            self.pscore += points
            if (self.name == "pc"):
                print("Λέξη: ", word)
            print("Πόντοι λέξης: ", points)
            print("*** Παίκτης: ", self.name, "   *** Σκορ: ", self.pscore)
            return True


    def hprint(self, hand):
        print("*******************************************************")
        print("*** Παίκτης: ", self.name, "   *** Σκορ: ", self.pscore)
        print(">>> Γράμματα: ", hand)
