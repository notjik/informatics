with open('27-131b.txt') as F:
   N, M, K = map( int, F.readline().split() )
   W = []
   for i in range(N):
     row = list( map(int, F.readline().split()) )
     W.append( row )

halfK = K//2

SW = [0]*N
SH = [ [0]*M for i in range(N) ]

for r in range(N):
  SW[r] = sum(W[r][:halfK+1])

for c in range(M):
  SH[0][c] = sum( W[r][c] for r in range(halfK+1) )
  for r in range(1,N):
    r1, r2 = r - halfK, r + halfK
    SH[r][c] = SH[r-1][c]
    if r1 > 0: SH[r][c] -= W[r1-1][c]
    if r2 < N: SH[r][c] += W[r2][c]

T = [ [0]*M for i in range(N) ]
T[0][0] = sum( sum(W[r][:halfK+1]) for r in range(halfK+1) )

maxTotal = 0
for r in range(N):
  r1, r2 = r - halfK, r + halfK
  if r > 0:
    T[r][0] = T[r-1][0]
    if r1 > 0: T[r][0] -= SW[r1-1]
    if r2 < N: T[r][0] += SW[r2]
  for c in range(1,M):
    T[r][c] = T[r][c-1]
    c1, c2 = c - halfK, c + halfK
    if c1 > 0: T[r][c] -= SH[r][c1-1]
    if c2 < M: T[r][c] += SH[r][c2]

print( max( max(row) for row in T ) )



