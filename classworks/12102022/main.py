from itertools import product

print('x y z f')
for x, y, z in product([0, 1], repeat=3):
    f = int((not x or not z) and (not y or x))
    if f:
        print(x, y, z, f)
            
