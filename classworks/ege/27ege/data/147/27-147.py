# Автор: А. Кабанов

f = open('27.txt')
N = int(f.readline())
K = int(f.readline())
a = [int(x) for x in f]

mx = float('-inf')
m = [float('-inf')]*101

for i in range(K,N):
    m [ a[i-K]%101 ] = max(a[i-K], m[ a[i-K]%101 ])
    ost = 0 if a[i]%101==0 else 101 - a[i]%101
    mx = max(mx, a[i]+m[ost])
print(mx)
