from itertools import product, permutations


def toBASE(num, base):
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b = alpha[num % base]
    while num >= base:
        num = num // base
        b += alpha[num % base]
    return b[::-1]


def sd(n):
    res = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            res.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        res.append(n)
    return set(res)


# print('x y z')
# for x, y, z in product([0, 1], repeat=3):
#     if (not x and y and z) or (not x and not y and z) or (not x and not y and not z):
#         print(x, y, z)

# c = 0
# for n in range(2, 100000):
#     n = bin(n)[2::]
#     n = n + n[-2] + n[1]
#     if 150 <= int(n, 2) <= 250:
#         c += 1
# print(c)

# for i in range(10000):
#     s = i
#     n = 1
#     while s < 28:
#         s = s + 5
#         n = n * 3
#     if n == 81:
#         print(i)

# print(54*(1/2)*3*(2/9))

# c = 0
# for s in permutations('УЛЕЙ'):
#     s = ''.join(s)
#     if not s.startswith('Й') and 'ЕУ' not in s:
#         c += 1
# print(c)

# mx = 0
# for i in range(100, 100000):
#     s = '1' * i
#     while '333' in s or '111' in s:
#         s = s.replace('333', '11', 1)
#         s = s.replace('111', '3', 1)
#     if mx < int(s):
#         mx = int(s)
#         print(i)

# print(toBASE(2*9**10 - 35 + 5, 3).count('2'))

# for a in range(1, 1000):
#     f = True
#     for x in range(1, 1000):
#         if not((x % 15 != 0 or x % 21 == 0) or (x % a != 0 or x % a != 15)):
#             f = False
#             break
#     if f:
#         print(a)
#         break

# def F(n):
#     if n > 1:
#         return 2*n + F(n-2)+F(n-3)
#     else:
#         return n + 5
#
# print(F(6))

# c = 0
# with open('data/17-7.txt') as f:
#     data = list(map(int, f.readlines()))
# summ = 0
# for i in range(len(data) - 2):
#     if data[i] % 3 == 2 or data[i + 1] % 3 == 2 or data[i + 2] % 3 == 2:
#         c += 1
#         summ += min(data[i], data[i + 1], data[i + 2])
# print(c, summ)

# for i in range(10000):
#     x = i
#     a = 0; b = 0; d = 0
#     while x > 0:
#         if d % 2 == 0:
#             a += x % 10
#         else:
#             b += x % 10
#         x = x // 10
#         d += 1
#     if a == 14 and b == 12:
#         print(i)
#         break

# def f(x):
#     res = [x]
#     for i in range(5):
#         n = len(res)
#         for j in range(n):
#             res.append(res[0] + 1)
#             res.append(res[0] * 2)
#             res.append(res[0] + (res[0] % 4))
#             res.remove(res[0])
#     return 80 in res
#
#
# print(len([x for x in range(81) if f(x)]))

# with open('data/24-4.txt') as f:
#     data = f.readline()
# alph = -1
# l = 0
# mx = 0
# tmp = 10 ** 100
# for i, elem in enumerate(data):
#     if ord(elem) > tmp:
#         l += 1
#     else:
#         if mx < l:
#             mx = l
#             alph = i - l
#         mx = max(mx, l)
#         l = 0
#     tmp = ord(elem)
# print(alph)

# c = 0
# mx = 100000
# for i in range(105673, 220785):
#     if len(sd(i)) == 3:
#         c += 1
#         mx = max(mx, i)
# print(c, mx)

# with open('data/26-4.txt') as f:
#     size, q = map(int, f.readline().split())
#     data = list(map(int, f.readlines()))
#     data.sort()
# for i in range(len(data)):
#     if size - data[i] <= 0:
#         print(i + 1, data[i - 1])
#         break
#     else:
#         size -= data[i]

with open('data/27-74b.txt') as f:
    n = int(f.readline())
    data = list(map(int, f.readlines()))
c = 0
for i in range(len(data)):
    for j in range(21):
        if not(sum(data[i:i+j]) % 39):
            c += 1
print(c)
