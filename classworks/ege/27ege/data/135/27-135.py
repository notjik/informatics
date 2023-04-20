from math import gcd

with open('27-135b.txt') as F:
   N = int( F.readline() )
   data = [ int(F.readline()) for _ in range(N) ]

D = 11
M = 2*3*5*7*11 # 2310

divs = [ d for d in range(1,M+1) if M % d == 0 ]

pairs = [ { d:0 for d in divs } for _ in range(D) ]

count = 0
for i in range(N):

  r = data[i] % D
  r2 = 0 if r == 0 else D-r

  for d in divs:
    if d*data[i] % M == 0:
      count += pairs[r2][d]

  d = gcd( data[i], M )
  pairs[r][d] += 1

print( count )