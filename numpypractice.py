import numpy as np


c=np.random.randint(0,25,(5,5))

d=np.ravel(c)

e=np.sort(d)
print(e)

f=e.reshape(5,5)
print(f)

