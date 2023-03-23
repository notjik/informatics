from itertools import product
from pprint import pprint

'''
Task 2
((w ∧ ¬ (x ∧ A )) ∧ ¬ ( x ≡ B )) ∧ ((w ≡ C) → (¬z ∨ (y → x)))
'''
### TODO: Ответ –
table = [(0, 0, 0, 1, 0),
         (1, 0, 1, 1, 0),
         (0, 1, 1, 0, 0),
         (1, 1, 0, 1, 1)]
for w, x, y, z, F in table:
    res = [[A, B, C, []] for A, B, C in product((('w', w), ('x', x), ('y', y), ('z', z)), repeat=3)]
    for i, elem in enumerate(res):
        A, B, C = elem[0][1], elem[1][1], elem[2][1]
        f = int(((w and not (x and A )) and not ( x == B )) and (not(w == C) or (not z or (not y or x))))
        res[i][3].append((w, x, y, z, f))
    for elem in res:
        c = 0
        for row in elem:
            if row in table:
                c += 1
        if c == len(table):
            print(elem[:3])
        print(elem)
    break
