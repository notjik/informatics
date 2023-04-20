# Автор: А. Кабанов

f = open('27.txt')
N = int(f.readline())
K = int(f.readline())
a = [int(x) for x in f]

mn = float('inf')
m = float('inf')
m157 = float('inf')

for i in range(K,N):
    if a[i-K]%157==0:
        m157 = min(m157,a[i-K])
    else:
        m = min(m, a[i-K])

    if a[i]%157==0:
        mn = min(mn, a[i]*m, a[i]*m157)
    else:
        mn = min(mn, a[i]*m157)
print(mn)
