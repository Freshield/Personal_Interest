import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

c = np.stack([a,b])

print c

c[c == 1] = 0
print c

square = map(lambda x: x * x, a)

print square

d = np.array([2.222222222222,3.333333333333333,4.44444444444444])
print d

print np.round(d)