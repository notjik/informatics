with open('27-148a.txt') as F:
  N = int( F.readline() )
  K = int( F.readline() )
  data = [ int(x) for x in F ]

D = 157

minProd157 = float('inf')
for i in range(N):
  for j in range(i+K, N):
    s = data[i] * data[j]
    if s % D == 0:
      print( f"({data[i]}, {data[j]}), {s}" )
      minProd157 = min( s, minProd157 )

print( minProd157 )
