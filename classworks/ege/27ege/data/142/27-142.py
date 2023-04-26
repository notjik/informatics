with open('27-142a.txt') as F:
  N, K, M = map( int, F.readline().split() )
  D = 20
  data = [0]*K
  for i in range(N):
     p, x = map( int, F.readline().split() )
     data[p % K] = (x-1)//D + 1

data *= 2
p = [0]*(2*K+1)
for i in range(1,2*K+1):
  p[i] = p[i-1] + data[i-1]

s = sum( data[i]*min(i, K-i) for i in range(K) )

nextPoint = prevPoint = 0
while data[nextPoint] == 0: nextPoint += 1
while data[prevPoint] == 0: prevPoint -= 1

minCost = s if not data[0] and prevPoint <= M and nextPoint >= M \
            else float('inf')
pos = 0
for i in range(1,K):
  s -= p[i+K//2] - p[i]
  s += p[i+K] - p[i+K//2]
  if data[i]:
    prevPoint = i
    if nextPoint <= prevPoint:
       nextPoint = i + 1
       while nextPoint < K and data[nextPoint] == 0:
         nextPoint += 1
  else:
    # print( i, s, prevPoint, nextPoint )
    if i - prevPoint >= M and nextPoint - i >= M:
      if s < minCost:
        minCost = s
        pos = i

print( pos, minCost )

