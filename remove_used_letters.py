
# αφερει τα γραμματα που θα του δωσεις απο μια λυστα και την επιστρεφει
class Remove_letters:
    # αφερει τα γραμματα που θα του δωσεις απο μια λυστα και την επιστρεφει
    def remove_letters(string, letter_list):
        used_letters = set(string)  # create a set of letters
        result = [letter for letter in letter_list if letter not in used_letters]
        return result