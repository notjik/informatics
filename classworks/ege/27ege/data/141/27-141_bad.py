with open('27-141a.txt') as F:
  N, M = map( int, F.readline().split() )
  data = [ int(s) for s in F ]

#N, M = 7, 10
#data = [1, 3, 5, 3, 6, 5, 8]

maxLen = 0
for i in range(N):
  curSum = 0
  j = i
  while j < N and curSum + data[j] <= M:
    curSum, j = curSum+data[j], j+1
  maxLen = max( j-i, maxLen )

print( maxLen )