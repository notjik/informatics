# PRO100 ЕГЭ
# https://youtu.be/B_r7kOK3PJo?t=18804

with open('27-143b.txt') as F:
  N, K = map( int, F.readline().split() )
  data = [ int(F.readline()) for _ in range(N) ]

p = [0]*(N+1)
for i in range(1,N+1):
  p[i] = p[i-1] + data[i-1]

inf = 10**20
sumK = [-inf]*(N+1) # суммы чисел по отрезкам длиной K
for i in range(K,N+1):  # начиная с K
  sumK[i] = p[i] - p[i-K]

D = 68
maxPrev = [None]*D
maxSum = -float('inf')
for i in range(K,N+1):
  r = sumK[i] % D
  rAdd = (D - r) % D
  if maxPrev[rAdd] is not None:
     maxSum = max( maxSum, sumK[i]+maxPrev[rAdd] )
  rNext = sumK[i+1-K] % D
  if maxPrev[rNext] is None or sumK[i+1-K] > maxPrev[rNext]:
    maxPrev[rNext] = sumK[i+1-K]

print( maxSum)
