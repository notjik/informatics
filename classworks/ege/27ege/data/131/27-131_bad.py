with open('27-131a.txt') as F:
   N, M, K = map( int, F.readline().split() )
   W = []
   for i in range(N):
     row = list( map(int, F.readline().split()) )
     W.append( row )

halfK = K//2
maxTotal = 0
for r in range(N):
  for c in range(M):
    total = 0
    for dr in range(-halfK, halfK+1):
      for dc in range(-halfK, halfK+1):
        if 0 <= r+dr < N and 0 <= c+dc < M:
           total += W[r+dr][c+dc]
    maxTotal = max( maxTotal, total )

print( maxTotal )



