import game
import json
import guidelines

with open('score.json', 'r', encoding="utf-8") as fin:
    # αρχικοποιει το αρχειο αποθηκευσης highscores
  highskors = json.load(fin)
  sorths = sorted(highskors.items(), key=lambda x: x[1])

print("***** Scrambble *****\n "
      "---------------------\n"
      "1: Σκορ \n"
      "2: Ρυθμισεις \n"
      "3: Παιχνιδι \n"
      "g: Τεκμηρίωση \n"
      "q: Εξοδος \n"
      "---------------------\n")

ap = input("Επιλεξτε καποια απο τις παραπανω επιλογες: ")
if (ap == '1'):
    #εκτυπονει τα αποθηκευμενα score
  pos = 1
  for i, j in reversed(sorths):
    print(pos, ". Ονομα: ", i, " Σκορ: ", j)
  pos += 1
elif (ap == '2'):

  print("Αλγοριθμοι του Η/Υ στο scrambble")
  print("1. SMART-FAIL")
  print("2. MIN-MAX-SMART")
elif (ap == '3'):
    #τρεχει την καλση GAME
  game1 = game.Game()
  game1.setup()
elif (ap == 'q'):
    # κλεινει το προγραμμα
  print("Αντιο")
  exit(202)
elif (ap == 'g'):
    # εκτυπονει τον οδηγο
    print(guidelines.guidelines())
else:
  print("Καμια επιλογη")
  exit(404)
