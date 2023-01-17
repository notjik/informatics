from itertools import product
from functools import lru_cache

##print('x y z f')
##for x, y, z in product([0, 1], repeat=3):
##    f = int((not(x) or y or z) and (not(x) or not(y) or z) and (x or not(y) or not(z)))
##    print(x, z, y, f)

##for i in range(256):
##    s = bin(i)[2::]
##    while len(s) < 8:
##        s = '0' + s
##    s1 = ''
##    for j in s:
##        if j == '0':
##            s1 += '1'   
##        else:
##            s1 += '0'
##    ii = int(s1, 2)
##    if ii - i == 45:
##        print(i)

##for i in range(1, 1000):
##    d = i
##    n = 0
##    s = 0
##    while s <= 365:
##        s = s + d
##        n = n + 5
##    if n == 55:
##        print(i)

##c = 0
##for i in product('МЕЧТА', repeat=6):
##    i = ''.join(i)
##    if i.count('А') >= 3:
##        c += 1
##print(c)

##s = 239 * '6'
##while '2222' in s or '666' in s:
##    if '2222' in s:
##        s = s.replace('2222', '6', 1)
##    else:
##        s = s.replace('666', '2', 1)
##print(s)

@lru_cache(None)
def check(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


@lru_cache(None)
def f(n):
    if n <= 1:
        return 1
    if not(n % 3):
        return 2 * f(n - 1) + f(n - 2)
    return 3 * f(n - 2) + f(n - 1)

c = 0
for i in range(1, 36):
    if check(sum(map(int, str(f(i))))):
             c += 1
print(c)

