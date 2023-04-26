with open("27-140b.txt") as F:
  N = int(F.readline())
  data = [ int(x) for x in F ]

K = 17
M = 7717

single = [0]*M
pairs  = [0]*M

queue = []
count = 0
for i in range(N):

  if len(queue) >= 2*K:
    delayed = queue.pop( 0 )
    r = delayed % M
    single[r] += 1

  if len(queue) >= K:
    middle = queue[K-1]
    r = middle % M
    for j in range(M):
      pairs[(j+r)%M] += single[j]

  r = data[i] % M
  r2 = 0 if r == 0 else M-r
  count += pairs[r2]

  queue.append( data[i] )

print( count )