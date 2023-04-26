from functools import reduce

"""
1) Имеется набор данных, состоящий из пар положительных целых чисел.
Необходимо выбрать из каждой пары ровно одно число так, чтобы сумма всех
выбранных чисел не делилась на 3 и при этом была минимально возможной.
Гарантируется, что искомую сумму получить можно. Программа должна напечатать
одно число – минимально возможную сумму, соответствующую условиям задачи.
Входные данные: Даны два входных файла: файл A (27-1a.txt) и файл B (27-1b.txt),
каждый из которых содержит в первой строке количество пар N (1 ≤ N ≤ 100000).
Каждая из следующих N строк содержит два натуральных числа,
не превышающих 10 000.
Пример входного файла:
6
1 3
5 12
6 9
5 4
3 3
1 1
Для указанных входных данных значением искомой суммы должно быть число 20. 
В ответе укажите два числа: сначала значение искомой суммы для файла А,
затем для файла B.
"""
### TODO: Ответ — 67303 200157496
##def solution1(n, data):
##    summ = [0]
##    for elem in data:
##        new_summ = []
##        while summ:
##            this = summ.pop()
##            for num in elem:
##                new_summ.append(this + num)
##        for i in range(3):
##            gen = [num for num in new_summ if num % 3 == i]
##            if gen:
##                summ.append(min(gen))
##    return min(num for num in summ if num % 3)
##
##with open('data/1/27-1t.txt') as f:
##    n = int(f.readline())
##    data = list(map(lambda x: list(map(int, x.split())), f.readlines()))
##print(solution1(n, data))
##
##with open('data/1/27-1a.txt') as f:
##    n = int(f.readline())
##    data = list(map(lambda x: list(map(int, x.split())), f.readlines()))
##print(solution1(n, data))
##
##with open('data/1/27-1b.txt') as f:
##    n = int(f.readline())
##    data = list(map(lambda x: list(map(int, x.split())), f.readlines()))
##print(solution1(n, data))


"""
2)  Имеется набор данных, состоящий из пар положительных целых чисел.
Необходимо выбрать из каждой пары ровно одно число так, чтобы сумма всех
выбранных чисел делилась на 3 и при этом была максимально возможной.
Гарантируется, что искомую сумму получить можно. Программа должна напечатать
одно число – максимально возможную сумму, соответствующую условиям задачи.
Входные данные: Даны два входных файла: файл A (27-2a.txt) и файл B (27-2b.txt),
каждый из которых содержит в первой строке количество пар N (1 ≤ N ≤ 100000).
Каждая из следующих N строк содержит два натуральных числа,
не превышающих 10 000.
Пример входного файла:
6
1 3
5 11
6 9
5 4
3 3
1 1
Для указанных входных данных значением искомой суммы должно быть число 30.
В ответе укажите два числа: сначала значение искомой суммы для файла А,
затем для файла B.
"""
### TODO: Ответ — 109737 401536407
##def solution2(n, data):
##    summ = [0]
##    for elem in data:
##        new_summ = []
##        while summ:
##            this = summ.pop()
##            for num in elem:
##                new_summ.append(this + num)
##        for i in range(3):
##            gen = [num for num in new_summ if num % 3 == i]
##            if gen:
##                summ.append(max(gen))
##    return max(num for num in summ if not num % 3)
##
##with open('data/2/27-2t.txt') as f:
##    n = int(f.readline())
##    data = list(map(lambda x: list(map(int, x.split())), f.readlines()))
##print(solution2(n, data))
##
##with open('data/2/27-2a.txt') as f:
##    n = int(f.readline())
##    data = list(map(lambda x: list(map(int, x.split())), f.readlines()))
##print(solution2(n, data))
##
##with open('data/2/27-2b.txt') as f:
##    n = int(f.readline())
##    data = list(map(lambda x: list(map(int, x.split())), f.readlines()))
##print(solution2(n, data))


"""
3)  Имеется набор данных, состоящий из пар положительных целых чисел.
Необходимо выбрать из каждой пары ровно одно число так, чтобы сумма всех
выбранных чисел делилась на 3 и при этом была минимально возможной.
Гарантируется, что искомую сумму получить можно. Программа должна напечатать
одно число – минимально возможную сумму, соответствующую условиям задачи.
Входные данные: Даны два входных файла: файл A (27-3a.txt) и файл B (27-3b.txt),
каждый из которых содержит в первой строке количество пар N (1 ≤ N ≤ 100000).
Каждая из следующих N строк содержит два натуральных числа,
не превышающих 10 000.
Пример входного файла:
6
1 3
5 11
6 9
5 4
3 3
1 1
Для указанных данных искомая сумма равна 21. 
В ответе укажите два числа: сначала значение искомой суммы для файла А,
затем для файла B.
"""
### TODO: Ответ — 66228 203412732
##def solution3(n, data):
##    summ = [0]
##    for elem in data:
##        new_summ = []
##        while summ:
##            this = summ.pop()
##            for num in elem:
##                new_summ.append(this + num)
##        for i in range(3):
##            gen = [num for num in new_summ if num % 3 == i]
##            if gen:
##                summ.append(min(gen))
##    return min(num for num in summ if not num % 3)
##
##with open('data/3/27-3t.txt') as f:
##    n = int(f.readline())
##    data = list(map(lambda x: list(map(int, x.split())), f.readlines()))
##print(solution3(n, data))
##
##with open('data/3/27-3a.txt') as f:
##    n = int(f.readline())
##    data = list(map(lambda x: list(map(int, x.split())), f.readlines()))
##print(solution3(n, data))
##
##with open('data/3/27-3b.txt') as f:
##    n = int(f.readline())
##    data = list(map(lambda x: list(map(int, x.split())), f.readlines()))
##print(solution3(n, data))


"""
4) Имеется набор данных, состоящий из пар положительных целых чисел.
Необходимо выбрать из каждой пары ровно одно число так, чтобы сумма всех
выбранных чисел делилась на 5 и при этом была максимально возможной.
Гарантируется, что искомую сумму получить можно. Программа должна напечатать
одно число – максимально возможную сумму, соответствующую условиям задачи.
Входные данные: Даны два входных файла: файл A (27-4a.txt) и файл B (27-4b.txt),
каждый из которых содержит в первой строке количество пар N (1 ≤ N ≤ 100000).
Каждая из следующих N строк содержит два натуральных числа,
не превышающих 10 000.
Пример входного файла:
6
1 3
5 11
6 9
5 4
3 3
1 1
Для указанных входных данных значением искомой суммы должно быть число 30.
В ответе укажите два числа: сначала значение искомой суммы для файла А,
затем для файла B.
"""
### TODO: Ответ — 123720 402332230
##def solution4(n, data):
##    summ = [0]
##    for elem in data:
##        new_summ = []
##        while summ:
##            this = summ.pop()
##            for num in elem:
##                new_summ.append(this + num)
##        for i in range(5):
##            gen = [num for num in new_summ if num % 5 == i]
##            if gen:
##                summ.append(max(gen))
##    return max(num for num in summ if not num % 5)
##
##with open('data/4/27-4t.txt') as f:
##    n = int(f.readline())
##    data = list(map(lambda x: list(map(int, x.split())), f.readlines()))
##print(solution4(n, data))
##
##with open('data/4/27-4a.txt') as f:
##    n = int(f.readline())
##    data = list(map(lambda x: list(map(int, x.split())), f.readlines()))
##print(solution4(n, data))
##
##with open('data/4/27-4b.txt') as f:
##    n = int(f.readline())
##    data = list(map(lambda x: list(map(int, x.split())), f.readlines()))
##print(solution4(n, data))


"""
5)  Имеется набор данных, состоящий из пар положительных целых чисел.
Необходимо выбрать из каждой пары ровно одно число так, чтобы сумма всех
выбранных чисел делилась на 5 и при этом была минимально возможной.
Гарантируется, что искомую сумму получить можно.
Программа должна напечатать одно число – минимально возможную сумму,
соответствующую условиям задачи.
Входные данные: Даны два входных файла: файл A (27-5a.txt) и файл B (27-5b.txt),
каждый из которых содержит в первой строке количество пар N (1 ≤ N ≤ 100000).
Каждая из следующих N строк содержит два натуральных числа,
не превышающих 10 000.
Пример входного файла:
6
1 3
5 11
6 9
5 4
3 3
1 1
Для указанных данных искомая сумма равна 20. 
"""
### TODO: Ответ — 75960 203343860
##def solution5(n, data):
##    summ = [0]
##    for elem in data:
##        new_summ = []
##        while summ:
##            this = summ.pop()
##            for num in elem:
##                new_summ.append(this + num)
##        for i in range(5):
##            gen = [num for num in new_summ if num % 5 == i]
##            if gen:
##                summ.append(min(gen))
##    return min(num for num in summ if not num % 5)
##
##with open('data/5/27-5t.txt') as f:
##    n = int(f.readline())
##    data = list(map(lambda x: list(map(int, x.split())), f.readlines()))
##print(solution5(n, data))
##
##with open('data/5/27-5a.txt') as f:
##    n = int(f.readline())
##    data = list(map(lambda x: list(map(int, x.split())), f.readlines()))
##print(solution5(n, data))
##
##with open('data/5/27-5b.txt') as f:
##    n = int(f.readline())
##    data = list(map(lambda x: list(map(int, x.split())), f.readlines()))
##print(solution5(n, data))


"""
6) [37] Имеется набор данных, состоящий из положительных целых чисел,
каждое из которых не превышает 1000. Требуется найти для этой
последовательности контрольное значение – наибольшее число R,
удовлетворяющее следующим условиям:
– R – произведение двух различных переданных элементов
последовательности («различные» означает, что не рассматриваются
квадраты переданных чисел, произведения различных, но равных по
величине элементов допускаются);
– R делится на 6.
Входные данные: Даны два входных файла: файл A (27-6a.txt) и
файл B (27-6b.txt), каждый из которых содержит в первой строке
количество чисел N (1 ≤ N ≤ 100000). Каждая из следующих N строк
содержит одно натуральное число, не превышающее 1000.
Пример входного файла:
6
60
17
3
7
9
60
Для указанных данных искомое контрольное значение равно 3600. 
В ответе укажите два числа: сначала контрольное значение для файла А,
затем для файла B.
"""
### TODO: Ответ — 782040 997002
##def divs_in_tuple(n):
##    r = []
##    i = 1
##    while i ** 2 <= n:
##        if i ** 2 == n:
##            r.append((i, i))
##        elif not n % i:
##            r.append((n // i, i))
##        i += 1
##    return r
##
##
##def solution6(n, data):
##    res = []
##    dels = divs_in_tuple(6)
##    for dl in dels:
##        tmp = data[:]
##        num1 = max(((i, elem) for i, elem in enumerate(tmp) if not elem % dl[0]),
##                   key=lambda x: x[1])
##        tmp.pop(num1[0])
##        num2 = max(i for i in tmp if not i % dl[1])
##        res.append(num1[1]*num2)
##    return max(res)
##
##
##with open('data/6/27.txt') as f:
##    n = int(f.readline())
##    data = list(map(int, f.readlines()))
##print(solution6(n, data))
##
##with open('data/6/27-6a.txt') as f:
##    n = int(f.readline())
##    data = list(map(int, f.readlines()))
##print(solution6(n, data))
##
##with open('data/6/27-6b.txt') as f:
##    n = int(f.readline())
##    data = list(map(int, f.readlines()))
##print(solution6(n, data))


"""
7) [51] Имеется набор данных, состоящий из положительных целых чисел, каждое из которых не превышает 1000. Требуется найти для этой последовательности контрольное значение – наибольшее число R, удовлетворяющее следующим условиям:
– R – произведение двух различных переданных элементов последовательности («различные» означает, что не рассматриваются квадраты переданных чисел, произведения различных, но равных по величине элементов допускаются);
– R делится на 7 и не делится на 49.
Если такое произведение получить невозможно, считается, что контрольное значение R = 1.
Входные данные: Даны два входных файла: файл A (27-7a.txt) и файл B (27-7b.txt), каждый из которых содержит в первой строке количество чисел N (1 ≤ N ≤ 100000). Каждая из следующих N строк содержит одно натуральное число, не превышающее 1000.
Пример входного файла:
6
60
17
3
7
9
60
Для указанных данных искомое контрольное значение равно 420. 
В ответе укажите два числа: сначала контрольное значение для файла А, затем для файла B.
"""
### TODO: Ответ — 692286 952567
##def solution7(n, data):
##    res = []
##    tmp = data[:]
##    num1 = max(((i, elem) for i, elem in enumerate(tmp) if not elem % 7 and elem % 49),
##                key=lambda x: x[1])
##    tmp.pop(num1[0])
##    num2 = max(i for i in tmp if i % 7)
##    return num1[1]*num2
##
##
##with open('data/7/27.txt') as f:
##    n = int(f.readline())
##    data = list(map(int, f.readlines()))
##print(solution7(n, data))
##
##with open('data/7/27-7a.txt') as f:
##    n = int(f.readline())
##    data = list(map(int, f.readlines()))
##print(solution7(n, data))
##
##with open('data/7/27-7b.txt') as f:
##    n = int(f.readline())
##    data = list(map(int, f.readlines()))
##print(solution7(n, data))


"""
8) [55] Имеется набор данных, состоящий из положительных целых чисел, каждое из которых не превышает 1000.
Они представляют собой результаты измерений, выполняемых прибором с интервалом 1 минута.
Требуется найти для этой последовательности контрольное значение – наименьшую сумму квадратов двух
результатов измерений, выполненных с интервалом не менее, чем в 5 минут.
Входные данные: Даны два входных файла: файл A (27-8a.txt) и файл B (27-8b.txt), каждый из которых
содержит в первой строке количество чисел N (5 ≤ N ≤ 100000). Каждая из следующих N строк содержит одно
натуральное число, не превышающее 1000.
Пример входного файла:
9
12
45
5
4
21
20
10
12
26
Для указанных данных искомое контрольное значение равно 169. 
В ответе укажите два числа: сначала контрольное значение для файла А, затем для файла B.
"""
### TODO: Ответ — 11009 200
def solution8(n, data):
    mn1 = min(((i, elem) for i, elem in enumerate(data)), key=lambda x: x[1])
    search2 = []
    if mn1[0]-5 >= 0:
        search2 += data[:mn1[0]-5]
    if mn1[0]+6 <= len(data):
        search2 += data[mn1[0]+6:]
    mn2 = min(i for i in search2)
    return mn1[1]**2 + mn2**2


with open('data/8/27-8a.txt') as f:
    n = int(f.readline())
    data = list(map(int, f.readlines()))
print(solution8(n, data))

with open('data/8/27-8b.txt') as f:
    n = int(f.readline())
    data = list(map(int, f.readlines()))
print(solution8(n, data))
