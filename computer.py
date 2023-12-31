from player import Player, words



# κατασκευαστης παικτων υπολογιστων
class Computer(Player):


    # αλγοριθμος που βρισκει την μικροτερη λεξη με τα γραμματα στο χερι (hand)
    def alg(self, hand, words):
        for strin in words:
            string_chars = ' '.join(list(strin))
            letters = Player.string_brake(self, strin)
            if Player.elenxos1(self, letters, hand) and Player.elenxos2(self, strin):
                return string_chars
        return False


    # συναρτηση που εκτελει και εκτιπωνει αποτελεσματα απο το player
    def cplay(self, hand):
        if (self.alg(hand, words) is False):
            print("pass")
            return False
        else:
            print("*******************************************************")
            print("*** Παίκτης: ", self.name, "   *** Σκορ: ", self.cscore)
            print(">>> Γράμματα: ", hand)
            cword = self.alg(hand, words)
            print("Παίζω την λέξη: ", cword)
            cletters = list(cword)
            cpoints = Player.points(self, cletters)
            print("Πόντοι λέξης: ", cpoints)
            self.cscore += cpoints
            print("*** Παίκτης: ", self.name, "   *** Σκορ: ", self.cscore)
            return True
