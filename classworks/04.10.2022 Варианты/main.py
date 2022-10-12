from itertools import product, permutations
from functools import lru_cache

##c = 0
##for s in permutations('ПРИКАЗ', r=4):
##    s = ''.join(s)
##    if s.count('И') + s.count('А') <= 1:
##        print(s.count('И'), s.count('А'))
##        c += 1
##print(c)

##c = 0
##for s in permutations('УЛЕЙ'):
##    s = ''.join(s)
##    if not(s.startswith('Й')) and 'ЕУ' not in s:
##        print(s)
##        c += 1
##print(c)


##c = 0
##for s in permutations('ПАНЕЛЬ'):
##    s = ''.join(s)
##    if not(s.startswith('Ь')) and 'ЕАП' not in s:
##        print(s)
##        c += 1
##print(c)

##c = 0
##for s in set(permutations('АВТОМАТ')):
##    s = ''.join(s)
##    f = True
##    for i in range(len(s)-1):
##        if ((s[i] in 'АО') and (s[i+1] in 'АО')) or ((s[i] in 'ВТМ') and (s[i+1] in 'ВТМ')): 
##            f = False
##    if f:
##        print(s)
##        c += 1
##print(c)

##c = 0
##for s in set(product('РАДУГА', repeat=6)):
##    s = ''.join(s)
##    if s.count('Р') + s.count('Д') + s.count('Г') >= 3:
##        c += 1
##print(c)

##s = 156 * '5'
##while '333' in s or '555' in s:
##    if '555' in s:
##        s = s.replace('555', '3', 1)
##    else:
##        s = s.replace('333', '5', 1)
##print(s)

##s = '1' * 120
##while '111' in s:
##    s = s.replace('111', '2', 1)
##    s = s.replace('222', '3', 1)
##    s = s.replace('333', '1', 1)
##print(s)    

##s = 170 * '1' + 100 * '3' + 7 * '2'
##while '11' in s:
##    s = s.replace('112', '4', 1)
##    s = s.replace('113', '2', 1)
##    s = s.replace('42', '3', 1)
##    s = s.replace('43', '1', 1)
##print(s)

##s = 184 * '5'
##while '333' in s or '555' in s:
##    if '555' in s:
##        s = s.replace('555', '3', 1)
##    else:
##        s = s.replace('333', '5', 1)
##print(s)

##for a in range(1, 10000):
##    f = True
##    for x in range(1, 10000):
##        if not(not(x % a != 0 and x % 21 == 0) or x % 14 != 0):
##            f = False
##            break
##    if f:
##        print(a)

##for a in range(1, 500):
##    f = True
##    for x in range(1, 500):
##        for y in range(1, 500):
##            if not((x**2 - 10*x + 16 > 0) or (y**2 - 10*y + 21 > 0) or (x*y < 2*a)):
##                f = False
##                break
##            if not f:
##                break
##    if f:
##        print(a)
##        break

##for a in range(1, 10000):
##    f = True
##    for x in range(1, 10000):
##        if not((40 % a == 0) and (((x % a == 0) or (x % 54 != 0)) or (x % 72 != 0))):
##            f = False
##            break
##    if f:
##        print(a)

##for a in range(1, 500):
##    f = True
##    for x in range(1, 500):
##        for y in range(1, 500):
##            if not((7*y + x < a) or (2*x + 3*y > 98)):
##                f = False
##                break
##            if not f:
##                break
##    if f:
##        print(a)
##        break

##def f(n):
##    if n > 25:
##        return 2*n*n*n + 1
##    return f(n+2) + 2*f(n+3)
##
##
##c = 0
##for i in range(1, 1001):
##    if f(i) % 11 == 0:
##        c += 1
##print(c)

##c = 0
##
##
##def F( n ):
##    global c
##    c += 1
##    if n >= 1:
##        c += 1
##        F(n-1)
##        F(n//2)
##
##
##F(120)
##print(c)

##c = 0
##
##
##def F(n):
##    global c
##    if n < 3:
##        c += 1
##    else:
##        F(n-1)
##        F(n-2)
##        F(n-2)
##
##
##F(6)
##print(c)

##def f(n):
##    if n == 0:
##        return 0
##    if not(n % 2):
##        return f(n//2) + 3
##    return 2*f(n-1) + 1
##
##
##l = set()
##for i in range(1, 1001):
##    l.add(f(i))
##print(len(l))

##@lru_cache(None)
##def f(n):
##    if n == 0:
##        return 8
##    if not(n % 3):
##        return 5 + f(n // 3)
##    return f(n // 3)
##
##
##c = 0
##for i in range(1, 100000001):
##    if f(i) == 18:
##        c += 1
##print(c)

##def ch(n):
##    return not(n % 2)
##
##
##with open('data/17-3.txt') as f:
##    data = list(map(int, f.readlines()))
##c = 0
##mx = -100000
##for i in range(len(data)-3):
##    if ch(data[i]) != ch(data[i+1]) and ch(data[i+2]) != ch(data[i+3]):
##        c += 1
##        mx = max(mx, data[i] + data[i+1] + data[i+2] + data[i+3])
##print(c, mx)

##with open('data/17-1.txt') as f:
##    data = list(map(int, f.readlines()))
##avg = sum(data)/len(data)
##c = 0
##mx = -100000
##for i in range(len(data)-2):
##    if (data[i] < avg and data[i+1] < avg or data[i+1] < avg and data[i+2] < avg \
##       or data[i] < avg and data[i+2] < avg) and \
##       (not(data[i] % 19) and not(data[i+1] % 19) or not(data[i+1] % 19) and \
##        not(data[i+2] % 19) or not(data[i] % 19) and not(data[i+2] % 19)):
##        c += 1
##        mx = max(mx, data[i] + data[i+1] + data[i+2])
##print(c, mx)

with open('data/17-1.txt') as f:
    data = list(map(int, f.readlines()))
avg = sum(data)/len(data)
c = 0
mx = -100000
for i in range(len(data)-2):
    if (data[i] > avg and data[i+1] > avg or data[i+1] > avg and data[i+2] > avg \
       or data[i] > avg and data[i+2] > avg):
        c += 1
        mx = max(mx, data[i] + data[i+1] + data[i+2])
print(c, mx)
