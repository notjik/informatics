with open('27.txt') as F:
  N = int( F.readline() )
  K = int( F.readline() )
  data = [ int(x) for x in F ]

D = 7

count = 0
for i in range(N):
  for j in range(i+K, N):
    if (data[i] + data[j]) % 2 == 0 and (data[i] * data[j]) % D == 0:
      print( data[i], data[j] )
      count += 1

print(count)
