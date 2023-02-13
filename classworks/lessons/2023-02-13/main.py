from itertools import product
from math import ceil

def to_base(n, b):
    a = '0123456789abcdefghigklmnopqrstuvwxyz'
    r = a[n % b]
    while n >= b:
        n //= b
        r += a[n % b]
    return r[::-1]

"Task 1"
### Ответ – 25


"Task 2"
### Ответ – wxzy
##print('w x z y f')
##for w, x, z, y in product([0, 1], repeat=4):
##    f = int(not((w or not y) and x) or (y == z))
##    if not f:
##        print(w, x, z, y, f)


"Task 3"
### Ответ – 207


"Task 4"
### Ответ – 22 (01 11 10 10 0000 0001 11 0010)
##l = 'АЕИПРСЦЯ'
##s = 'ПИЦЦЕРИЯ'
##print(*sorted({i: s.count(i) for i in l}.items(),
##              key=lambda x: x[1],
##              reverse=True), sep='\n')
##print(len('01 11 10 10 0000 0001 11 0010'.replace(' ', '')))


"Task 5"
### Ответ – 29
##res = []
##for n in range(1, 10000):
##    r = bin(n)[2:]
##    if not(sum(map(int, r)) % 2):
##        r += '0'
##        r = '1' + r[2:]
##    else:
##        r += '1'
##        r = '11' + r[2:]
##    r = int(r, 2)
##    if r > 25:
##        res.append((n, r))
##print(sorted(res, key=lambda x: x[1])[0][0])
    

"Task 6"
### Ответ – 112
##from turtle import *
##
##screensize(1000,1000)
##left(90)
##m = 20
##color('black', 'red')
##begin_fill()
##speed(0)
##
##for i in range(2):
##    forward(10 * m)
##    right(90)
##    forward(20 * m)
##    right(90)
##penup()
##forward(3 * m)
##right(90)
##forward(7 * m)
##left(90)
##pendown()
##for i in range(2):
##    forward(70 * m)
##    right(90)
##    forward(90 * m)
##    right(90)
##
##end_fill()
##penup()
##for x in range(6*m, 22*m, m):
##    for y in range(-1*m, 15*m, m):
##        goto(x, y)
##        dot(3, 'green')
##mainloop()


"Task 7"
### Ответ – 128


"Task 8"
### Ответ – 1296
##c = 0
##for n in product('0123456', repeat=6):
##    if n[0] == '0':
##        continue
##    n = ''.join(n)
##    if n.count('6') == 1:
##        flag = True
##        for i in range(len(n) - 1):
##            if int(n[i]) % 2 == int(n[i + 1]) % 2:
##                flag = False
##        if flag:
##            c += 1
##print(c)


"Task 9"
### Ответ – 2321


"Task 10"
### Ответ – 15


"Task 11"
### Ответ – 3136
##print((ceil((10*39)/8)*65536)//(2**10))


"Task 12"
### Ответ – 1
##s = '8' * 120
##while '888' in s or '2222' in s:
##    if '2222' in s:
##        s = s.replace('2222', '88', 1)
##    else:
##        s = s.replace('888', '22', 1)
##print(s.count('8'))


"Task 13"
### Ответ – 28 


"Task 14"
### Ответ –
print(to_base(3*1024**75+2*256**76-16**77-2023, 32).count('0'))

