from itertools import product

##print('x y z w')
##for x, y, z, w in product([0, 1], repeat=4):
##    if not(x and (not(y) or z) or w):
##        print(x, y, z, w)   

##n = 120
##o = bin(n)[2:]
##print(o)
##print(int('10001000', 2))

##for i in range(10000):
##    s = i
##    n = 4
##    while s < 37:
##        s = s + 3
##        n = n * 2
##    if n == 128:
##        print(i, n)
##        break

c = 0
for i in product('АИОУЭ', repeat=6):
    c += 1
    if ''.join(i) == 'ОЭЭЭЭО':
        print(i, c)
