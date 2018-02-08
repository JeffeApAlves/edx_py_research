# Exercicio 1b

sentence = 'Jim quickly realized that the beautiful gowns are expensive'

#alphabet = string.ascii_letters
letters = list(set(sentence) & alphabet)

count_letters = dict.fromkeys(letters)

for l in letters:
    count_letters[l] = sentence.count(l)
