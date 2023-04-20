
with open('27-136b.txt') as F:
   N = int( F.readline() )
   data = [ int(F.readline()) for _ in range(N) ]

D = 13
deg2 = 10
M = 2**deg2
T = 11

pairs = [ [0]*(deg2+1) for _ in range(D) ]

def divs2( n ):
  d2 = 0
  while n % 2**(d2+1) == 0  and  d2 < deg2:
    d2 += 1
  return d2

queue = []
count = 0
for i in range(N):

  if len(queue) >= T:
    delayed = queue.pop( 0 )
    r = delayed % D
    d2 = divs2( delayed )
    pairs[r][d2] += 1

  r = data[i] % D
  r2 = 0 if r == 0 else D-r
  d2 = divs2( data[i] )

  count += sum( pairs[r2][deg2-d2:deg2+1] )

  queue.append( data[i] )

print( count )