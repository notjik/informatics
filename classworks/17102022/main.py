from itertools import permutations

'''
23. (№ 3747) Исполнитель Калькулятор преобразует число, записанное на экране.
У исполнителя есть три команды, которым присвоены номера:
1. Прибавь 1
2. Прибавь 2
3. Прибавь 3
Сколько существует программ, которые преобразуют исходное число 5 в число 18,
и при этом траектория вычислений содержит число 11 и не содержит чисел 10 и 15?
'''
##l = [0] * 100 #23
##l[5] = 1
##for i in range(5, 12):
##    l[10] = 0
##    l[15] = 0
##    if i + 1 <= 11:
##        l[i+1] += l[i]
##    if i + 2 <= 11:
##        l[i+2] += l[i]
##    if i + 3 <= 11:
##        l[i+3] += l[i]
##for i in range(11, 19):
##    l[10] = 0
##    l[15] = 0
##    l[i+1] += l[i]
##    l[i+2] += l[i]
##    l[i+3] += l[i]
##print(l[18])


'''
24. (№ 4140) (А. Богданов) Текстовый файл 24-169.txt состоит не более чем из 106
символов X, Y и Z. Определите максимальную длину цепочки символов, состоящей
из повторяющихся фрагментов XYZ. Цепочка может начинаться и заканчиваться
любым символом из XYZ, но внутри цепочки порядок строго определен. Например,
для строки ZZZXYZXYZXZZZ длина цепочки равна 8: Z+XYZ+XYZ+X, где цепочка
начинается с Z и заканчивается X.
'''
##with open('data/24-169.txt') as f:
##    data = f.readline()
##s = 'XYZ'
##l = 0
##while s in data:
##    l = max(l, len(s))
##    for x in ['', 'YZ', 'Z']:
##        for y in ['', 'X', 'XY']:
##            if x + s + y in data:
##                l = max(len(x+s+y), l)
##    s += 'XYZ'
##print(l)


'''
25. (№ 4117) (А. Кабанов) Обозначим через M разность максимального и минимального
натуральных делителей целого числа, не считая единицы и самого числа. Если
таких делителей у числа нет, то считаем значение M равным нулю. Напишите
программу, которая перебирает целые числа, большие 350000, в порядке
возрастания и ищет среди них такие, для которых значение M при делении на 23
даёт в остатке 9. Запишите первые 6 найденных чисел в порядке возрастания,
справа от каждого числа запишите соответствующее значение M.
'''
##def nd(n):
##     return set([x for x in range(2, n // 2 + 1) if n % x == 0])
##
##c = 0
##for x in range(350000, 500000):
##    snd = nd(x)
##    if snd:
##        M = max(snd) - min(snd)
##    else:
##        M = 0
##    if M % 23 == 9:
##        c += 1
##        print(x, M)
##        if c == 6:
##            break


'''
26. (№ 3765) (А. Кабанов) В текстовом файле записан набор натуральных чисел.
Гарантируется, что все числа различны. Рассматриваются пары чисел с чётной
суммой, такие что половина элементов последовательности больше, чем среднее
арифметическое элементов пары. Необходимо определить, сколько в наборе таких
пар, и наибольшее из средних арифметических таких пар.
Входные данные представлены в файле 26-49.txt следующим образом. Первая строка
содержит целое число N – общее количество чисел в наборе. Каждая из следующих
N строк содержит одно число, не превышающее 109.
В ответе запишите два целых числа: сначала количество пар, затем наибольшее
среднее арифметическое.
Пример входного файла:
6 
3 
8 
14 
11 
2 
17
В данном случае есть четыре подходящие пары: 2 и 8 (среднее арифметическое 5),
2 и 14 (среднее арифметическое 8), 3 и 11 (среднее арифметическое 7), 3 и 17
(среднее арифметическое 10). В ответе надо записать числа 4 и 10.
'''
with open('data/26-49.txt') as f:
    n = int(f.readlines())
    data = list(map(int, f.readlines()))
