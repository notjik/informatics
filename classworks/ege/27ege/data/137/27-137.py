
with open('27-137b.txt') as F:
   N = int( F.readline() )
   data = [ int(F.readline()) for _ in range(N) ]

D = 8
deg3 = 6
M = 3**deg3
T = 15

pairs = [ [0]*(deg3+1) for _ in range(D) ]

def divs3( n ):
  d3 = 0
  while n % 3**(d3+1) == 0  and  d3 < deg3:
    d3 += 1
  return d3

queue = []
count = 0
for i in range(N):

  if len(queue) >= T:
    delayed = queue.pop( 0 )
    r = delayed % D
    d3 = divs3( delayed )
    pairs[r][d3] += 1

  r = data[i] % D
  r2 = 0 if r == 0 else D-r
  d3 = divs3( data[i] )

  count += sum( pairs[r2][deg3-d3:deg3+1] )

  queue.append( data[i] )

print( count )