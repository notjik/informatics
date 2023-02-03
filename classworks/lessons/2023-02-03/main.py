from math import ceil
from copy import deepcopy

"Task 27"
### FIXME: 
with open('data/27-A.txt') as f:
    n, v, m = map(int, f.readline().split())
    data = list(map(lambda x: list(map(int, x.split())), f.readlines()))
data.sort()
prefix = [[-1, 0]] + deepcopy(data)
for i in range(1, len(prefix)):
    prefix[i][1] = prefix[i-1][1] + prefix[i][1]
print(data[:5])
print(prefix[:6])
res = []
for i in range(len(data)):
    s = prefix[i+m if i+m < len(data) else len(data)-1][1] - \
        prefix[i-m-1 if i-m-1 >= 0 else 0][1]
    res.append([data[i], s, ceil(s/v)])
print(sorted(res, key=lambda x: x[2])[0])
