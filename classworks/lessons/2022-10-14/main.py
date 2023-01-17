from itertools import product, permutations

##c = 0 #1
##for s in permutations('АПОРТ', r=5):
##    s = ''.join(s)
##    if 'АА' not in s and 'ОО' not in s and 'ОА' not in s and 'АО' not in s:
##        c += 1
##print(c)


##c = 0 #2
##for i in range(3, 10):
##    for s in product('1234567', repeat=i):
##        s = ''.join(s)
##        if '11' not in s and '22' not in s and '33' not in s and '44' not in s \
##           and '55' not in s and '66' not in s and '77' not in s \
##           and s.count('1') <= 6 and s.count('2') <= 6 and s.count('3') <= 6 \
##           and s.count('4') <= 6 and s.count('5') <= 6 and s.count('6') <= 6 \
##           and s.count('7') <= 6:
##            c += 1
##print(c)


##c = 0 #3
##for i in range(4, 7):
##    for s in product('ОНИКС', repeat=i):
##        s = ''.join(s)
##        if s.count('С') == 3 and s.count('О') == 1:
##            c += 1
##print(c)


##for i in range(40, 100): #4
##    s = '1' * i
##    while '111' in s:
##        s = s.replace('111', '2', 1)
##        s = s.replace('222', '1', 1)
##    if s == '11':
##        print(i)
##        break


##s = '5' * 150 #5
##while '5555' in s:
##    s = s.replace('5555', '33', 1)
##    s = s.replace('333', '5', 1)
##print(s)


##for i in range(80, 150):
##    s = '1' * i
##    while '111' in s:
##        s = s.replace('111', '2', 1)
##        s = s.replace('222', '1', 1)
##    if s == '21':
##        print(i)
##        break


##def f(n):
##    if n < 5:
##        return 1 + 2*n
##    if not(n % 3):
##        return 2*(n + 1)*f(n-2)
##    return 2*n + 1 + f(n-1) + 2*f(n-2)
##
##
##print(f(15))


##def f(n):
##    if n > 12:
##        return 2*n - 5
##    return  2*f(n+2) + n - 4
##
##
##print(f(1))


##def f(n):
##    if n <= 5:
##        return n
##    if not(n % 4):
##        return n + f(n // 2 - 1)
##    return n + f(n + 2)
##
##
##for i in range(1, 1000):
##    try:
##        f(i)
##        print(i)
##    except Exception:
##        pass


with open('data/17-1.txt') as f:
    data = list(map(int, f.readlines()))
avg = sum(data)/len(data)
c = 0
mx = -30000
for i in range(len(data)-2):
    if not(data[i] % 19) and not(data[i+1] % 19) or \
       not(data[i+1] % 19) and not(data[i+2] % 19) or \
       not(data[i] % 19) and not(data[i+2] % 19):
        if data[i] < avg and data[i+1] < avg or \
           data[i+1] < avg and data[i+2] < avg or \
           data[i] < avg and data[i+2] < avg:
            c += 1
            mx = max(mx, sum([data[i], data[i+1], data[i+2]]))
print(c, mx)


with open('data/17-243') as f:
    data = list(map(int, f.readlines()))
