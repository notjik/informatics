with open('27-142a.txt') as F:
  N, K, M = map( int, F.readline().split() )
  D = 20
  data = [0]*K
  for i in range(N):
     p, x = map( int, F.readline().split() )
     data[p % K] = (x-1)//D + 1

def dist( i, j ):
   return min( abs(j-i), K-abs(j-i) )

minCost = 10**10
for i in range(K):
  s = sum( dist(i,j)*data[j] for j in range(K) )
  if not data[i]:
    for j in range(i-M+1,i+M):
      if data[j%K]: break
    else:
      if s < minCost:
        minCost = s
        pos = i
        #print( i, s )

print( pos, minCost )

"""
N, K, M = 7, 20, 2
data = [0]*K
data[1] = 100
data[3] = 134
data[5] = 24
data[8] = 57
data[12] = 89
data[15] = 35
data[20%K] = 435
"""
