# Exercicio 1c

import string

def counter(input_string):

    alphabet = set(string.ascii_letters)

    letters = list(set(input_string) & alphabet)

    count_letters = dict.fromkeys(letters)

    for l in letters:
        count_letters[l] = input_string.count(l)

    return count_letters
