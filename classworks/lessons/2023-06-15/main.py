from itertools import product
from math import ceil

"""Task 1"""
### TODO: Ответ — 55


"""Task 2"""
### TODO: Ответ — xyzw
##print('x y z w f')
##for x, y, z, w in product(range(2), repeat=4):
##    F = int((not (not w or y) or (x == y)) or not z)
##    if not F:
##        print(x, y, z, w, F)


"""Task 3"""
### TODO: Ответ — 989


"""Task 4"""
### TODO: Ответ — 111


"""Task 5"""
### TODO: Ответ — 9
##for n in range(4, 1000):
##    r = bin(n)[2:]
##    r += r[-3:] if n % 3 == 0 else bin((n % 3) * 2)[2:]
##    r = int(r, 2)
##    if r < 76:
##        print(n)


"""Task 6"""
### TODO: Ответ — 40
##from turtle import *
##
##m = 25
##speed(0)
##screensize(1000,1000)
##color('red', 'green')
##left(90)
##begin_fill()
##
##right(315)
##for _ in range(7):
##    forward(12 * m)
##    right(45)
##    forward(6 * m)
##    right(135)
##
##end_fill()
##penup()
##tracer(0)
##for x in range(-50 * m, 50 * m, m):
##    for y in range(-50 * m, 50 * m, m):
##        goto(x, y)
##        dot(3, 'white')


"""Task 7"""
### TODO: Ответ — 3360
##print((120*16*56000*2)/32000)


"""Task 8"""
### TODO: Ответ — 4821
##for i, s in enumerate(product('АВОРТ', repeat=6)):
##    if ''.join(s) == 'ВОРОТА':
##        print(i + 1)


"""Task 9"""
### TODO: Ответ — 7695


"""Task 10"""
### TODO: Ответ — 69 (88 - 19)


"""Task 11"""
### TODO: Ответ — 4688
##print((ceil((213*11)/8)*16384)/(2**10))


"""Task 12"""
### TODO: Ответ — 18
##for n in range(4, 1000):
##    s = '2' + '5' * n
##    while '25' in s or '355' in s or '555' in s:
##        s = s.replace('25', '5', 1)
##        s = s.replace('355', '52', 1)
##        s = s.replace('555', '3', 1)
##    if s.count('3') == 2:
##        print(n)
##        break


"""Task 13"""
### TODO: Ответ — 33


"""Task 14"""
### TODO: Ответ — 118330623
##for x in '0123456789abcde':
##    exp = int('99658' + x + '29', 15) + int('102' + x + '023', 15)
##    if exp % 14 == 0:
##        print(x, exp // 14)
        

"""Task 15"""
### TODO: Ответ — 16
##for A in range(1000):
##    flag = True
##    for x in range(1000):
##        f = not ((x & 52 != 0) and (x & 36 == 0)) or not (x & A == 0)
##        if not f:
##            flag = False
##            break
##    if flag:
##        print(A)
##        break


"""Task 16"""
### TODO: Ответ — 4049
##def F(n):
##    if n >= 2025:
##        return n
##    return n + 3 + F(n + 3)
##
##print(F(2018) - F(2022))


"""Task 17"""
### TODO: Ответ — 13 9500
with open('data/17_8504.txt') as f:
    data = list(map(int, f.readlines()))
mn5 = min(i for i in data if i % 10 == 5 and 100 <= i < 1000)
c = 0
mxs = 0
for i in range(len(data) - 1):
    if any(100 <= data[i+j] < 1000 for j in range(2)) and sum(data[i:i+2]) % mn5 == 0:
        c += 1
        mxs = max(sum(data[i:i+2]), mxs)
print(c, mxs)
