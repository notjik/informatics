from random import randint

with open("27-132bb.txt", "w") as F:
   N = 152336
   print( N, file = F )
   for i in range(N):
     print( randint(1000, 9999), file = F )
