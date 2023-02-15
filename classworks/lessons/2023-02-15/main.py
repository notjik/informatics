from itertools import product, permutations

def to_base(n, b):
    a = '0123456789abcdefghijklmnopqrstuvwxyz'
    r = a[n % b]
    while n >= b:
        n //= b
        r += a[n % b]
    return r[::-1]

"Task 1"
### TODO: Ответ – 83 (38+17+11+8+9)


"Task 2"
### TODO: Ответ – cab
##print('c a b f')
##for c, a, b in product([0, 1], repeat=3):
##    f = int((a == (b or c)) == b)
##    if f:
##        print(c, a, b, f)


"Task 3"
### TODO: Ответ – 88479


"Task 4"
### TODO: Ответ – 20


"Task 5"
### TODO: Ответ – 331
##for n in range(1, 10000):
##    r = to_base(n, 6)
##    r += r[-1]
##    r = bin(int(r, 6))[2:]
##    r += r[-1]
##    r = int(r, 2)
##    if r < 334:
##        print(r)


"Task 6"
### TODO: Ответ – 28 (4*6 + 4)
##from turtle import *
##
##left(90)
##m = 20
##color('black', 'red')
##begin_fill()
##speed(0)
##
##for i in range(15):
##    forward(4*m)
##    right(60)
##
##penup()
##for x in range(1*m, 10*m, m):
##    for y in range(1*m, 10*m, m):
##        goto(x, y)
##        dot(3, 'green')


"Task 7"
### TODO: Ответ – 24 (7*3+3)
##print('Кол-во целых загрузок: {}'.format(int(40/(10+2))),
##      'Осталось секунд: {}'.format(40-3*12),
##      'Передача одного файла: {}'.format((1600*1200*11)/(2**24)),
##      'Длина одного сеанса: {}'.format((1600*1200*11)/(2**24)*7),
##      'Длина последнего сеанса: {}'.format((1600*1200*11)/(2**24)*3),
##      sep='\n')


"Task 8"
### TODO: Ответ – 281
c1 = 0
for n in permutations('0123456789', r=6):
    if n[0] == '0':
        continue
    flag = True
    for i in range(len(n)-1):
        if int(n[i]) % 2 == int(n[i+1]) % 2:
            flag = False
            break
    if flag:
        c1 += 1

c2 = 0
for n in product('0123456789', repeat=4):
    if n[0] == '0':
        continue
    flag = True
    for i in range(len(n)-1):
        if n[i] == n[i+1]:
            flag = False
            break
    if flag:
        c2 += 1

print('1' if c1 > c1 else '2', abs(c2-c1), sep='')
