with open('27-151a.txt') as F:
  N = int( F.readline() )
  K = int( F.readline() )
  data = [ int(x) for x in F ]

D = 100
R = 37

count = 0
for i in range(N):
  for j in range(i+1, min(i+K+1, N)):
    if abs(data[i] - data[j]) % D == 0 and \
       ((data[i] % R == 0) ^ (data[j] % R == 0)):
      print( f"({data[i]}, {data[j]})" )
      count += 1

print( count )
