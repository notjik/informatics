from itertools import product, permutations


def to_base(n: int, b: int) -> str:
    alpha = '0123456789abcdefghijklmnopqrstuvwxyz'
    r = alpha[n % b]
    while n >= b:
        n //= b
        r += alpha[n % b]
    return r


# print('x y z w f')
# for x, y, z, w in product([0, 1], repeat=4):
#     f = int(((not x or y) and (not y or w)) or (z == (x or y)))
#     if not f:
#         print(x, y, z, w, f)


# for n in range(1, 501):
#     b = bin(n)[2:]
#     if int(b[::-1], 2) == 11:
#         print(f'{n}: {b, b[::-1], int(b[::-1], 2)}')


# for i in range(100000):
#     S = i
#     S = S // 8
#     N = 2
#     while S <= 102:
#         S = S + 4
#         N = N * 2 - 1
#     if N == 257:
#         print(i)


# c = 0
# for s in permutations('НИЧЬЯ'):
#     s = ''.join(s)
#     if s[0] != 'Ь' and 'ЬИЯ' not in s:
#         c += 1
# print(c)


# print(to_base(36**27 + 6**18 - 19, 6).count('0'))


# def F(n):
#     if n > 2:
#         return F(n - 1) + G(n - 2)
#     else:
#         return n
#
#
# def G(n):
#     if n > 2:
#         return G(n - 1) + F(n - 2)
#     else:
#         return n + 1
#
#
# print(F(6))


# with open('data/17-4.txt') as f:
#     data = list(map(int, f.readlines()))
# avg = sum(data)/len(data)
# mn = 10**9
# c = 0
# for i in range(len(data) - 1):
#     if (data[i] > avg or data[i+1] > avg) and not((data[i] + data[i+1]) % 7):
#         c += 1
#         mn = min(mn, data[i] + data[i+1])
# print(c, mn)

# def g(x):
#     if x >= 51:
#         return 0
#     tmp = []
#     if (x * 3) % 2:
#         tmp.append(g(x * 3))
#     if (x + 1) % 2:
#         tmp.append(g(x + 1))
#     if (x + 3) % 2:
#         tmp.append(g(x + 3))
#     if not (x % 2):
#         tmp.append(g(x // 2))
#     negative = [i for i in tmp if i <= 0]
#     if len(negative) != 0:
#         return -max(negative) + 1
#     else:
#         return -max(tmp)
#
#
# print([i for i in range(1, 50) if g(i) == 2])
# print([i for i in range(1, 50) if g(i) == -2])


# for i in range(10000):
#     x = i
#     a = 0
#     b = 0
#     while x > 0:
#         if x % 2 == 0:
#             a += 1
#         else:
#             b += x % 6
#         x = x // 6
#     if a == 2 and b == 6:
#         print(i)
#         break


# def f(x: int, n: int, a: bool):
#     if x > n:
#         return 0
#     if x == n:
#         return 1
#     if not a:
#         return f(x + 1, n, True) + f(x + 2, n, False) + f(x * 2, n, False)
#     return f(x + 2, n, False) + f(x * 2, n, False)
#
#
# print(f(1, 18, False))


# with open('data/k7a-5.txt') as f:
#     s = f.readline()
# c = 0
# mxc = 0
# for i in s:
#     if i in 'CF':
#         mxc = max(mxc, c)
#         c = 0
#     c += 1
# mxc = max(mxc, c)
# print(mxc)

# def prime(n):
#     if n < 2:
#         return False
#     i = 2
#     while i**2 < n:
#         if not(n % i):
#             return False
#         i += 1
#     return True
#
# s = 0
# for i in range(3159, 31585):
#     if prime(i):
#         s += i
# print(s)


# with open('data/26-j6.txt') as f:
#     n = f.readline()
#     data = list(map(int, f.readlines()))
# size = sum(data) * 0.9
# data.sort()
# tmpdata = data[:]
# full = []
# for i in range(len(data)):
#     if sum(full) + sum(tmpdata) * 0.8 < size:
#         tmpdata.remove(data[i])
#         full.append(data[i])
#     if sum(full) + sum(tmpdata) * 0.8 < size:
#         tmpdata.reverse()
#         tmpdata.remove(data[-(i+1)])
#         tmpdata.reverse()
#         full.append(data[-(i+1)])
# print(len(full))

def check(n: int) -> bool:
    return n < 0 and abs(n) % 10 == 3


with open('data/27-93b.txt') as f:
    n, k = map(int, f.readline().split())
    data = list(map(int, f.readlines()))
tmpk = 0
mxs = -10*15
s = 0
for i in data:
    if check(i):
        tmpk += 1
    if tmpk == k:
        if s != 0:
            mxs = max(mxs, s)
            s = 0
    else:
        s += i
print(mxs)