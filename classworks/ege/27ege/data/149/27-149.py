# Автор: А. Кабанов

f = open('27.txt')
N = int(f.readline())
K = int(f.readline())
a = [int(x) for x in f]

mx = float('-inf')
m47 = [float('-inf')]*2023
m = [float('-inf')]*2023

for i in range(K,N):
    if a[i-K]%47==0:
        m47[ a[i-K]%2023 ] = max(m47[ a[i-K]%2023 ], a[i-K])
    else:
        m[ a[i-K]%2023 ] = max(m[ a[i-K]%2023 ], a[i-K])

    ost = 0 if a[i]%2023==0 else 2023 - a[i]%2023
    if a[i]%47==0:
        mx = max(mx, a[i]+m[ost])
    else:
        mx = max(mx, a[i]+m47[ost])
print(mx)



