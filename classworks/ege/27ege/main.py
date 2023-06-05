from functools import reduce
from itertools import combinations
from math import factorial

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
##def solution8(n, data):
##    mn1 = min(((i, elem) for i, elem in enumerate(data)), key=lambda x: x[1])
##    search2 = []
##    if mn1[0]-5 >= 0:
##        search2 += data[:mn1[0]-5]
##    if mn1[0]+6 <= len(data):
##        search2 += data[mn1[0]+6:]
##    mn2 = min(i for i in search2)
##    return mn1[1]**2 + mn2**2
##
##
##with open('data/8/27-8a.txt') as f:
##    n = int(f.readline())
##    data = list(map(int, f.readlines()))
##print(solution8(n, data))
##
##with open('data/8/27-8b.txt') as f:
##    n = int(f.readline())
##    data = list(map(int, f.readlines()))
##print(solution8(n, data))


"""
9) [60] На спутнике «Восход» установлен прибор, предназначенный для измерения
солнечной активности. Каждую минуту прибор передаёт по каналу связи
неотрицательное целое число – количество энергии солнечного излучения,
полученной за последнюю минуту, измеренное в условных единицах. Временем,
в течение которого происходит передача, можно пренебречь. Необходимо найти
в заданной серии показаний прибора минимальное нечётное произведение двух
показаний, между моментами передачи которых прошло не менее 6 минут.
Если получить такое произведение не удаётся, ответ считается равным –1.
Входные данные: Даны два входных файла: файл A (27-9a.txt) и
файл B (27-9b.txt), каждый из которых содержит в первой строке количество
чисел N (7 ≤ N ≤ 100000). Каждая из следующих N строк содержит одно
натуральное число, не превышающее 1000.
Пример входного файла:
11
12
45
17
23
21
20
19
12
26
Для указанных данных искомое контрольное значение равно 95. 
В ответе укажите два числа: сначала контрольное значение для файла А,
затем для файла B.
"""
### TODO: Ответ — 2465 121
##def solution9(n, data):
##    mins_odd = sorted(((i, data[i]) for i in range(len(data)) if data[i] & 1), key=lambda x: (x[1], x[0]))
##    mn = 10 ** 10
##    for i, odd1 in enumerate(mins_odd):
##        for odd2 in mins_odd[i + 1:]:
##            if abs(odd2[0] - odd1[0]) >= 6:
##                mn = min(mn, odd1[1] * odd2[1])
##                break
##        if odd1[1] >= mn:
##            break
##    return mn
##
##
##with open('data/9/27.txt') as f:
##    n = int(f.readline())
##    data = list(map(int, f.readlines()))
##print(solution9(n, data))
##
##with open('data/9/27-9a.txt') as f:
##    n = int(f.readline())
##    data = list(map(int, f.readlines()))
##print(solution9(n, data))
##
##with open('data/9/27-9b.txt') as f:
##    n = int(f.readline())
##    data = list(map(int, f.readlines()))
##print(solution9(n, data))


"""
10) [73] (Д.Ф. Муфаззалов) Имеется набор данных, состоящий из троек
положительных целых чисел. Необходимо выбрать из каждой тройки ровно
одно число так, чтобы сумма всех выбранных чисел не делилась на 4 и
при этом была максимально возможной. Гарантируется, что искомую сумму
получить можно. Программа должна напечатать одно число – максимально
возможную сумму, соответствующую условиям задачи.
Входные данные: Даны два входных файла: файл A (27-10a.txt) и
файл B (27-10b.txt), каждый из которых содержит в первой строке
количество троек N (1 ≤ N ≤ 100000). Каждая из следующих N строк содержит
три натуральных числа, не превышающих 10 000.
Пример входного файла:
6
1 3 2
5 12 12
6 8 12
5 4 12
3 3 12
1 1 13
Для указанных входных данных значением искомой суммы должно быть число 63. 
В ответе укажите два числа: сначала значение искомой суммы для файла А,
затем для файла B.
"""
### TODO: Ответ — 15062 45226419
##def solution10(n, data):
##    data = sorted((sorted(i, reverse=True) for i in data), key=lambda x: ((x[0] - x[1])))
##    summ = sum(i[0] for i in data)
##    i = 0
##    j = 1
##    while not summ % 4:
##        if (summ - data[i][0] + data[i][1]) % 4:
##            summ -= data[i][0] - data[i][1]
##        i += 1
##    return summ
##
##
##with open('data/10/27.txt') as f:
##    n = int(f.readline())
##    data = list(map(lambda x: list(map(int, x.split())), f.readlines()))
##print(solution10(n, data))
##
##
##with open('data/10/27-10a.txt') as f:
##    n = int(f.readline())
##    data = list(map(lambda x: list(map(int, x.split())), f.readlines()))
##print(solution10(n, data))
##
##
##with open('data/10/27-10b.txt') as f:
##    n = int(f.readline())
##    data = list(map(lambda x: list(map(int, x.split())), f.readlines()))
##print(solution10(n, data))


"""
11) Имеется набор данных, состоящий из троек положительных целых чисел.
Необходимо выбрать из каждой тройки ровно одно число так, чтобы сумма всех
выбранных чисел делилась на 8 и при этом была максимально возможной.
Гарантируется, что искомую сумму получить можно. Программа должна
напечатать одно число – максимально возможную сумму, соответствующую
условиям задачи.
Входные данные: Даны два входных файла: файл A (27-11a.txt) и
файл B (27-11b.txt), каждый из которых содержит в первой строке количество
троек N (1 ≤ N ≤ 100000). Каждая из следующих N строк содержит три натуральных
числа, не превышающих 10 000.
Пример входного файла:
6
8 3 4
4 8 12
9 5 6
2 8 3
12 3 5
1 4 12
Для указанных входных данных значением искомой суммы должно быть число 56. 
В ответе укажите два числа: сначала значение искомой суммы для файла А,
затем для файла B.
"""
### TODO: Ответ — 14432 45978688
##def solution11(n, data):
##    data = sorted((sorted(i, reverse=True) for i in data), key=lambda x: ((x[0] - x[1])))
##    summ = sum(i[0] for i in data)
##    i = 0
##    j = 1
##    while summ % 8:
##        if not (summ - data[i][0] + data[i][1]) % 8:
##            summ -= data[i][0] - data[i][1]
##        i += 1
##    return summ
##
##
##with open('data/11/27.txt') as f:
##    n = int(f.readline())
##    data = list(map(lambda x: list(map(int, x.split())), f.readlines()))
##print(solution11(n, data))
##
##
##with open('data/11/27-11a.txt') as f:
##    n = int(f.readline())
##    data = list(map(lambda x: list(map(int, x.split())), f.readlines()))
##print(solution11(n, data))
##
##
##with open('data/11/27-11b.txt') as f:
##    n = int(f.readline())
##    data = list(map(lambda x: list(map(int, x.split())), f.readlines()))
##print(solution11(n, data))


"""
12) [75] (Д.В. Богданов) Имеется набор данных, состоящий из положительных
целых чисел. Необходимо определить количество пар элементов (ai, aj) этого
набора, в которых 1 ≤ i < j ≤ N и произведение элементов кратно 6. 
Входные данные: Даны два входных файла: файл A (27-12a.txt) и
файл B (27-12b.txt), каждый из которых содержит в первой строке количество
чисел N (1 ≤ N ≤ 100000). Каждая из следующих N строк содержит натуральное
число, не превышающее 1000.
Пример входного файла:
4
7
5
6
12
Для указанных входных данных количество подходящих пар должно быть равно 5.
В приведённом наборе из 4 чисел имеются пять пар (7, 6), (5, 6), (7, 12),
(5, 12), (6, 12), произведение элементов которых кратно 6. 
В ответе укажите два числа: сначала количество подходящих пар для файла А,
затем для файла B.
"""
### TODO: Ответ — 47 745460178
##def solution12(n, data):
##    res = 0
##    c2 = 0
##    c3 = 0
##    c6 = 0
##    for i, elem in enumerate(data):
##        if not elem % 6:
##            res += i
##            c6 += 1
##        elif not elem % 2:
##            res += c3 + c6
##            c2 += 1
##        elif not elem % 3:
##            res += c2 + c6
##            c3 += 1
##        else:
##            res += c6
##    return res
##
##
##with open('data/12/27.txt') as f:
##    n = int(f.readline())
##    data = list(map(int, f.readlines()))
##print(solution12(n, data))
##
##
##with open('data/12/27-12a.txt') as f:
##    n = int(f.readline())
##    data = list(map(int, f.readlines()))
##print(solution12(n, data))
##
##
##with open('data/12/27-12b.txt') as f:
##    n = int(f.readline())
##    data = list(map(int, f.readlines()))
##print(solution12(n, data))


"""
13) Имеется набор данных, состоящий из положительных целых чисел. Необходимо
определить количество пар элементов (ai, aj) этого набора,
в которых 1   i + 7  j  N и произведение элементов кратно 14. 
Входные данные: Даны два входных файла: файл A (27-13a.txt) и файл B
(27-13b.txt), каждый из которых содержит в первой строке количество чисел N
(1 ≤ N ≤ 100000). Каждая из следующих N строк содержит натуральное число,
не превышающее 1000.
Пример входного файла:
9
7
5
6
12
5
11
8
16
14
Для указанных входных данных количество подходящих пар должно быть равно 3.
В приведённом наборе имеются три подходящие пары (7, 16), (7, 14), (5, 14),
произведение элементов которых кратно 14, а индексы элементов
последовательности различаются не меньше, чем на 7. 
В ответе укажите два числа: сначала количество подходящих пар для файла А,
затем для файла B.
"""
### TODO: Ответ — 30 360137507
##def solution13(n, data):
##    res = 0
##    c2 = [0] * n
##    c7 = [0] * n
##    c14 = [0] * n
##    for i, elem in enumerate(data):
##        if not elem % 14:
##            res += i - 6 if i - 7 >= 0 else 0
##            c14[i] += 1
##        elif not elem % 2:
##            res += c7[i-7] if i - 7 >= 0 else 0
##            res += c14[i-7] if i - 7 >= 0 else 0
##            c2[i] += 1
##        elif not elem % 7:
##            res += c2[i-7] if i - 7 >= 0 else 0
##            res += c14[i-7] if i - 7 >= 0 else 0
##            c7[i] += 1
##        else:
##            res += c14[i-7] if i - 7 >= 0 else 0
##
##        c14[i] += c14[i-1] if i != 0 else 0
##        c7[i] += c7[i-1] if i != 0 else 0
##        c2[i] += c2[i-1] if i != 0 else 0
##        
##    return res
##
##
##with open('data/13/27.txt') as f:
##    n = int(f.readline())
##    data = list(map(int, f.readlines()))
##print(solution13(n, data))
##
##
##with open('data/13/27-13a.txt') as f:
##    n = int(f.readline())
##    data = list(map(int, f.readlines()))
##print(solution13(n, data))
##
##
##with open('data/13/27-13b.txt') as f:
##    n = int(f.readline())
##    data = list(map(int, f.readlines()))
##print(solution13(n, data))


"""
14) [77] (Д.В. Богданов) Имеется набор данных, состоящий из положительных
целых чисел. Необходимо определить количество пар элементов (ai, aj) этого
набора, в которых 1  i < j  N и сумма элементов кратна 12. 
Входные данные: Даны два входных файла: файл A (27-14a.txt) и файл B
(27-14b.txt), каждый из которых содержит в первой строке количество чисел N
(1 ≤ N ≤ 100000). Каждая из следующих N строк содержит натуральное число,
не превышающее 1000.
Пример входного файла:
5
7
5
6
12
24
Для указанных входных данных количество подходящих пар должно быть равно 2.
В приведённом наборе имеются две пары (7, 5) и (12, 24), сумма элементов
которых кратна 12. 
В ответе укажите два числа: сначала количество подходящих пар для файла А,
затем для файла B.
"""
### TODO: Ответ — 17 150016535
##def solution14(n, data):
##    res = 0
##    osts = [0] * 12
##    for elem in data:
##        res += osts[(12 - elem % 12) % 12]
##        osts[elem % 12] += 1
##    return res
##
##
##with open('data/14/27.txt') as f:
##    n = int(f.readline())
##    data = list(map(int, f.readlines()))
##print(solution14(n, data))
##
##
##with open('data/14/27-14a.txt') as f:
##    n = int(f.readline())
##    data = list(map(int, f.readlines()))
##print(solution14(n, data))
##
##
##with open('data/14/27-14b.txt') as f:
##    n = int(f.readline())
##    data = list(map(int, f.readlines()))
##print(solution14(n, data))



"""
15) Имеется набор данных, состоящий из положительных целых чисел.
Необходимо определить количество пар элементов (ai, aj) этого набора,
в которых 1  i + 5  j  N и сумма элементов кратна 14. 
Входные данные: Даны два входных файла: файл A (27-15a.txt) и файл B
(27-15b.txt), каждый из которых содержит в первой строке количество чисел N
(1 ≤ N ≤ 100000). Каждая из следующих N строк содержит натуральное число,
не превышающее 1000.
Пример входного файла:
8
7
5
6
12
24
7
9
12
Для указанных входных данных количество подходящих пар должно быть равно 2.
В приведённом наборе имеются две пары (7, 7) и (5, 9), сумма элементов которых
кратна 14 и индексы в последовательности отличаются не менее, чем на 5. 
В ответе укажите два числа: сначала количество подходящих пар для файла А,
затем для файла B.
"""
### FIXME: Ответ — 
from pprint import pprint


def solution15(n, data):
    res = 0
    osts = [[0] * 14 for i in range(n)]
    for i, elem in enumerate(data):
        res += osts[i-5][(14 - elem % 14) % 14] if i - 5 >= 0 else 0
        osts[i][elem % 14] += 1
        osts[i] = [osts[i][j % 14] + elemj for j, elemj in enumerate(osts[i-1])]
##        print(i, elem, elem % 14, res)
##        pprint(osts)
##        input()
    return res


with open('data/15/27.txt') as f:
    n = int(f.readline())
    data = list(map(int, f.readlines()))
print(solution15(n, data))


with open('data/15/27-15a.txt') as f:
    n = int(f.readline())
    data = list(map(int, f.readlines()))
print(solution15(n, data))


with open('data/15/27-15b.txt') as f:
    n = int(f.readline())
    data = list(map(int, f.readlines()))
print(solution15(n, data))
