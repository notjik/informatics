with open('27-138a.txt') as F:
   N = int( F.readline() )
   data = [ int(F.readline()) for _ in range(N) ]

D = 6
deg2, deg3 = 4, 5
M = 2**deg2 * 3**deg3
T = 18

count = 0
for i in range(N-T):
  for j in range(i+T,N):
     if (data[i]+data[j]) % D == 0 and \
        (data[i]*data[j]) % M == 0:
        count += 1

print( count )