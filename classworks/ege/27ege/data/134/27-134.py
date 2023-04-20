
with open('27-134b.txt') as F:
   N = int( F.readline() )
   data = [ int(F.readline()) for _ in range(N) ]

D = 7
deg2, deg3 = 5, 4
M = 2**deg2 * 3**deg3

pairs = [ [[0]*(deg3+1) for d2 in range(deg2+1)] for _ in range(D) ]

count = 0
for i in range(N):

  r = data[i] % D
  r2 = 0 if r == 0 else D-r

  d2 = 0
  while data[i] % 2**(d2+1) == 0  and  d2 < deg2:
    d2 += 1
  d3 = 0
  while data[i] % 3**(d3+1) == 0  and  d3 < deg3:
    d3 += 1

  count += sum( sum( pairs[r2][i2][deg3-d3:deg3+1] )
                   for i2 in range(deg2-d2,deg2+1) )

  pairs[r][d2][d3] += 1

print( count )