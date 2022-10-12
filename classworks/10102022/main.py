##s = 18 * '8' + (21-18) * '5'
##while '555' in s or '888' in s:
##    if '555' in s:
##        s = s.replace('555', '8', 1)
##    while '888' in s:
##        s = s.replace('888', '5', 1)
##    if '555' in s:
##        s = s.replace('555', '8', 1)
##print(s)

##c = 0
##s = 400 * '5'
##while '555' in s or '333' in s:
##    if '555' in s:
##        s = s.replace('555', '3', 1)
##    else:
##        s = s.replace('333', '5', 1)
##        c += 3
##print(c)

##s = '6' * 282
##while '222' in s or '6666' in s:
##    if '222' in s:
##        s = s.replace('222', '6', 1)
##    else:
##        s = s.replace('6666', '2', 1)
##print(s)

##s = '5' * 247
##while '222' in s or '555' in s:
##    if '222' in s:
##        s = s.replace('222', '5', 1)
##    else:
##        s = s.replace('555', '2', 1)
##print(s)

##s = '8' * 156
##while '222' in s or '888' in s:
##    if '222' in s:
##        s = s.replace('222', '8', 1)
##    else:
##        s = s.replace('888', '2', 1)
##print(s)

##for i in range(50, 200):
##    s = '1' * i
##    while '111' in s:
##        s = s.replace('111', '2', 1)
##        s = s.replace('222', '1', 1)
##    if s == '22':
##        print(i)

##s = '1' * 2019 + '2' * 2050
##while '222' in s:
##    s = s.replace('222', '1', 1)
##    s = s.replace('111', '2', 1)
##print(s)

##with open('data/17-5.txt') as f:
##    a = list(map(int,f.readlines()))
##mx = -10 ** 10
##c = 0
##for i in range(len(a)-1):
##    if abs(a[i]) % 10 == 7 or abs(a[i+1]) % 10 == 7:
##        c += 1
##        mx = max(mx, a[i] + a[i+1])
##print(c,mx)

##with open('data/17-1.txt') as f:
##    a = list(map(int,f.readlines()))
##avg = sum(a) / len(a)
##mx = -10 ** 10
##c = 0
##for i in range(len(a)-1):
##    if a[i] > avg or a[i+1] > avg:
##        c += 1
##        mx = max(mx, a[i] + a[i+1])
##print(c,mx)


with open('data/17-243.txt') as f:
    a = list(map(int,f.readlines()))
for i in range(len(a)):
    if a[i] % 35 == 0:
        sm = sum(map(int, list(a[i])))
mn = 10 ** 10
c = 0
for i in range(len(a)-1):
    if a[i] > sm and a[i+1] % 16 == 14 or a[i+1] > sm and a[i] % 16 == 14:
        c += 1
        mn = min(mx, a[i] + a[i+1])
print(c,mx)
