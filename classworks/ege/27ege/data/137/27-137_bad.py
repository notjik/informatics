with open('27-137a.txt') as F:
   N = int( F.readline() )
   data = [ int(F.readline()) for _ in range(N) ]

D = 8
deg3 = 6
M = 3**deg3
T = 15

count = 0
for i in range(N-T):
  for j in range(i+T,N):
     if (data[i]+data[j]) % D == 0 and \
        (data[i]*data[j]) % M == 0:
        count += 1

print( count )