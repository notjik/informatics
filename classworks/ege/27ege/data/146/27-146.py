# Автор: А. Кабанов

f = open('27-146b.txt')
N = int(f.readline())
K = int(f.readline())
a = [int(x) for x in f]

count = 0
k41 = [0]*120
k = [0]*120

for i in range(K,N):
    if a[i-K]%41==0:
        k41[ a[i-K]%120 ] += 1
    else:
        k[ a[i-K]%120 ] += 1

    ost = 0 if a[i]%120==0 else 120 - a[i]%120
    if a[i]%41==0:
        count += k[ost]
    else:
        count += k41[ost]
print(count)