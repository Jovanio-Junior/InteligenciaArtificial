import numpy as np
v = np.array([1, 3, 5, 6])
print(v)
v2 = v.copy()

print(v2)

v[2] = 0

print(v2)
print(v)