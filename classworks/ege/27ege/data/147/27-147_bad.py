with open('27-147a.txt') as F:
  N = int( F.readline() )
  K = int( F.readline() )
  data = [ int(x) for x in F ]

D = 101

maxSum101 = 0
for i in range(N):
  for j in range(i+K, N):
    s = data[i] + data[j]
    if s % D == 0:
      print( f"({data[i]}, {data[j]}), {s}" )
      maxSum101 = max( s, maxSum101 )

print( maxSum101 )
