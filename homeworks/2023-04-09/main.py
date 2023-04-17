from itertools import product, permutations
from math import ceil
from functools import lru_cache


def to_base(n, b):
    a = [chr(c) for c in range(48, 58)] + [chr(c) for c in range(97, 123)]
    r = a[n % b]
    while n >= b:
        n //= b
        r += a[n % b]
    return r[::-1]


"""
1 Между населёнными пунктами A, B, C, D, E, F, Z построены дороги с односторонним движением. В таблице
указана протяжённость каждой дороги. Отсутствие числа в таблице означает, что прямой дороги между
пунктами нет. Например, из A в B есть дорога длиной 4 км, а из B в A дороги нет.
Сколько существует таких маршрутов из A в Z, которые проходят через 6 и
более населенных пунктов? Пункты A и Z при подсчете учитывать. Два раза проходить через один пункт
нельзя.
"""
# # TODO: Ответ — 26 (2+7+11+6)


"""
2 (В.Н. Шубинкин) Логическая функция F задаётся выражением (x ≡ y) → (z ≡ w). Ниже приведён частично
заполненный фрагмент таблицы истинности этой функции, содержащий неповторяющиеся строки. Сколькими
способами можно поставить в соответствие переменные w, x, y, z столбцам таблицы истинности функции F,
опираясь на информацию из данного фрагмента?
"""
# # TODO: Ответ — 12
# res_table = [[0, 0, 0, 1, 0],
#              [1, 1, 1, 0, 0]]
# res = 0
# for first, second, third, forth in permutations((0, 1, 3, 2)):
#     table = []
#     for row in product((0, 1), repeat=len(res_table[0]) - 1):
#         f = int(not (row[first] == row[second]) or (row[third] == row[forth]))
#         table.append(list(row) + [f])
#     if all([i in table for i in res_table]):
#         res += 1
# print(res)


"""
3 (М. Ишимов) В файле 3-101.xls приведён фрагмент базы данных «Продукты» о поставках товаров в магазины
районов города. База данных состоит из трёх таблиц. Таблица «Движение товаров» содержит записи о
поставках товаров в магазины в течение первой декады июня 2021 г., а также информацию о проданных
товарах. Поле Тип операции содержит значение Поступление или Продажа, а в соответствующее поле
Количество упаковок, шт. занесена информация о том, сколько упаковок товара поступило в магазин или было
продано в течение дня. Таблица «Товар» содержит информацию об основных характеристиках каждого товара.
Таблица «Магазин» содержит информацию о местонахождении магазинов. На рисунке приведена схема
указанной базы данных.
Используя информацию из приведённой базы данных, определите
наибольшее количество проданных упаковок из всех видов шоколада в магазинах Промышленного района, за
период с 2 по 10 августа включительно. В ответе запишите только число.
"""
# # TODO: Ответ — 1864


"""
4 (А.Н. Носкин) Для кодирования некоторой последовательности, состоящей из букв А, Б, В, Г, Д, решили
использовать неравномерный двоичный код, удовлетворяющий условию Фано. Для букв А, Б, В, Г
использовали соответственно кодовые слова 011, 010, 001, 0001. Укажите возможное кодовое слово для буквы
Д, при котором код будет допускать однозначное декодирование. Если таких кодов несколько, укажите код с
наименьшим числовым значением.
"""
# # TODO: Ответ — 0000


"""
5 Автомат обрабатывает натуральное число N по следующему алгоритму:
1) Строится двоичная запись числа N.
2) Запись «переворачивается», то есть читается справа налево. Если при этом появляются ведущие нули, они
отбрасываются.
3) Полученное число переводится в десятичную систему счисления и выводится на экран.
Какое наименьшее число, превышающее 500, после обработки автоматом даёт результат 19?
"""
# # TODO: Ответ — 800
# for n in range(500, 10000):
#     r = bin(n)[2:]
#     r = str(r[::-1].rstrip('0'))
#     if int(r, 2) == 19:
#         print(n)
#         break


"""
6 (А. Богданов) Исполнитель Черепаха действует на плоскости с декартовой системой координат. В начальный
момент Черепаха находится в начале координат, её голова направлена вдоль положительного направления оси
ординат, хвост опущен. При опущенном хвосте Черепаха оставляет на поле след в виде линии. В каждый
конкретный момент известно положение исполнителя и направление его движения. У исполнителя существует
две команды: Вперёд n (где n – целое число), вызывающая передвижение Черепахи на n единиц в том
направлении, куда указывает её голова, и Направо m (где m – целое число), вызывающая изменение
направления движения на m градусов по часовой стрелке. Запись
Повтори k [Команда1 Команда2 … КомандаS]
означает, что последовательность из S команд повторится k раз. Черепахе был дан для исполнения следующий
алгоритм:
Повтори 13 [ Направо 135 Вперед 5 ]
Найдите количество точек фигуры, образованных пересечением отрезков, без учета концов самих отрезков.
"""
# # TODO: Ответ — 16
# from turtle import *
#
# m = 50
# color('red', 'blue')
# speed(0)
# left(90)
#
# for _ in range(19):
#     forward(5 * m)
#     right(135)
#
# mainloop()


"""
7 Изображение размером 4х7 дюйма отсканировано с разрешением 300 ppi и использованием 2^24 цветов.
Заголовок файла занимает 6 Кбайт. Определите, сколько Кбайт памяти необходимо выделить для хранения
файла. В ответе введите целое число.
"""
# # TODO: Ответ — 7389
# print(ceil(((4 * 300) * (7 * 300) * 24) / (2**13)) + 6)


"""
8 Вася составляет слова из букв слова АТТЕСТАТ. Код должен состоять из 8 букв, и каждая буква в нём
должна встречаться столько же раз, сколько в заданном слове. Кроме того, в коде должны стоять рядом две
гласные или две согласные буквы. Сколько различных слов может составить Вася?
"""
# # TODO: Ответ — 840
# vowels = [''.join(i) for i in product('АЕ', repeat=2)]
# consonants = [''.join(i) for i in product('ТС', repeat=2)]
# print(vowels, consonants)
# c = 0
# for s in set(permutations('АТТЕСТАТ')):
#     s = ''.join(s)
#     if any(i in s for i in vowels) or any(i in s for i in consonants):
#         c += 1
# print(c)


"""
9 (С. Якунин) В файле электронной таблицы 9-187.xls в каждой строке записаны пять латинских букв.
Определите количество строк таблицы, содержащих ровно 2 одинаковые буквы
"""
# # TODO: Ответ — 326


"""
10 С помощью текстового редактора определите, сколько раз, не считая сносок, встречается предлог «со» (со
строчной буквы) в тексте романа А.С. Пушкина «Капитанская дочка» (файл 10-34.docx). В ответе укажите
только число.
"""
# # TODO: Ответ — 55


"""
11 Сотрудникам компании выдают электронную карту, на которой записаны их личный код, номер
подразделения (целое число от 1 до 120) и дополнительная информация. Личный код содержит 11 символов и
может включать латинские буквы (заглавные и строчные буквы различаются) и десятичные цифры. Для
хранения кода используется посимвольное кодирование, все символы кодируются одинаковым минимально
возможным количеством битов, для записи кода отводится минимально возможное целое число байтов. Номер
подразделения кодируется отдельно и занимает минимально возможное целое число байтов. Известно, что на
карте хранится всего 28 байтов данных. Сколько байтов занимает дополнительная информация?
"""
# # TODO: Ответ — 18
# print(28 - (ceil(7 / 8) + ceil((11 * 6) / 8)))


"""
12 Исполнитель Редактор получает на вход строку цифр и преобразовывает её. Редактор может выполнять две
команды, в обеих командах v и w обозначают цепочки цифр.
1. заменить (v, w)
2. нашлось (v)
Первая команда заменяет в строке первое слева вхождение цепочки v на цепочку w. Если цепочки v в строке
нет, эта команда не изменяет строку. Вторая команда проверяет, встречается ли цепочка v в строке исполнителя
Редактор. Если она встречается, то команда возвращает логическое значение «истина», в противном случае
возвращает значение «ложь». Дана программа для исполнителя Редактор:
НАЧАЛО
ПОКА нашлось (222)
заменить (22, 7)
заменить (77, 2)
КОНЕЦ ПОКА
КОНЕЦ
Какая строка получится в результате применения приведённой ниже программы к строке, состоящей из 103
цифр 2?
"""
# # TODO: Ответ — 722
# s = 103 * '2'
# while '222' in s:
#     s = s.replace('22', '7', 1)
#     s = s.replace('77', '2', 1)
# print(s)


"""
13 На рисунке представлена схема дорог, связывающих города А, Б, В, Г, Д, Е, Ж, З, И, К, Л, М, Н. По каждой
дороге можно двигаться только в одном направлении, указанном стрелкой. Сколько существует различных
путей из пункта А в пункт Н, проходящих через пункт Е?
"""
# # TODO: Ответ — 27


"""
14 (М.В. Кузнецова) Значение арифметического выражения: 9^5 + 3^7 – 14 записали в системе счисления с
основанием 3. Какая из цифр реже всего встречается в этой записи? В ответе укажите, сколько таких цифр в
записи.
"""
# # TODO: Ответ — 3
# expression = to_base(9 ** 5 + 3 ** 7 - 14, 3)
# c_in_exp = [(i, expression.count(i)) for i in set(expression)]
# print(min(filter(lambda x: x[1] == min(c_in_exp, key=lambda y: y[1])[1], c_in_exp), key=lambda z: ord(z[0]))[1])


"""
15 Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число
m». Для какого наибольшего натурального числа А формула
ДЕЛ(x, 18) → (¬ДЕЛ(x, A) → ¬ДЕЛ(x, 12))
тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной х)?
"""
# # TODO: Ответ — 36
# for A in range(1, 10000):
#     flag = True
#     for x in range(1, 10000):
#         f = x % 18 != 0 or (x % A == 0 or x % 12 != 0)
#         if not f:
#             flag = False
#             break
#     if flag:
#         print(A)

"""
16 Алгоритм вычисления значения функции F(n), где n – целое неотрицательное число, задан следующими
соотношениями:
F(0) = 1
F(n) = 1 + F(n - 1), если n > 0 и n нечётное
F(n) = F(n / 2) в остальных случаях
Определите количество значений n на отрезке [1, 500 000 000], для которых F(n) = 4.
"""
# # TODO: Ответ — 3654
# c = 0
# for n in range(1, 500_000_001):
#     if not n % 100_000_000:
#         print('+')
#     if bin(n)[2:].count('1') + 1 == 4:
#         c += 1
# print(c)


"""
17 (А. Кабанов) В файле 17-4.txt содержится последовательность целых чисел. Элементы последовательности
могут принимать целые значения от 0 до 10 000 включительно. Рассматривается множество элементов
последовательности, которые удовлетворяют следующим условиям:
− запись в двоичной системе заканчивается на 1001;
− запись в пятеричной системе заканчивается на 11.
Найдите максимальное из таких чисел и их сумму. Гарантируется, что искомая сумма не превосходит 10^7
"""
# # TODO: Ответ — 6681 23686
# with open('data/17-4.txt') as f:
#     data = list(map(int, f.readlines()))
# mx = 0
# summ = 0
# for i in data:
#     if bin(i).endswith('1001') and to_base(i, 5).endswith('11'):
#         mx = max(mx, i)
#         summ += i
# print(mx, summ)


"""
18 (Е. Джобс) Квадрат разлинован на N×N клеток (2 < N < 20). Исполнитель Робот может перемещаться по
клеткам, выполняя за одно перемещение одну из двух команд: вправо или вверх. По команде вправо Робот
перемещается в соседнюю правую клетку, по команде вверх – в соседнюю верхнюю. При попытке выхода за
границу квадрата Робот разрушается, при столкновении со стеной робот разрушается. Также робот
перемещается вдоль стен, то есть может переместиться только в ту клетку, в которой есть стена. Перед
каждым запуском Робота в каждой клетке квадрата записано число от 10 до 99. Посетив клетку Робот
прибавляет к своему счету записанное в ней значение. Определите максимальное и минимальное значение
счета, который может набрать Робот, пройдя из левой нижней клетки в правую верхнюю.
Исходные данные для Робота записаны в файле 18-116.xls в виде прямоугольной таблицы, каждая ячейка
которой соответствует клетке квадрата. В ответе укажите сначала максимальный, затем минимальный результат,
который может быть получен исполнителем.
"""
# # TODO: Ответ — 1849 1534


"""
19, 20, 21 Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит две кучи камней. Игроки
ходят по очереди, первый ход делает Петя. За один ход игрок может добавить в любую кучу один камень или
добавить добавить в любую кучу столько камней, сколько их в данный момент в другой куче. Игра
завершается в тот момент, когда общее количество камней в двух кучах становится не менее 79. Победителем
считается игрок, сделавший последний ход. В начальный момент в первой куче было 9 камней, а во второй – S
камней, 1 ≤ S ≤ 69.
Ответьте на следующие вопросы:
Вопрос 1. Известно, что Ваня выиграл своим первым ходом после неудачного первого хода Пети. Назовите
минимальное значение S, при котором это возможно.
Вопрос 2. Найдите минимальное и максимальное значение S, при котором у Пети есть выигрышная стратегия,
причём одновременно выполняются два условия:
− Петя не может выиграть за один ход;
− Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.
Найденные значения запишите в ответе в порядке возрастания.
Вопрос 3. Найдите значение S, при котором одновременно выполняются два условия:
– у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре
Пети;
– у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.
"""
# # TODO: Ответ —
# #  19) 21
# #  20) 20 34
# #  21) 33
@lru_cache(None)
def game(x, y):
    if x + y >= 79:
        return 0
    tmp = [game(x + 1, y), game(x, y + 1),
           game(x + y, y), game(x, y + x)]
    ng = [i for i in tmp if i <= 0]
    if ng:
        return -max(ng) + 1
    return -max(tmp)


task2 = [s for s in range(1, 70) if game(9, s) == 2]
print(min(task2), max(task2))
print(*[s for s in range(1, 70) if game(9, s) == -2])
