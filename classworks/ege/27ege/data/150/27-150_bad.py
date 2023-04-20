with open('27-150a.txt') as F:
  N = int( F.readline() )
  K = int( F.readline() )
  data = [ int(x) for x in F ]

D = 17

count = 0
for i in range(N):
  for j in range(i+1, min(i+K+1, N)):
    if (data[i] + data[j]) % D == 0:
      print( f"({data[i]}, {data[j]})" )
      count += 1

print( count )
