from itertools import product
from math import ceil
from functools import lru_cache
from bisect import bisect_left

def to_base(num, base):
    alpha = "0123456789abcdef"
    b = alpha[num % base]
    while num >= base:
        num = num // base
        b += alpha[num % base]
    return b[::-1]

"Task 1"
### TODO: Ответ: 16 


"Task 2"
### TODO: Ответ: zwyx
##print('z w y x f')
##for x, y, z, w in product([0, 1], repeat=4):
##    f = int((z and ((not w) or y)) and (not x))
##    if f:
##        print(z, w, y, x, f)


"Task 3"
### TODO: Ответ:  219


"Task 4"
### TODO: Ответ: 28
##print(3+3+2+2+4+4+3+2+3+2)


"Task 5"
### TODO: Ответ: 19
##for n in range(200):
##    r = bin(n)[2:]
##    if sum(map(int, r)) % 2 == 0:
##        r += '0'
##        r = '1' + r[2:]
##    else:
##        r += '1'
##        r = '11' + r[2:]
##    if int(r, 2) > 49:
##        print(n)
##        break


"Task 6"
### TODO: Ответ: 68
##from turtle import *
##
##left(90)
##m = 30
##color('black', 'red')
##begin_fill()
##speed(0)
##for i in range(2):
##    right(120)
##    forward(9 * m)
##right(300)
##for i in range(2):
##    right(120)
##    forward(9 * m)
##penup()
##for x in range(-10*m, 10*m, m):
##    for y in range(-10*m, 10*m, m):
##        goto(x, y)
##        dot(3, 'green')
##mainloop()


"Task 7"
### TODO: Ответ: 35
##print(((280*2**23)*(1/4)*1.5*(1/3))/(2**23))


"Task 8"
### TODO: Ответ: 38866
##res = []
##for i, s in enumerate(product('АЕКМНЬ', repeat=6)):
##    s = ''.join(s)
##    if s[0] != 'Ь' and s.count('М') == 2 and s.count('А') <= 1:
##        res.append((i + 1, s))
##print(res[-1])


"Task 9"
### TODO: Ответ: 3519


"Task 10"
### TODO: Ответ: 11


"Task 11"
### TODO: Ответ: 2688
##print((ceil(30*11/8)*65536)//(2**10))


"Task 12"
### TODO: Ответ: 37733
##s = 116 * '3'
##while '333' in s or '7777' in s:
##    if '333' in s:
##        s = s.replace('333', '77', 1)
##    else:
##        s = s.replace('7777', '3', 1)
##print(s)


"Task 13"
### TODO: Ответ: 30


"Task 14"
### TODO: Ответ: 2688
##print(to_base(5 * 216**1255 + 4 * 36**1256 - 4 * 6**1257 - 2023, 6).count('5'))


"Task 15"
### TODO: Ответ: 11


"Task 16"
### TODO: Ответ: 44
##@lru_cache(None)
##def F(n):
##    if n < 3:
##        return 1
##    if n % 2 == 0:
##        return F(n - 1) + n
##    return F(n - 2) + 2 * n
##
##print(F(22) - F(20))


"Task 17"
### TODO: Ответ: 1876 174903
##with open('data/17.txt') as f:
##    a = list(map(int, f.readlines()))
##mn7 = min(i for i in a if i % 7 == 0)
##c = 0
##mx = 0
##for i in range(len(a) - 1):
##    if any((a[i] % 10 == 7, a[i + 1] % 10 == 7)) and \
##       (a[i] - a[i+1])**2 > mn7**2:
##        c += 1
##        mx = max(mx, a[i] + a[i+1])
##print(c, mx)


"Task 18"
### TODO: Ответ: 2414 1045


"Task 19"
### TODO: Ответ: 22
##print((97-9)//2//2)


"Task 20"
### TODO: Ответ: 39 43
##@lru_cache(None)
##def game(x, y):
##    if x + y >= 97:
##        return 0
##    tmp = [game(x + 1, y), game(x, y + 1),
##           game(x * 2, y), game(x, y * 2)]
##    negative = [i for i in tmp if i <= 0]
##    if len(negative) != 0:
##        return -max(negative) + 1
##    return -max(tmp)
##
##print(*[i for i in range(1, 88) if game(9, i) == 2])


"Task 21"
### TODO: Ответ: 38
##@lru_cache(None)
##def game(x, y):
##    if x + y >= 97:
##        return 0
##    tmp = [game(x + 1, y), game(x, y + 1),
##           game(x * 2, y), game(x, y * 2)]
##    negative = [i for i in tmp if i <= 0]
##    if len(negative) != 0:
##        return -max(negative) + 1
##    return -max(tmp)
##
##print(min([i for i in range(1, 88) if game(9, i) == -2]))


"Task 22"
### TODO: Ответ: 24


"Task 23"
### TODO: Ответ: 56
##def f(x, n):
##    if x > n or x == 24: 
##        return 0
##    if x == n:
##        return 1
##    return f(x+1, n) + f(x*2, n)
##
##
##print(f(1, 11)*f(11, 33))


"Task 24"
### TODO: Ответ: 9
##with open('data/24.txt') as f:
##    s = f.readline()
##s1 = 'DF'
##while s1 in s:
##    s1 += 'DF'
##s1 = s1[:-2]
##if 'F' + s1 in s:
##    s1 = 'F' + s1
##if s1 + 'D' in s:
##    s1 += 'D'
##print(len(s1), s1)


"Task 25"
### TODO: Ответ:
###  112346 754
###  12234986 82114
###  13234776 88824
###  14234566 95534
###  15234356 102244
###  16234146 108954
##res = []
##l = ['']
##for i in range(2): 
##    l += [''.join(j) for j in product('0123456789', repeat=i+1)]
##for x1 in product('0123456789', repeat=1):
##    x1 = x1[0]
##    for x2 in l:
##        x = int('1' + x1 + '234' + x2 + '6')
##        if x % 149 == 0:
##            res.append(x)
##res.sort()
##[print(i, i // 149) for i in res]


