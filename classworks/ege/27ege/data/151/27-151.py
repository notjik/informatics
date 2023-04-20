# Автор: А. Кабанов

f = open('27-151a.txt')
N = int(f.readline())
K = int(f.readline())
a = [int(x) for x in f]

count = 0
k = [0]*100
k37 = [0]*100

for i in range(K+1):
    if a[i]%37==0:
        count += k[ a[i]%100 ]
        k37[ a[i]%100 ] += 1
    else:
        count += k37[ a[i]%100 ]
        k[ a[i]%100 ] += 1

for i in range(K+1,N):
    if a[i-(K+1)]%37==0:
        k37[ a[i-(K+1)]%100 ] -= 1
    else:
        k[ a[i-(K+1)]%100 ] -= 1

    if a[i]%37==0:
        count += k[ a[i]%100 ]
        k37[ a[i]%100] +=1
    else:
        count += k37[ a[i]%100 ]
        k[ a[i]%100 ] +=1
print(count)

count = 0
for i in range(N):
    for j in range(i+1,N):
        if j-i<=K and (a[i]-a[j])%100==0 and (a[i]%37==0) + (a[j]%37==0)==1:
            count+=1
print(count)
