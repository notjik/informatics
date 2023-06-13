def to_base(n, b=2):
    alpha = '0123456789abcdefghijklmnopqrstuvwxyz'
    res = alpha[n % b]
    while n >= b:
        n //= b
        res += alpha[n % b]
    return res[::-1]


##c = 0
##for i in range(2, 11):
##    r = to_base(3456, i)
##    f = True
##    for j in r:
##        if int(j) % 2:
##            f = False
##            break
##    if f:
##        print(i)
##        c += i
##print(c)

##for x in range(5, 37):
##    if (int('12', x) * int('31', x)) == int('402', x):
##        print(x)
##        exit(0)

##for x in range(6, 37):
##    for y in range(6, 37):
##        x1 = int('225', x)
##        y2 = int('405', y)
##        if x1 == y2:
##            print(x, y)
##            exit(0)

##c = []
##for i in range(2, 11):
##    res = to_base(7667, i)
##    if res == res[::-1]:
##        print(i)
##        c.append(i)
##print(sum(c))

##c = 0
##for i in range(2, 11):
##    res = to_base(609, i)
##    if int(res[0]) % 2 != int(res[-1]) % 2:
##        c += i
##print(c)

##for i in range(2, 37):
##    res = to_base(87, i)
##    if res[-1] == '2' and len(res) <= 2:
##        print(i, res)
##        break

