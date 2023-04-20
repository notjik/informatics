with open('27-133a.txt') as F:
   N = int( F.readline() )
   data = [ int(F.readline()) for _ in range(N) ]

D = 4
deg3 = 7
M = 3**deg3

count = 0
for i in range(N-1):
  for j in range(i+1,N):
     if (data[i]+data[j]) % D == 0 and \
        (data[i]*data[j]) % M == 0:
        count += 1

print( count )