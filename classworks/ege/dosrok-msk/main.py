from itertools import product
from math import ceil

"Task 1"
### TODO: Ответ — 45


"Task 2"
### TODO: Ответ — yxzw
##print('y x z w f')
##for x, y, z, w in product((0, 1), repeat=4):
##    f = int(not (y and not x) and not (x == z) and w)
##    if f:
##        print(y, x, z, w, f)


"Task 3"
### TODO: Ответ — 736


"Task 4"
### TODO: Ответ — 110


"Task 5"
### TODO: Ответ — 11
##for n in range(1, 1000):
##    r = bin(n)[2:]
##    if not n % 3:
##        r += r[-3:]
##    else:
##        r += bin((n % 3) * 3)[2:]
##    if int(r, 2) > 76:
##        print(n)
##        break


"Task 6"
### TODO: Ответ — 44 (6*2 + 8*4)
##from turtle import *
##
##screensize(5000, 5000)
##m = 50
##color('white', 'red')
##speed(0)
##left(90)
##begin_fill()
##
##right(45)
##for _ in range(7):
##    forward(6*m)
##    right(45)
##    forward(12*m)
##    right(135)
##
##end_fill()
##penup()
##for x in range(-1*m, 18*m, m):
##    for y in range(-1*m, 6*m, m):
##        goto(x, y)
##        dot(3, 'green')


"Task 7"
### TODO: Ответ — 43200
##print((2*16*48000*90)/3200)


"Task 8"
### TODO: Ответ — 1945
##for i, s in enumerate(product('АКЛМНЯ', repeat=5)):
##    s = ''.join(s)
##    if s.startswith('КМ'):
##        print(i + 1)
##        break


"Task 9"
### TODO: Ответ — 15058


"Task 10"
### TODO: Ответ — 42


"Task 11"
### TODO: Ответ — 294
##print(ceil((ceil((3*35)/8)*21504)/2**10))


"Task 12"
### TODO: Ответ — 26
##for n in range(3, 1000):
##    s = '3' + '5' * n
##    while '25' in s or '355' in s or '555' in s:
##        s = s.replace('25', '32', 1)
##        s = s.replace('355', '25', 1)
##        s = s.replace('555', '3', 1)
##    if sum(map(int, s)) == 17:
##        print(n)
##        break


"Task 13"
### TODO: Ответ — 16


"Task 14"
### TODO: Ответ — 116071912
for x in '0123456789abcde':
    res_exp = int('97968{}15'.format(x), 15) + int('7{}233'.format(x), 15)
    if not res_exp % 14:
        print(res_exp // 14)
        break


