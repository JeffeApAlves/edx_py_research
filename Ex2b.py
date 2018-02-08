# Exercicio 2b

import random

random.seed(1) # This line fixes the value called by your function,
               # and is used for answer-checking.

def rand():
   return random.uniform(-1,1)

print(rand())