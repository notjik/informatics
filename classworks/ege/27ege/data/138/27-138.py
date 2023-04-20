
with open('27-138b.txt') as F:
   N = int( F.readline() )
   data = [ int(F.readline()) for _ in range(N) ]

D = 6
deg2, deg3 = 4, 5
M = 2**deg2 * 3**deg3
T = 18

pairs = [ [[0]*(deg3+1) for d2 in range(deg2+1)] for _ in range(D) ]

def divsX( n, x, maxDeg ):
  dx = 0
  while n % x**(dx+1) == 0  and  dx < maxDeg:
    dx += 1
  return dx

queue = []
count = 0
for i in range(N):

  if len(queue) >= T:
    delayed = queue.pop( 0 )
    r = delayed % D
    d2 = divsX( delayed, 2, deg2 )
    d3 = divsX( delayed, 3, deg3 )
    pairs[r][d2][d3] += 1

  r = data[i] % D
  r2 = 0 if r == 0 else D-r
  d2 = divsX( data[i], 2, deg2 )
  d3 = divsX( data[i], 3, deg3 )

  count += sum( sum( pairs[r2][i2][deg3-d3:deg3+1] )
                   for i2 in range(deg2-d2,deg2+1) )

  queue.append( data[i] )

print( count )