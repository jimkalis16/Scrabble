from player import Player, words


class Computer(Player):

    def alg(self, xeri, words):
        for strin in words:
            string_chars =' '.join(list(strin))
            gram = Player.string_brake(self, strin)
            if Player.elenxos1(self, gram, xeri, strin) and Player.elenxos2(self, gram, xeri, strin):
                    return string_chars
        return False

    def cplay(self, xeri):
        if (self.alg(xeri, words) == False):
            print("pass")
            return False
        else:
            print("*******************************************************")
            print("*** Παίκτης: ", self.name, "   *** Σκορ: ", self.cskor)
            print(">>> Γράμματα: ", xeri)
            clex = self.alg(xeri, words)
            print("Παίζω την λέξη: ", clex)
            cgram = list(clex)
            cpoints = Player.points(self, cgram)
            print("Πόντοι λέξης: ", cpoints)
            self.cskor += cpoints
            print("*** Παίκτης: ", self.name, "   *** Σκορ: ", self.cskor)
            return True
