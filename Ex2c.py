# Exercicio 2c

import math

def distance(x, y):

    delta_pw = (math.pow(a-b,2) for a, b in zip(x, y))
    sum_pw = sum( delta_pw )
    return math.sqrt(sum_pw)
   
print(distance((0,0),(1,1)))