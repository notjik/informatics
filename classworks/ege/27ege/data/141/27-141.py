with open('27-141b.txt') as F:
  N, M = map( int, F.readline().split() )
  data = [ int(s) for s in F ]

maxLen = 0
curSum = j = 0
for i in range(N):
  while j < N and curSum + data[j] <= M:
    curSum, j = curSum+data[j], j+1
  maxLen = max( j-i, maxLen )
  curSum -= data[i]

print( maxLen )