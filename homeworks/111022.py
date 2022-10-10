from itertools import product, permutations
from functools import lru_cache


def toBASE(num, base):
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b = alpha[num % base]
    while num >= base:
        num = num // base
        b += alpha[num % base]
    return b[::-1]


# print('y x z f')
# for y, x, z in product([0, 1], repeat=3):
#     f = int((not x or y) and (not y or z))
#     print(y, x, z, f)

# print(39252199708/2**20)

# for i in range(100):
#     for j in range(3):
#         n = bin(i)[2::]
#         z = n.count('0')
#         o = n.count('1')
#         if z == o:
#             n += n[-1]
#         else:
#             if z > o:
#                 n += '1'
#             else:
#                 n += '0'
#     n = int(n, 2)
#     if not(n % 4) and n % 8:
#         print(i)

# print(2**((64*2**13)/(512*256)))

# c = 0
# for s in set(permutations('МИМИКРИЯ')):
#     s = ''.join(s)
#     print(s)
#     c += 1
# print(c)

# s = '1' + '0' * 33
# while '1' in s or '100' in s:
#     if '100' in s:
#         s = s.replace('100', '0001', 1)
#     else:
#         s = s.replace('1', '00', 1)
# print(s.count('0'))

# print(toBASE(4**503 + 3*4**244 - 2*4**444 - 95, 4).count('3'))


# @lru_cache(None)
# def F(n, m):
#     if m == 0:
#         d = 0
#     else:
#         d = n + F(n, m - 1)
#     return d
#
#
# c = 0
# for n in range(1000):
#     for m in range(1000):
#         if F(n, m) == 30:
#             c += 1
# print(c)

# def f(l):
#     c1 = 0
#     c2 = 0
#     c3 = 0
#     for i in range(4):
#         if l[0][i] == l[1][i]:
#             c1 += 1
#         if l[1][i] == l[2][i]:
#             c2 += 1
#         if l[0][i] == l[2][i]:
#             c3 += 1
#     if c1 == 3 or c2 == 3 or c3 == 3:
#         return True
#     return False
#
#
# c = 0
# with open('data111022/17-316.txt') as file:
#     data = list(map(int, file.readlines()))
# mn = 30000
# mx = -20000
# for i in permutations(data, r=2):
#     mx = max(mx, sum(i))
# for i in range(len(data) - 2):
#     l = [list(str(data[i])), list(str(data[i+1])), list(str(data[i+2]))]
#     if f(l) and sum([data[i], data[i+1], data[i+2]]) < mx:
#         c += 1
#         mn = min(mn, sum([data[i], data[i+1], data[i+2]]))
# print(c, mn)


