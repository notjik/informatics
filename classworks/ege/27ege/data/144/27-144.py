# Автор: А. Кабанов

with open('27-144a.txt') as F:
  N = int(f.readline())
  K = int(f.readline())
  a = [int(x) for x in f]

count = 0
k25 = [0]*25

for i in range(K,N):
    k25[ a[i-K]%25 ] += 1
    ost = 0 if a[i]%25==0 else 25-a[i]%25
    count += k25[ost]

print(count)
