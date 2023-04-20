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
def solution5(n, data):
    summ = [0]
    for elem in data:
        new_summ = []
        while summ:
            this = summ.pop()
            for num in elem:
                new_summ.append(this + num)
        for i in range(5):
            gen = [num for num in new_summ if num % 5 == i]
            if gen:
                summ.append(min(gen))
    return min(num for num in summ if not num % 5)

with open('data/5/27-5t.txt') as f:
    n = int(f.readline())
    data = list(map(lambda x: list(map(int, x.split())), f.readlines()))
print(solution5(n, data))

with open('data/5/27-5a.txt') as f:
    n = int(f.readline())
    data = list(map(lambda x: list(map(int, x.split())), f.readlines()))
print(solution5(n, data))

with open('data/5/27-5b.txt') as f:
    n = int(f.readline())
    data = list(map(lambda x: list(map(int, x.split())), f.readlines()))
print(solution5(n, data))
