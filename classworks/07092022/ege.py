from statistics import mean

file = open('17data/17-4.txt')
p = list(map(int, file.readlines()))
mn = 10**10
mx = -10**11
c = 0
summ = mean(p)
for i in range(len(p)-2):
	if p[i] > summ and p[i+1] > summ or p[i+1] > summ and p[i+2] > summ or p[i] > summ and p[i+2] > summ:
		c += 1
		mx = max(mx, p[i+1]+p[i]+p[i+2])
print(c, mx)