with open('27-146a.txt') as F:
  N = int( F.readline() )
  K = int( F.readline() )
  data = [ int(x) for x in F ]

D = 120
R = 41

count = 0
for i in range(N):
  for j in range(i+K, N):
    if (data[i] + data[j]) % D == 0 and \
       ((data[i] % R == 0) ^ (data[j] % R == 0)):
      print( f"({data[i]}, {data[j]})" )
      count += 1

print(count)
