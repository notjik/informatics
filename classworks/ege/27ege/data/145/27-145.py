# Автор: А. Кабанов

f = open('27-145b.txt')
N = int(f.readline())
K = int(f.readline())
a = [int(x) for x in f]

count = 0
k = [0,0]
k7 = [0,0]

for i in range(K,N):
    if a[i-K]%7==0:
        k7[ a[i-K]%2 ] += 1
    else:
        k[ a[i-K]%2 ] += 1

    if a[i]%7==0:
        count += k7[ a[i]%2 ] + k [ a[i]%2 ]
    else:
        count += k7[ a[i]%2 ]

print(count)
