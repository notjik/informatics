##s = '1' * 95 + '7' * 31
##while '1111' in s:
##    s = s.replace('1111', '7', 1)
##    s = s.replace('77', '1', 1)
##print(s)



##s = '5' * 156
##while '333' in s or '555' in s:
##    if '555' in s:
##        s = s.replace('555', '3', 1)
##    else:
##        s = s.replace('333', '5', 1)
##print(s)



##s = '1' * 2018 + '3' * 2050
##while '111' in s:
##    s = s.replace('111', '2', 1)
##    s = s.replace('222', '3', 1)
##    s = s.replace('333', '1', 1)
##print(s)



##s = '5' * 500
##c = 0
##while '555' in s or '333' in s:
##    if '333' in s:
##        s = s.replace('333', '5', 1)
##        c += 3
##    else:
##        s = s.replace('555', '3', 1)
##print("{} [{}]".format(c, s))



##def f(n):
##    if n == 1:
##        return 1
##    if n > 1:
##        return 3 * f(n - 1) + g(n - 1) - n + 5
##
##
##def g(n):
##    if n == 1:
##        return 1
##    if n > 1:
##        return f(n - 1) + 3 * g(n - 1) - 3 * n
##
##
##print(f(14)+g(14))
    


##def f(s):
##    if int(s, 2) > 500000000:
##        return 0
##    if s.count('1') == 2:
##        return f(s+'0')+1
##    else:
##        return f(s+'0')+f(s+'1')
##
##
##print(f('1'))



##def f(n, m):
##    if m == 0:
##        return n
##    else:
##        return f(m, n % m)
##
##
##c = set()
##for i in range(100, 1001):
##    for j in range(100, 1001):
##        if f(i, j) == 30:
##            c.add(i)
##print(len(c))


from functools import lru_cache

@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n >= 2:
        return f(n - 1) - 2 * g(n - 1)


@lru_cache(None)
def g(n):
    if n == 1:
        return 1
    if n >= 2:
        return f(n - 1) + g(n - 1) + n


print(sum(map(int,str(g(36)))))
