
with open('27-133b.txt') as F:
   N = int( F.readline() )
   data = [ int(F.readline()) for _ in range(N) ]

D = 4
deg3 = 7
M = 3**deg3

pairs = [ [0]*(deg3+1) for _ in range(D) ]

count = 0
for i in range(N):

  r = data[i] % D
  r2 = 0 if r == 0 else D-r

  d3 = 0
  while data[i] % 3**(d3+1) == 0  and  d3 < deg3:
    d3 += 1

  count += sum( pairs[r2][deg3-d3:deg3+1] )
  pairs[r][d3] += 1

print( count )