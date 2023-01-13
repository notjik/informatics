"""
2. (Е. Джобс) Логическая функция F задаётся выражением (a → d) ∧ ¬(b → c).
На рисунке приведён частично заполненный фрагмент
таблицы истинности функции F, содержащий неповторяющиеся строки. Определите, какому столбцу
таблицы истинности функции F соответствует каждая из переменных a, b, c, d.
"""
# # TODO: Ответ – dabc
# print('d a b c f')
# for d, a, b, c in product([0, 1], repeat=4):
#     f = int((not a or d) and not (not b or c))
#     if f:
#         print(d, a, b, c, f)


"""
5. Автомат получает на вход трёхзначное число. По этому числу строится новое число по следующим
правилам.
1. Из цифр, образующих десятичную запись N, строятся наибольшее и наименьшее возможные
двузначные числа (числа не могут начинаться с нуля).
2. На экран выводится разность полученных двузначных чисел.
Пример. Дано число N = 351. Наибольшее двузначное число из заданных цифр – 53, наименьшее – 13.
На экран выводится разность 53 – 13 = 40.
Чему равно количество трёхзначных чисел N, в результате обработки которых на экране автомата
появится число 35?
"""
# # TODO: Ответ – 882
# c = 0
# for n in range(100, 1000):
#     nmb = list(set(int(''.join(i)) for i in permutations(str(n), r=2) if 10 <= int(''.join(i)) <= 100))
#     if max(nmb) - min(nmb):
#         c += 1
# print(c)


"""
6. (А. Минак) Исполнитель Чертёжник перемещается на координатной плоскости, оставляя след в
виде линии. Чертёжник может выполнять команду Сместиться на (a,b) (где a, b — целые числа),
перемещающую Чертёжника из точки с координатами (x, y) в точку с координатами (x+a, y+b). Если
числа a, b положительные, то значение соответствующей координаты увеличивается, если
отрицательные — уменьшается. Например, если Чертёжник находится в точке с координатами (4, 2),
то команда Сместиться на (2,-3) переместит Чертёжника в точку (6,-1). Запись
Повтори k раз
 Команда1 Команда2 Команда3
конец
означает, что последовательность Команда1 Команда2 Команда3 повторится k раз.
Чертёжнику был дан для исполнения следующий алгоритм:
Повтори 10 раз
 Сместиться на (200, 100)
 Сместиться на (-50, -150)
 Сместиться на (-150, 50)
конец
Определите, сколько точек с целочисленными координатами принадлежат траектории движения
Чертёжника.
"""
# # TODO: Ответ – 200 (50 * 4 = 200)
# from turtle import *
#
# screensize(30, 30)
# speed(1000000)
# left(90)
# m = 30
# color('black')
# come = [(4 * m, 2 * m),  # 200/5 ; 100/5
#         (-1 * m, -3 * m),  # -50/5 ; -150/5
#         (-3 * m, 1 * m)]  # -150/5 ; 50/5
# x, y = 0, 0
# for j in come:
#     x, y = x + j[0], y + j[1]
#     goto(x, y)
# penup()
#
# for x in range(-10 * m, 10 * m, m):
#     for y in range(-10 * m, 10 * m, m):
#         goto(x, y)
#         dot(3, 'green')
#
# mainloop()


"""
8. Петя составляет 4-буквенные слова из букв Н, О, Д, А. Каждую букву нужно использовать ровно 1
раз, при этом нельзя ставить подряд две гласные или две согласные. Сколько различных кодов может
составить Петя?
"""
# # TODO: Ответ – 24
# c = 0
# for s in permutations('НОДА'):
#     s = ''.join(s)
#     if 'ОА' not in s or 'АО' not in s or 'НД' not in s or 'ДН' not in s:
#         c += 1
# print(c)


"""
12. Исполнитель Редактор получает на вход строку цифр и преобразовывает её. Редактор может
выполнять две команды, в обеих командах v и w обозначают цепочки цифр.
1. заменить (v, w)
2. нашлось (v)
Первая команда заменяет в строке первое слева вхождение цепочки v на цепочку w. Если цепочки v в
строке нет, эта команда не изменяет строку. Вторая команда проверяет, встречается ли цепочка v в
строке исполнителя Редактор. Если она встречается, то команда возвращает логическое значение
«истина», в противном случае возвращает значение «ложь». Дана программа для исполнителя
Редактор:
НАЧАЛО
 ПОКА нашлось (5555)
 заменить (5555, 33)
 заменить (333, 5)
 КОНЕЦ ПОКА
КОНЕЦ
Какая строка получится в результате применения приведённой ниже программы к строке, состоящей
из 150 цифр 5?
"""
# # TODO: Ответ – 5355
# s = '5' * 150
# while '5555' in s:
#     s = s.replace('5555', '33', 1)
#     s = s.replace('333', '5', 1)
# print(s)


"""
14. В какой системе счисления выполняется равенство 21X · 13X = 313X? В ответе укажите число –
основание системы счисления.
"""
# # TODO: Ответ – 6
# for x in range(4, 37):
#     if int('21', x) * int('13', x) == int('313', x):
#         print(x)


"""
15. Укажите наименьшее целое значение А, при котором выражение
(x + 3y ≠ 27) ∨ ((A > x) ∧ (A > y))
истинно для любых целых неотрицательных значений x и y
"""
# # TODO: Ответ – 28
# for A in range(100):
#     flag = True
#     for x in range(100):
#         for y in range(100):
#             if not ((x + 3*y != 27) or ((A > x) and (A > y))):
#                 flag = False
#                 break
#         if not flag:
#             break
#     if flag:
#         print(A)
#         break


"""
16. Алгоритм вычисления значений функций F(n) и G(n), где n – натуральное число, задан
следующими соотношениями:
F(1) = 1; G(1) = 1;
F(n) = F(n–1) – n·G(n–1), при n >=2
G(n) = F(n–1) + 2·G(n–1), при n >=2
Чему равно значение величины G(18)?
"""
#
#
# def F(n):
#     if n == 1: return 1
#     return F(n - 1) - n * G(n - 1)
#
#
# def G(n):
#     if n == 1: return 1
#     return F(n - 1) + 2 * G(n - 1)
#
#
# # TODO: Ответ – 87810480
# print(G(18))


"""
17. В файле 17-243.txt содержится последовательность целых чисел. Элементы последовательности
могут принимать целые значения от 0 до 10 000 включительно. Определите количество пар чисел, в
которых хотя бы один из двух элементов больше, чем наибольшее из всех чисел в файле, делящихся
на 133, и в восьмеричной записи хотя бы одного элемента из двух содержится цифра 3. В ответе
запишите два числа: сначала количество найденных пар, а затем – минимальную сумму элементов
таких пар. В данной задаче под парой подразумевается два идущих подряд элемента
последовательности.
"""
# TODO: Ответ – 34 11169
with open('data/17-243.txt') as f:
    data = list(map(int, f.readlines()))
mx133 = max([i for i in data if not (i % 133)])
c = 0
mn = 30000
for i in range(len(data) - 1):
    if any((data[i] > mx133, data[i+1] > mx133)) and any(('3' in oct(data[i])[2:], '3' in oct(data[i+1])[2:])):
        c += 1
        mn = min(mn, data[i] + data[i+1])
print(c, mn)
