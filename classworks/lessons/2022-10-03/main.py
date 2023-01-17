from itertools import product, permutations

##print('x y z f')
##for x, y, z in product([0, 1], repeat=3):
##    f = int((not(x) or y) and (not(y) or z))
##    print(x, y, z, f)


##for i in range(10000):
##    n = bin(i)[2::]
##    for j in range(2):
##        if not(i % 2):
##            n = n + '0'
##        else:
##            n = n + '1'
##    if int(n, 2) < 171:
##        print(i)

a = permutations('0123456789ABCDEF', r=3)
c = 0
for i in a:
    i = ''.join(i)
    if i[0] == '0':
        continue
    f = True
    for s1 in '02468ACE':
        for s2 in '02468ACE':
            if s1 + s2 in i:
                f = False
    for s1 in '13579BDF':
        for s2 in '13579BDF':
            if s1 + s2 in i:
                f = False
    if f:
        c += 1
print(c)
