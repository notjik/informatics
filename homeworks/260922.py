import math
import sys
from itertools import product, permutations
from functools import lru_cache


# c = 0
# for s in product('СЛОН', repeat=5):
#     s = ''.join(s)
#     if s.count('С') == 1:
#         c += 1
# print(c)

# c = 0
# for s in product('КУСАТЬ', repeat=5):
#     s = ''.join(s)
#     if s[0] != 'Ь' and 'СУК' not in s and s.count('К') <= 1 and s.count('У') <= 1 and s.count('С') <= 1 and \
#             s.count('А') <= 1 and s.count('Т') <= 1 and s.count('Ь') <= 1:
#         c += 1
# print(c)

# c = 0
# for s in permutations('НОБЕЛИЙ'):
#     s = ''.join(s)
#     if s[0] != 'Й' and 'ИЙО' not in s:
#         c += 1
# print(c)

# s = '8' * 9 + '5' * (21 - 9)
# while '555' in s or '888' in s:
#     while '555' in s:
#         s = s.replace('555', '8', 1)
#     while '888' in s:
#         s = s.replace('888', '5', 1)
# print(s)

# s = '5' * 193
# while '333' in s or '555' in s:
#     if '555' in s:
#         s = s.replace('555', '3', 1)
#     else:
#         s = s.replace('333', '5', 1)
# print(s)

# s = '0' + '1' * 12 + '2' * 5 + '3' * 9 + '0'
# print(len(s))
# while '00' not in s:
#     s = s.replace('01', '21022', 1)
#     s = s.replace('02', '310', 1)
#     s = s.replace('03', '230112', 1)
# print(s)
# print(s.count('1'), s.count('2'), s.count('3'))

# @lru_cache(None)
# def f(n):
#     if n < 2:
#         return 1
#     if not (n % 3):
#         return f(n // 3) - 1
#     return f(n - 1) + 17
#
#
# c = 0
# for i in range(1, 100000):
#     if f(i) == 43:
#         c += 1
# print(c)

# @lru_cache(None)
# def f(n):
#     summ = 0
#     summ += 2*n+1
#     if n > 1:
#         summ += 3*n-8
#         summ += f(n-1)
#         summ += f(n-4)
#     return summ
#
#
# for i in range(10000):
#     summ = f(i)
#     if summ > 5000000:
#         print(i, summ)
#         break


# @lru_cache(None)
# def f(n):
#     if n <= 5:
#         return n
#     if not (n % 4):
#         return n + f(n // 2 + 1)
#     return n + f(n + 2)
#
#
# c = 0
# sys.setrecursionlimit(2000)
# for i in range(1, 100000):
#     try:
#         print(i, f(i))
#         c = i
#     except RecursionError:
#         print(f'error: {i}')
#         continue
# print(f'end: {c}')

# c = 0
# with open('data250922/17-243.txt') as f:
#     data250922 = list(map(int, f.readlines()))
# tmp = ()
# mx = -20000
# cst = max([i for i in data250922 if not(i % 171)])
# for i in range(len(data250922) - 1):
#     if (data250922[i] < cst or data250922[i + 1] < cst) and (data250922[i] % 2 or data250922[i + 1] % 2):
#         c += 1
#         mx = max(mx, data250922[i] + data250922[i + 1])
#         if data250922[i] + data250922[i + 1] == mx:
#             tmp = (data250922[i], data250922[i + 1])
# print(c, mx, tmp, cst)

# with open('data250922/17-1.txt') as f:
#     data250922 = list(map(int, f.readlines()))
# maximus = []
# lst = -20000
# mn = 20000
# for i in range(1, len(data250922) - 1):
#     if data250922[i] > data250922[i - 1] and data250922[i] > data250922[i + 1]:
#         maximus.append(data250922[i])
#         mn = min(mn, i - lst)
#         lst = i
# print(len(maximus), mn)

c = 0
with open('data250922/17-4.txt') as f:
    data = list(map(int, f.readlines()))
avg = sum(data) / len(data)
mn = 40000
for i in range(len(data) - 1):
    if data[i] < avg and data[i + 1] < avg and (data[i] + data[i + 1]) % 100 == 19:
        c += 1
        mn = min(mn, data[i] + data[i + 1])
print(c, mn)
