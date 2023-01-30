from itertools import product

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
#### TODO: Ответ – 31
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


"Task 8"
### TODO: Ответ – 1056


