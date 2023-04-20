with open('27-136a.txt') as F:
   N = int( F.readline() )
   data = [ int(F.readline()) for _ in range(N) ]

D = 13
deg2 = 10
M = 2**deg2
T = 11

count = 0
for i in range(N-T):
  for j in range(i+T,N):
     if (data[i]+data[j]) % D == 0 and \
        (data[i]*data[j]) % M == 0:
        count += 1

print( count )