"""
1. Среди целых чисел, принадлежащих числовому отрезку [351627;428763], найдите числа, которые
представляют собой произведение двух различных простых делителей. Запишите в ответе количество
таких чисел и их среднее арифметическое. Для среднего арифметического запишите только целую
часть числа.
"""
def prime_divisors(n):
    res = []
    i = 2
    while i**2 <= n:
        if not n % i:
            res.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        res.append(n)
    return res

res = []
for i in range(351627, 428763):
    pd = prime_divisors(i)
    if len(set(pd)) == len(pd) == 2:
        res.append(i)
print(len(res), int(sum(res)/len(res)))
