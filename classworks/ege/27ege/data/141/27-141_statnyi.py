# Автор: Д. Статный

f = open('27-141b.txt')
n, m = map(int, f.readline().split())
a = [int(x) for x in f]
s = a[0]
st = end = 0
while s + a[end+1] <= m:
    s += a[end+1]
    end += 1
mx = end - st + 1
while end+1 != n:
    s -= a[st]
    st += 1
    while end+1 != n and s + a[end+1] <= m:
        s += a[end+1]
        end += 1
    mx = max(mx, end - st + 1)
print(mx)
