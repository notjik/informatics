from itertools import product, permutations
from functools import lru_cache


def toBASE(num: int, base: int) -> str:
    alpha = '0123456789abcdefghijklmnopqrstuvwxyz'
    res = alpha[num % base]
    while num >= base:
        num = num // base
        res += alpha[num % base]
    return res[::-1]


# print('x y z w f')
# for x, y, z, w in product([0, 1], repeat=4):
#     f = int(not ((not z or y) and (x or w)) or ((z == w) or (y and not x)))
#     if not f:
#         print(x, y, z, w, f)


# for i in range(2, 100):
#     n = bin(i)[2::]
#     n += n[-2]
#     n += n[1]
#     r = int(n, 2)
#     if r > 170:
#         print(i, r)
#         break


# n = 0
# s = 0
# while s <= 365:
#     s = s + 36
#     n = n + 10
# print(n)


# print((6*2**23)/(((400*400)/(100*100))*64*2**13))

# c = 0
# for i in set(permutations('МИМИКРИЯ')):
#     c += 1
# print(c)


# for o in range(1, 100):
#     for tw in range(1, 100):
#         for th in range(1, 100):
#             s = '0'+'1'*o+'2'*tw+'3'*th
#             while '01' in s or '02' in s or '03' in s:
#                 s = s.replace('01', '2302', 1)
#                 s = s.replace('02', '10', 1)
#                 s = s.replace('03', '201', 1)
#             if s.count('1') == 51 and s.count('2') == 29 and s.count('3') == 23:
#                 print(th)


# print(bin(8**1234-4**234+2**1620-108)[2::].count('1'))


# for a in range(1, 1000):
#     flag = True
#     for x in range(1, 1000):
#         if not(not(not(x % a) and (x % 36)) or (x % 12)):
#             flag = False
#     if flag:
#         print(a)
#         break


# def f(n):
#     if n == 0:
#         return 5
#     return 3 * f(n-4) if n > 0 else f(n+3)
#
#
# print(f(43))


# with open('data/17-282.txt') as f:
#     data = list(map(int, f.readlines()))
# summtrk = sum(map(int, toBASE(max([i for i in data if not(i % 11)]), 3)))
# c = 0
# mn = 20000
# for i in range(len(data) - 1):
#     if any([sum(map(int, toBASE(data[i], 3))) == summtrk, sum(map(int, toBASE(data[i+1], 3))) == summtrk]):
#         c += 1
#         mn = min(mn, data[i] + data[i+1])
# print(c, mn)


# with open('data/18-18.txt') as f:
#     data = list(map(lambda x: float(x.strip().replace(',', '.')), f.readlines()))
# flag = False
# mxsumm = data[0]
# summ = data[0]
# for i in range(1, len(data)):
#     if data[i-1] > data[i]:
#         summ += data[i]
#     else:
#         summ = data[i]
#     mxsumm = max(mxsumm, summ)
# print(mxsumm)


# @lru_cache(None)
# def game(x, y):
#     if x + y >= 78:
#         return 0
#     tmp = [game(x + 3, y), game(x, y + 3),
#            game(x * 2, y), game(x, y * 2)]
#     negative = [i for i in tmp if i <= 0]
#     if len(negative) != 0:
#         return -max(negative) + 1
#     else:
#         return -max(tmp)
#
#
# print([i for i in range(1, 71) if game(7, i) == 2])
# print([i for i in range(1, 71) if game(7, i) == -2])


# for i in range(1000):
#     x = i
#     a = 1
#     while x > 0:
#         a *= x % 7
#         x = x // 7
#     if a == 48:
#         print(i)
#         break

# @lru_cache(None)
# def f(x, y, k, n):
#     if x == y and k > n:
#         return 1
#     if x > y:
#         return 0
#     return f(x + 3, y, k, n + 1) + f(x * 2, y, k + 1, n) + f(x * 7, y, k + 1, n)
#
#
# print(f(2, 472, 0, 0))


# with open('data/24-191.txt') as f:
#     s = f.readline()
# l = 0
# res = 0
# flag = False
# for i in s:
#     if flag:
#         if i == 'A' and l >= 16:
#             res += 1
#             l = 1
#         elif i == 'A':
#             l = 1
#         elif i == 'B':
#             l = 0
#             flag = False
#         else:
#             l += 1
#     else:
#         if i == 'A':
#             l = 1
#             flag = True
# if l >= 17:
#     res += 1
#     l = 0
# print(res, l)


# def delitels(n):
#     return [x for x in range(1, n // 2 + 1) if n % x == 0] + [n]
#
#
# for i in range(190061, 190073):
#     dels = delitels(i)
#     if len([i for i in dels if i % 2]) == 4:
#         print(list(reversed([i for i in dels if i % 2][-2:])))


with open('data/26-81.txt') as f:
     n, k = map(int, f.readline().split())
     data = list(map(lambda x: list(map(int, x.split())), f.readlines()))
fly = {1: {},
        2: {}}
for i in data:
     if i[1] in fly[i[0]]:
         fly[i[0]][i[1]].append(i[2])
     else:
         fly[i[0]][i[1]] = [i[2]]
res = []
for i in fly[1]:
     if 2 not in fly[1][i] and 3 not in fly[1][i] and 4 not in fly[1][i]:
         res.append(i)
for i in fly[2]:
     if 2 not in fly[2][i] and 3 not in fly[2][i] and 4 not in fly[2][i]:
         res.append(i)
print(max(res), len(res))


##with open('data/27-54a.txt') as f:
##    n = int(f.readline())
##    data = list(map(int, f.readlines()))
##mx = 0
##for i in permutations(data, r=4):
##    summ = sum(i)
##    if not(summ % 4) and summ > mx:
##        mx = summ
##print(mx)
