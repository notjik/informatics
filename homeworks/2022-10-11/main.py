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
# with open('data/17-316.txt') as file:
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

# @lru_cache(None)
# def game(x):
#     if x >= 25:
#         return 0
#     tmp = []
#     if x + 1 <= 45:
#         tmp.append(game(x + 1))
#     if x * 2 <= 45:
#         tmp.append(game(x * 2))
#     negative = [i for i in tmp if i <= 0]
#     if len(negative) != 0:
#         return -max(negative) + 1
#     else:
#         return -max(tmp)
#
#
# print([i for i in range(1, 24) if game(i) == -1])
# print([i for i in range(1, 24) if game(i) == 2])
# print([i for i in range(1, 24) if game(i) == -2])

# def f(x, n):
#     if x > n:
#         return 0
#     if x == n:
#         return 1
#     return f(x + 1, n) + f(x * 2, n)
#
#
# print(f(2, 12) * f(12, 34))

# with open('data/24-200.txt') as f:
#     data = list(map(lambda x: x.strip(), f.readlines()))
# c = 0
# for i in data:
#     if i.startswith('195.2') and i.endswith('.14'):
#         print(i)
#         c += 1
# print(c)

# def nd(n):
#     return set([x for x in range(2, n // 2 + 1) if n % x == 0])
#
#
# for i in range(174457, 174506):
#     d = nd(i)
#     if len(d) == 2:
#         print(sorted(d))

# with open('data/26-j1.txt') as f:
#     n = int(f.readline())
#     data = sorted(list(map(int, f.readlines())))
# c = 0
# for i in range(n):
#     for j in range(n - 1, i, -1):
#         if data[i] + data[j] == 100:
#             c += 1
#             data[j] = 0
# print(c)

# def prime(n):
#     if n % 2 == 0:
#         return n == 2
#     d = 3
#     while d * d <= n and n % d != 0:
#         d += 2
#     return d * d > n
#
#
# # with open('data/27-82a.txt') as f:
# #     n = int(f.readline())
# #     data = list(map(int, f.readlines()))
# with open('data/27-82b.txt') as f:
#     n = int(f.readline())
#     data = list(map(int, f.readlines()))
# tmp = []
# c = 0
# mxsumm = -10*7
# for i in range(n-1):
#     th = prime(data[i])
#     ne = prime(data[i+1])
#     if c < 9:
#         if th and ne:
#             tmp.append(data[i])
#             mxsumm = max(mxsumm, sum(tmp))
#             tmp = []
#             c = 0
#         elif th:
#             c += 1
#             tmp.append(data[i])
#         else:
#             tmp.append(data[i])
#     elif ne:
#         tmp.append(data[i])
#         mxsumm = max(mxsumm, sum(tmp))
#         tmp = []
#         c = 0
#     else:
#         tmp.append(data[i])
# print(mxsumm)
