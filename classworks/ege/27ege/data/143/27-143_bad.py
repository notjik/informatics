with open('27-143a.txt') as F:
  N, K = map( int, F.readline().split() )
  data = [ int(F.readline()) for _ in range(N) ]

maxSum = 0
for i in range(N-K):
  s1 = sum( data[i:i+K] )
  for j in range(i+K,N-K):
    s2 = sum( data[j:j+K] )
    if (s1 + s2) % 68 == 0:
      maxSum = max( maxSum, s1+s2 )

print( maxSum)
