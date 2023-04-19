from itertools import product, permutations, combinations
from math import ceil
from functools import lru_cache


def to_base(n, b):
    a = [chr(c) for c in range(48, 58)] + [chr(c) for c in range(97, 123)]
    r = a[n % b]
    while n >= b:
        n //= b
        r += a[n % b]
    return r[::-1]


def is_prime(n):
    i = 2
    while i ** 2 <= n:
        if not n % i:
            return False
        i += 1
    return True


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
# @lru_cache(None)
# def game(x, y):
#     if x + y >= 79:
#         return 0
#     tmp = [game(x + 1, y), game(x, y + 1),
#            game(x + y, y), game(x, y + x)]
#     ng = [i for i in tmp if i <= 0]
#     if ng:
#         return -max(ng) + 1
#     return -max(tmp)
#
#
# task2 = [s for s in range(1, 70) if game(9, s) == 2]
# print(min(task2), max(task2))
# print(*[s for s in range(1, 70) if game(9, s) == -2])


"""
22 (А. Кабанов) В файле 22-35.xls содержится информация о совокупности N вычислительных процессов,
которые могут выполняться параллельно или последовательно. Будем говорить, что процесс B зависит от
процесса A, если для выполнения процесса B необходимы результаты выполнения процесса A. Информация о
процессах представлена в файле в виде таблицы. В первом столбце таблицы указан идентификатор процесса
(ID), во втором столбце таблицы – время его выполнения в миллисекундах, в третьем столбце перечислены с
разделителем «;» ID процессов, от которых зависит данный процесс. Если процесс является независимым, то в
таблице указано значение 0. При составлении таблицы была потеряна информация о том, после какого
процесса начался процесс ID = 16. Однако известно, что вся совокупности процессов завершилась за
минимальное время 138 мс. Определите ID процесса, после которого начался процесс с ID = 16. В ответе
укажите только число.
Типовой пример организации данных в файле:
В данном случае независимые процессы 1 и 2 могут выполняться
параллельно, при этом процесс 1 завершится через 4 мс, а процесс 2 – через 3 мс с момента старта. Процесс 3
может начаться только после завершения обоих процессов 1 и 2, то есть, через 4 мс после старта. Он длится 1
мс и закончится через 4 + 1 = 5 мс после старта. Выполнение процесса 4 может начаться только после
завершения процесса, ID которого потеряно. Его продолжительность равно 7 мс. Если бы минимальное время
завершения всех процессов была равно 12 мс, то процесс 4 начинался бы после процесса 3 (12 – 7 = 5мс).
"""
# # TODO: Ответ — 4


"""
23 У исполнителя Калькулятор три команды, которым присвоены номера:
1. прибавь 1
2. умножь на 2
3. умножь на 3
Сколько есть программ, которые число 1 преобразуют в число 14?
"""
# # TODO: Ответ — 48
# def f(x, end):
#     if x > end:
#         return 0
#     if x == end:
#         return 1
#     return f(x + 1, end) + f(x * 2, end) + f(x * 3, end)
#
#
# print(f(1, 14))


"""
24 (Д. Статный) Текстовый файл 24-235.txt состоит не более чем из 10^6 символов и содержит только буквы
XYZWOP. Определите самый часто встречающийся символ в комбинации X*P, который стоит на месте
звездочки. В ответе укажите количество раз, сколько он встретился в данной комбинации.
"""
# # TODO: Ответ — 4683
# with open('data/24-235.txt') as f:
#     s = f.read()
# comb = re.findall(r"X[A-Z]P", s)
# print(max(((i, comb.count("X{}P".format(i))) for i in 'XYZWOP'), key=lambda x: x[1]))


"""
25 Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [2484292;
2484370], простые числа. Выведите все найденные простые числа в порядке возрастания, слева от каждого
числа выведите его номер по порядку
"""
# # TODO: Ответ —
# #  1 2484311
# #  2 2484319
# #  3 2484323
# #  4 2484331
# #  5 2484353
# #  6 2484359
# c = 0
# for i in range(2484292, 2484371):
#     if is_prime(i):
#         c += 1
#         print(c, i)


"""
26 (М. Шагитов) Для экрана размером 10000х10000 пикселей используется цветовая модель RGB. Графический
адаптер считывает пиксели экрана и записывает в файл данные всех пикселей, кроме тех, для которых
установлен белый цвет. Для каждого пикселя записывается номер строки, номер позиции в строке и цвет в виде
шестнадцатеричного кода (например, #FFFFFF – белый цвет). Найдите все пиксели с кодом #00FF00, слева и
справа от которых записаны по три подряд идущих пикселя с кодом #0000FF. Определите общее количество
подходящих пикселей, а также номер строки, в которой есть наибольшее количество таких пикселей.
Гарантируется, что на экране есть хотя бы один подходящий пиксель.
Входные данные представлены в файле 26-87.txt следующим образом. В первой строке входного файла
записано натуральное число N – общее количество записей (1 ≤ N ≤ 100 000). В каждой из следующих N строк
находятся два натуральных числа, не превышающих 10000, и шестнадцатеричный код, разделённые пробелом:
номер строки, номер позиции в строке уникального пикселя и цвет пикселя.
Запишите в ответе два числа: общее количество подходящих пикселей на экране и наибольший номер строки, с
максимальным количеством подходящих пикселей.
Пример входного файла::
11
1 1 #00FF00
1 3 #00FF00
2 1 #0000FF
2 2 #0000FF
2 3 #0000FF
2 4 #00FF00
2 5 #0000FF
2 6 #0000FF
2 7 #0000FF
3 3 #00FF00
3 5 #00FF00
В данном случае есть один подходящий пиксель (строка 2, позиция 4) с кодом цвета #00FF00, окруженный с
двух сторон тройками пикселей с кодом #0000FF. Ответ: 1 2.
"""
# # TODO: Ответ — 1487 9980
# screen = [['#FFFFFF' for _ in range(10000)] for _ in range(10000)]
# with open('data/26-87.txt') as f:
#     n = int(f.readline())
#     data = list(map(lambda x: x.split(), f.readlines()))
# for i in data:
#     screen[int(i[0]) - 1][int(i[1]) - 1] = i[2]
# res = []
# for i, row in enumerate(screen):
#     c = 0
#     for i_col in range(3, len(row) - 3):
#         if row[i_col] == '#00FF00' and all(row[i_col - right] == '#0000FF' for right in range(1, 4)) and \
#                 all(row[i_col + left] == '#0000FF' for left in range(1, 4)):
#             c += 1
#     res.append((i + 1, c))
# print(sum(i[1] for i in res), max(res[::-1], key=lambda x: x[1])[0])


"""
27 Имеется набор данных, состоящий из троек положительных целых чисел. Необходимо выбрать из каждой
тройки два числа так, чтобы сумма всех выбранных чисел не делилась на 5 и при этом была максимально
возможной. Гарантируется, что искомую сумму получить можно. Программа должна напечатать одно число –
максимально возможную сумму, соответствующую условиям задачи.
Входные данные. Даны два входных файла (файл A и файл B), каждый из которых содержит в первой строке
количество троек N (1 ≤ N ≤ 100000). Каждая из следующих N строк содержит три натуральных числа, не
превышающих 10 000.
Пример входного файла:
6
8 3 4
4 8 12
9 5 6
2 8 3
12 3 5
1 4 11
Для указанных входных данных значением искомой суммы должно быть число 89.
В ответе укажите два числа:сначала искомое значение для файла А, затем для файла B.
"""
# # TODO: Ответ — 25034 76468978
def solution(n, data):
    summ = [0]
    for elem in data:
        new_summ = []
        while summ:
            this = summ.pop()
            for double in combinations(elem, r=2):
                new_summ.append(this+sum(double))
        summ = []
        for i in range(5):
            gen = [j for j in new_summ if j % 5 == i]
            if gen:
                summ.append(max(gen))
    return max(i for i in summ if i % 5)


with open('data/27-29t.txt') as f:
    n = int(f.readline())
    data = list(map(lambda x: list(map(int, x.split())), f.readlines()))
print(solution(n, data))

with open('data/27-29a.txt') as f:
    n = int(f.readline())
    data = list(map(lambda x: list(map(int, x.split())), f.readlines()))
print(solution(n, data))

with open('data/27-29b.txt') as f:
    n = int(f.readline())
    data = list(map(lambda x: list(map(int, x.split())), f.readlines()))
print(solution(n, data))
