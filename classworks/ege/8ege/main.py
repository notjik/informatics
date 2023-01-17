def to_base(n, b=2):
    alpha = '0123456789abcdefghijklmnopqrstuvwxyz'
    res = alpha[n % b]
    while n >= b:
        n //= b
        res += alpha[n % b]
    return res[::-1]


##print(to_base(349, 4))
##print(to_base(449, 4))
##print(int('20000',3))
##print(int('20202', 3))



##from itertools import product
##
##lt = 'КЛОУН'
##c = 0
##for s in product(lt, repeat=5):
##    if s.count('У') > 0:
##        c += 1
##print(c)



##from itertools import permutations as per
##
##lt = 'КАЛИЙ'
##c = 0
##for s in per(lt):
##    s = ''.join(s)
##    if not(s.startswith('Й')) and 'ИА' not in s:
##        c += 1
##print(c)



##from itertools import permutations as per
##
##lt = 'АБАК'
##c = 0
##for s in set(per(lt)):
##    s = ''.join(s)
##    if 'АА' not in s:
##        c += 1
##print(c)



##from itertools import product
##
##num = '01234567'
##c = 0
##for s in product(num, repeat=5):
##    if s[0] == '0':
##        continue
##    s = ''.join(s)
##    f = True
##    for i in '1357':
##        if '6' + i in s or i + '6' in s:
##            f = False
##            break
##    if f and s.count('6') == 1:
##        c += 1
##print(c)



from itertools import product

num = '012345678'
c = 0
for s in product(num, repeat=5):
    if s[0] == '0':
        continue
    
    if s[0] not in '1357' and s[-1] not in '18' and s.count('3') <= 1:
        c += 1
print(c)
