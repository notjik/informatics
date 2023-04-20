# Автор: Д. Статный

f = open('27-142b.txt')
n, k, m = map(int, f.readline().split())
a = [0]*k
b = set()
for i in range(n):
    km, c = map(int, f.readline().split())
    km %= k
    a[km] = (c+19)//20
    b.add(km)
#ОБЩЕЕ КОЛИЧЕСТВО МЕШКОВ, ТРЕБУЕМЫХ ДЛЯ ДОСТАВКИ
sm = sum(a)
s = 0
#ВЫЧИСЛЕНИЕ СУММЫ ДЛЯ САМОГО ПЕРВОГО ПУНКТА
for i in range(k):
    s += min(i, k-i)*a[i]
mn_s = km = float('inf')
#КОЛИЧЕСТВО МЕШКОВ ПЕРЕД НАМИ
forward = sum(a[1:k//2+1])
#КОЛИЧЕСТВО МЕШКОВ ЗА НАМИ
back = sm - forward
for i in range(1, k-m+1):
    s = s - forward + back
    if a[i]==0 and i>=m:
        if sum(a[i-m+1:i])==0:
            if sum(a[i:i+m])==0:
                if s < mn_s:
                    mn_s = s
                    km = i
    forward = forward - a[i] + a[(k//2+i)%k]
    back = sm - forward
print( km, mn_s )


