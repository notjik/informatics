from math import gcd

with open('27-139b.txt') as F:
   N = int( F.readline() )
   data = [ int(F.readline()) for _ in range(N) ]

D = 4
M = 9009 # 3*3*7*11*13
T = 25

divs = [ d for d in range(1,M+1) if M % d == 0 ]

pairs = [ { d:0 for d in divs } for _ in range(D) ]

queue = []
count = 0
for i in range(N):

  if len(queue) >= T:
    delayed = queue.pop( 0 )
    r = delayed % D
    d = gcd( delayed, M )
    pairs[r][d] += 1

  r = data[i] % D
  r2 = 0 if r == 0 else D-r

  for d in divs:
    if d*data[i] % M == 0:
      count += pairs[r2][d]

  queue.append( data[i] )

print( count )