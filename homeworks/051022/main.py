def toBASE(num, base):
    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b = alpha[num % base]
    while num >= base:
        num = num // base
        b += alpha[num % base]
    return b[::-1]


# summ = 0
# for i in range(2, 11):
#     if '1' in toBASE(804, i):
#         summ += i
# print(summ)

# n = (4**103) + 3 * (4**444) - 2 * (4**44) + 67
# print(toBASE(n, 4).count('3'))

# n = 36**17 + 6**48 - 17
# print(toBASE(n, 6).count('0'))

# n = 64**30 + 2**300 - 32
# print(toBASE(n, 4).count('3'))

# for x in range(4, 10):
#     n = (88 + 2 * (8 ** x)) * (8 ** x) + 88 + 88
#     print(sum(map(int, toBASE(n, 8))))

# n = 4**590 + 8**350 - 2**1020 - 25
# print(bin(n)[2::].count('0'))

# for x in range(4, 16):
#     if int('103', x) + 11 == int('103', x + 1):
#         print(x)

# n = 8**148 - 4**123 + 2**654 - 17
# print(bin(n)[2::].count('1'))

# n = 9**22 + 3**66 - 12
# print(toBASE(n, 3).count('2'))

n = (512**78 - 512**60) * (512**5 + 64**5)
print(toBASE(n, 8).count('7'))
