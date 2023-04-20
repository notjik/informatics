with open('27-139a.txt') as F:
   N = int( F.readline() )
   data = [ int(F.readline()) for _ in range(N) ]

D = 4
M = 3*3*7*11*13
T = 25

count = 0
for i in range(N-T):
  for j in range(i+T,N):
     if (data[i]+data[j]) % D == 0 and \
        (data[i]*data[j]) % M == 0:
        #print( data[i], data[j], data[i]+data[j], data[i]*data[j] )
        count += 1

print( count )

