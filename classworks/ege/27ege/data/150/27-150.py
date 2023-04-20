# Автор: А. Кабанов

f = open('27.txt')
N = int(f.readline())
K = int(f.readline())
a = [int(x) for x in f]

count = 0
k17 = [0]*17

for i in range(K+1):
    ost = 0 if a[i]%17==0 else 17 - a[i]%17
    count += k17[ost]

    k17[a[i]%17] += 1

for i in range(K+1,N):
    k17[ a[i-(K+1)]%17 ] -= 1
    ost = 0 if a[i]%17==0 else 17 - a[i]%17
    count += k17[ost]

    k17[a[i]%17]+=1
print(count)
