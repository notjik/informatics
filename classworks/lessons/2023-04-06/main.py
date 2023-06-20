from functools import lru_cache

'''
1 Алгоритм вычисления значения функции F(n), где n – целое число, задан следующими соотношениями:
F(n) = n, при n ≤ 5,
F(n) = n + F(n / 3 + 2), когда n > 5 и делится на 3,
F(n) = n + F(n + 3) , когда n > 5 и не делится на 3.
Назовите минимальное значение n, для которого F(n) определено и больше 1000.
'''
### TODO: Ответ – 732
##def F(n):
##    if n <= 5:
##        return n
##    return n + F(n / 3 + 2) if not n % 3 else -10**100
##
##
##for i in range(1, 10000):
##    if F(i) > 1000:
##        print(i)
##        break


'''
2 Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
F(n) = n*n*n + n*n + 1, при n ≤ 13
F(n) = F(n-1) + 2*n*n - 3, при n > 13, кратных 3
F(n) = F(n-2) + 3*n + 6, при n > 13, не кратных 3
Определите количество натуральных значений n из отрезка [1; 1000], для которых все цифры значения F(n)
нечётные.
'''
### TODO: Ответ – 14
##def F(n):
##    if n <= 13:
##        return n*n*n + n*n + 1
##    return F(n-1) + 2*n*n - 3 if not n % 3 else F(n-2) + 3*n + 6
##
##
##c = 0
##for i in range(1, 1001):
##    if all(int(l) & 1 for l in str(F(i))):
##        c += 1
##print(c)


'''
3 (А. Кабанов) Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими
соотношениями:
F(n) = n, если n ≥ 10 000,
F(n) = n + F(n / 3), если n < 10 000 и n делится на 3,
F(n) = 2·n + F(n + 3) , если n < 10 000 и n не делится на 3.
Чему равно значение выражения F(999) – F(46)?
'''
### TODO: Ответ – 1683
##@lru_cache(None)
##def F(n):
##    if n >= 10000:
##        return n 
##    return n + F(n // 3) if not n % 3 else 2*n + F(n + 3)
##
##
##for i in range(10000, 46, -1):
##    if i % 3:
##        F(i)
##
##for i in range(10000, 46, -1):
##    if not i % 3:
##        F(i)
##
##print(F(999) - F(46))
    

'''
4 Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
F(n) = 1, при n ≤ 1
F(n) = n + F(n–1), при чётном n > 1;
F(n) = n*n + F(n-2), при нечётном n > 1;
Определите значение F(80).
'''
### TODO: Ответ – 85400
##@lru_cache(None)
##def F(n):
##    if n <= 1:
##        return 1 
##    return n + F(n-1) if not n & 1 else n*n + F(n-2)
##
##
##print(F(80))


'''
5 (А. Кабанов) В файле 17-3.txt содержится последовательность целых чисел. Элементы последовательности
могут принимать целые значения от -10 000 до 10 000 включительно. Определите и запишите в ответе сначала
количество четвёрок элементов последовательности, в которых числа идут в порядке убывания, при этом
разность наибольшего и наименьшего числа больше 1000, затем минимальную сумму элементов таких четвёрок.
В данной задаче под четвёркой подразумевается четыре идущих подряд элемента последовательности.
'''
### TODO: Ответ – 181 -31478
##with open('data/17-3.txt') as f:
##    data = list(map(int, f.readlines()))
##c = 0
##mn = 40000
##for i in range(len(data) - 3):
##    four = data[i:i+4]
##    if sorted(four, reverse=True) == four and max(four) - min(four) > 1000:
##        c += 1
##        mn = min(mn, sum(four))
##print(c, mn)


'''
6 В файле 17-243.txt содержится последовательность целых чисел. Элементы последовательности могут
принимать целые значения от 0 до 10 000 включительно. Определите количество пар чисел, в которых хотя бы
один из двух элементов больше, чем наибольшее из всех чисел в файле, делящихся на 171, и хотя бы один
элемент из двух содержит стоящие рядом две цифры 1. В ответе запишите два числа: сначала количество
найденных пар, а затем – минимальную сумму элементов таких пар. В данной задаче под парой
подразумевается два идущих подряд элемента последовательности.
'''
### TODO: Ответ – 25 10899
##with open('data/17-243.txt') as f:
##    data = list(map(int, f.readlines()))
##mx171 = max(i for i in data if not i % 171)
##c = 0
##mn = 20000
##for i in range(len(data) - 1):
##    pair = data[i:i+2]
##    if any(elem > mx171 for elem in pair) and any('11' in str(elem) for elem in pair):
##        c += 1
##        mn = min(mn, sum(pair))
##print(c, mn)


'''
7 (П. Волгин) В файле 17-5.txt содержится последовательность целых чисел. Элементы последовательности
могут принимать значения от –100 до 100 включительно. Определите сначала количество пар элементов
последовательности, в которых оба числа оканчивается на 5, а затем максимальную из сумм элементов таких
пар. Под парой подразумевается два идущих подряд элемента последовательности. Например, для
последовательности из 5 элементов: 5, 35, –15, 7, 5 ответ должен быть 2 40.
'''
### TODO: Ответ – 1 40
##with open('data/17-5.txt') as f:
##    data = list(map(int, f.readlines()))
##c = 0
##mx = -200
##for i in range(len(data) - 1):
##    if all(abs(elem) % 10 == 5 for elem in data[i:i+2]):
##        c += 1
##        mx = max(mx, sum(data[i:i+2]))
##print(c, mx)


'''
8 (А. Кабанов) В файле 17-4.txt содержится последовательность целых чисел. Элементы последовательности
могут принимать целые значения от 0 до 10 000 включительно. Рассматривается множество элементов
последовательности, которые удовлетворяют следующим условиям:
− сумма последних двух цифр не менее 15;
− не делится на 3, 4 и 7.
Найдите минимальное из таких чисел и их сумму. Гарантируется, что искомая сумма не превосходит 107.
'''
### TODO: Ответ – 1189 460004
##with open('data/17-4.txt') as f:
##    data = list(map(int, f.readlines()))
##res = [n for n in data if n % 10 + n % 100 // 10 >= 15 and all(n % i for i in [3, 4, 7])]
##print(min(res), sum(res))