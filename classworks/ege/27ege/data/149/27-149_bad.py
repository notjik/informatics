with open('27-149a.txt') as F:
  N = int( F.readline() )
  K = int( F.readline() )
  data = [ int(x) for x in F ]

D = 2023
R = 47

maxSum2023 = 0
for i in range(N):
  for j in range(i+K, N):
    s = data[i] + data[j]
    if s % D == 0 and \
       ((data[i] % R == 0) ^ (data[j] % R == 0)):
      print( f"({data[i]}, {data[j]}), {s}" )
      maxSum2023 = max( s, maxSum2023 )

print( maxSum2023 )
