with open("27.txt") as F:
  N = int(F.readline())
  data = [ int(x) for x in F ]

K = 17
M = 7717

count = 0
for i in range(N-2*K):
 for j in range(i+K,N-K):
   for h in range(j+K,N):
     if (data[i] + data[j] + data[h]) % M == 0:
        count += 1

print( count )