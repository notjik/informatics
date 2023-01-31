from itertools import product
from math import ceil
from functools import lru_cache

"Task 1"
### TODO: Ответ – 66 (13 + 53)


"Task 2"
### TODO: Ответ – wyxz
##print('w y x z f')
##for x, y, z, w in product([0, 1], repeat=4):
##    f = int(not w or (not (not x or z) or y))
##    if not f:
##        print(w, y, x, z, f)


"Task 3"
### TODO: Ответ – 55226


"Task 4"
### TODO: Ответ – 31
##s = 'ИНВАРИАНТ'
##[print('{}: {}'.format(i, s.count(i))) for i in set(s)]
##print(len('1011100010011010010111010100011'))


"Task 5"
### TODO: Ответ – 30
##mx = 0
##for n in range(16):
##    r = bin(n)[2:]
##    if not(sum(map(int, r)) % 2):
##        r += '1'
##        r = '10' + r[2:]
##    else:
##        r += '0'
##        r = '11' + r[2:]
##    mx = max(mx, int(r, 2))
##print(mx)


"Task 6"
### TODO: Ответ – 70
##from turtle import *
##
##left(90)
##color('black', 'red')
##m = 20
##
##for i in range(2):
##    forward(9 * m)
##    right(90)
##    forward(15 * m)
##    right(90)
##penup()
##forward(12 * m)
##right(90)
##pendown()
##for i in range(2):
##    forward(6 * m)
##    right(90)
##    forward(12 * m)
##    right(90)
##
##penup()
##for x in range(0*m, 10*m, m):
##    for y in range(0*m, 10*m, m):
##        goto(x, y)
##        dot(3, 'green')


"Task 7"
### TODO: Ответ – 10
##print((10*2**23*(10/7))/(44*1000*2*135))


"Task 8"
### TODO: Ответ – 768
##c = 0
##for s in product('АРБУЗ', repeat=6):
##    s = ''.join(s)
##    if s.count('А') == 3 and 'АА' in s and 'ААА' not in s:
##        c += 1
##print(c)


"Task 9"
### TODO: Ответ – 1056


"Task 10"
### TODO: Ответ – 18


"Task 11"
### TODO: Ответ – 65920
##print(ceil(14*294/8)*131072/2**10)



"Task 12"
### TODO: Ответ – 14
##c = 0
##for n in range(1, 100):
##    s = '1' + '0' * n
##    while '10' in s or '1' in s:
##        if '10' in s:
##            s = s.replace('10', '0001', 1)
##        else:
##            if '1' in s:
##                s = s.replace('1', '0', 1)
##    if not(len(s) % 7):
##        c += 1
##print(c)


"Task 13"
### TODO: Ответ – 15 (2+2+2+3+2+4)


"Task 14"
### TODO: Ответ – 199
##for n in range(2, 1000):
##    if n**2+n == 39800:
##        print(n)
##        break


"Task 15"
### TODO: Ответ – 6
##c = 0
##for a in range(1, 10000):
##    flag = True
##    for x in range(1, 10000):
##        f = not(160 <= x <= 180) or (x % 35 or not(x % a))
##        if not f:
##            flag = False
##            break
##    if flag:
##        c += 1
##print(c)

"Task 16"
### TODO: Ответ – 21
##@lru_cache(None)
##def F(n):
##    if n >= 10000:
##        return n
##    return F(n+2) - 3 if not(n % 2) else F(n+2) + 1
##
##
##for i in range(10000, 1, -1):
##    F(i)
##
##print(F(94)-F(80))


"Task 17"
### TODO: Ответ – 3 74280
##with open('data/17.txt') as f:
##    data = list(map(int, f.readlines()))
##mnk8 = min([i for i in data if not(i % 8) and i != 8])
##c = 0
##mn = [10**10]
##for i in range(len(data) - 1):
##    if not(data[i] % mnk8) and not(data[i+1] % mnk8):
##        c += 1
##        if sum(mn) > sum(data[i:i+2]):
##            mn = data[i:i+2]
##print(c, max(mn))


"Task 18"
### TODO: Ответ – 2483 1157



