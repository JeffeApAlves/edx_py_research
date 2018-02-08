import numpy as np
import matplotlib.pyplot as plt
import random
import time
'''
x  = np.logspace(-1,1,40)
y1 = x**2
y2 = x**1.5

plt.loglog(x,y1,"bo-",label = "First")
plt.loglog(x,y2,"gs-",label = "Second")

plt.xlabel("X")
plt.ylabel("Y")
plt.legend(loc="upper left")
plt.show()
plt.savefig("plot.pdf")

values = (random.choice(range(10)) for i in range(10))

print(values)

print(sum(values))

v = random.sample(range(10),10)

print(v)

print(sum(v))'''

t0 = time.clock()

y1 = []

for rep in range(1000000):
    y1.append( sum([random.choice(range(1,7)) for i in range(10)]))
plt.hist(y1,label = "standard", normed = True)

t1 = time.clock()


x = np.random.randint(1,7,(1000000,10))
y = np.sum(x,axis=1)
plt.hist(y,label = "numpy",normed = True)

t2 = time.clock()

print (t1-t0)
print (t2-t1)

plt.legend(loc="upper left")
plt.show()

