class Remove_letters:
    def remove_letters(string, letter_list):
        used_letters = set(string)  # create a set of letters
        result = [letter for letter in letter_list if letter not in used_letters]
        return result