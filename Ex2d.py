import random, math

random.seed(1)

def in_circle(x, origin = [0]*2):
   return distance(x,origin)<1.0
   
print(in_circle((1,1)))


# Verifica se o numero é primo

x=3
not np.any([x%i == 0 for i in range(2, x)])