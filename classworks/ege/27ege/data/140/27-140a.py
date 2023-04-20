with open("27-140b.txt") as F:
  N = int(F.readline())
  data = [ int(x) for x in F ]

K = 17
M = 7717

single = [0]*M
pairs  = [0]*M

count = 0
for i in range(N):

  if i >= 2*K:
    r = data[i-2*K] % M
    single[r] += 1

  if i >= K:
    r = data[i-K] % M
    for j in range(M):
      pairs[(j+r)%M] += single[j]

  r = data[i] % M
  r2 = 0 if r == 0 else M-r
  count += pairs[r2]

print( count )