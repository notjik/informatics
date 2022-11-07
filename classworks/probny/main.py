from itertools import permutations, product
from functools import lru_cache, reduce
from math import factorial

def toBASE(num: int, base: int) -> str:
    alpha = '0123456789abcdefghijklmnopqrstuvwxyz'
    res = alpha[num % base]
    while num >= base:
        num = num // base
        res += alpha[num % base]
    return res[::-1]

##print('x y z f')
##for x, y, z in product([0, 1], repeat=3):
##    f = int((not x or z) and (not x or not y or not z))
##    if not f:
##        print(x, y, z, f)


##for n in range(1, 200):
##    b = bin(n)[2:]
##    summ = sum(map(int, b))
##    b += str(summ % 2)
##    summ = sum(map(int, b))
##    b += str(summ % 2)
##    if int(b, 2) > 108:
##        print(n, b, int(b, 2))
##        break


##for i in range(10000):
##    s = i
##    n = 11
##    while s < 224:
##        s = s + 15
##        n = n + 8
##    if n == 115:
##        print(i)


##print(2**int((5*(2**23)*4)/(512*(2**13)*4)))


##c = 0
##for n in product('0123456789abcdef', repeat=6):
##    n = ''.join(n)
##    if n[0] == '0':
##        continue
##    if not(n.startswith('1')) and n.endswith('ab'):
##        c += 1
##print(c)


##print((15*3//8)*20)


##r = 0
##for i in range(2, 10):
##    n = toBASE(572, i)
##    if '00' in n or '11' in n or '22' in n or '33' in n or '44' in n or \
##       '55' in n or '66' in n or '77' in n or '88' in n or '99' in n:
##        r += i
##print(r)


##for a in range(1, 10000):
##    f = True
##    for x in range(1, 10000):
##        check = not(40 % a) and (not(x % a and not(x % 54)) or x % 72)
##        if not check:
##            f = False
##            break
##    if f:
##        print(a)


##def f(n):
##    if n == 0:
##        return 3
##    if 0 < n <= 15:
##        return f(n-1)
##    if 15 < n < 95:
##        return 2.5 * f(n-3)
##    return 3.3 * f(n-2)
##
##
##print(f(70))


##with open('data/17-4.txt') as f:
##    data = list(map(int, f.readlines()))
##mx = 0
##mn = 10000
##c = 0
##for i in data:
##    if i % 10 in [5, 7] and i % 9 and i % 11:
##        c += 1
##        mx = max(mx, i)
##        mn = min(mn, i)
##print(c, mx+mn)


##@lru_cache(None)
##def game(x): 
##    if x >= 51: 
##        return 0
##    tmp = []
##    if (x * 3) % 2:
##        tmp.append(game(x * 3))
##    if (x + 1) % 2:
##        tmp.append(game(x + 1)) 
##    if (x + 3) % 2:
##        tmp.append(game(x + 3))
##    negative = [i for i in tmp if i <= 0] 
##    if len(negative) != 0: 
##        return -max(negative)+1 
##    else:
##        return -max(tmp)
##
##
##print([i for i in range(1, 51) if game(i) == 2])
##print([i for i in range(1, 51) if game(i) == 2])


##for i in range(1000):
##    x = i
##    L = 0
##    M = 0
##    while x > 5:
##        L = L + 1
##        if M < (x % 10):
##            M = x % 10
##        x = x // 10
##    if L == 3 and M == 7:
##        print(i)


##l = [0] * 1000
##l[2] = 1
##for i in range(1, 25):
##    l[12] = 0
##    l[i+1] += l[i]
##    l[i+4] += l[i]
##    if factorial(i+1) < 1000:
##        l[factorial(i+1)] += l[i]
##print(l[24])


##with open('data/24-s1.txt') as f:
##    data = list(map(lambda x: x.strip() ,f.readlines()))
##mx = 0
##letta = ''
##c = 0
##num = 0
##for n, i in enumerate(data):
##    if i.count('Q') >= mx:
##        mx = i.count('Q')
##        num = n
##mn = 10**6
##for a in sorted(list(set(data[num])), reverse=False):
##    if data[num].count(a) < mn:
##        letta = a
##        mn = data[num].count(a)
##print(letta, ''.join(data).count(letta))


##def delitels(n):
##    return [x for x in range(1, n // 2 + 1) if n % x == 0] + [n]
##
##for i in range(338472, 338495):
##    delit = delitels(i)
##    if len(set(delit)) == 4:
##        print(i, sorted(sorted(delit, reverse=True)[:2]))


##with open('data/27-102a.txt') as f:
##    data = list(map(int, f.readlines()))
##c = 0
##for i in range(1, len(data)):
##    for j in permutations(data, r=i):
##        if reduce(lambda x, y: x * y, j) % 524288:
##            c += 1
##print(c)

