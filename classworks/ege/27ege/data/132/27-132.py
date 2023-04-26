# Разбор: https://www.youtube.com/watch?v=ded1rxZwKyo&t=1379s

with open('27-132b.txt') as F:
   N = int( F.readline() )
   data = [ int(F.readline()) for _ in range(N) ]

D = 5
deg2 = 11
M = 2**deg2

pairs = [ [0]*(deg2+1) for _ in range(D) ]

count = 0
for i in range(N):
  r = data[i] % D
  r2 = 0 if r == 0 else D-r

  d2 = 0
  while data[i] % 2**(d2+1) == 0  and  d2 < deg2:
    d2 += 1

  count += sum( pairs[r2][deg2-d2:deg2+1] )
  pairs[r][d2] += 1

print( count )