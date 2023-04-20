with open('27-135a.txt') as F:
   N = int( F.readline() )
   data = [ int(F.readline()) for _ in range(N) ]

D = 11
M = 2*3*5*7*11

count = 0
for i in range(N-1):
  for j in range(i+1,N):
     if (data[i]+data[j]) % D == 0 and \
        (data[i]*data[j]) % M == 0:
        #print( data[i], data[j], data[i]+data[j], data[i]*data[j] )
        count += 1

print( count )

