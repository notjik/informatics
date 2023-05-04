import re

from itertools import product, permutations
from math import ceil
from functools import reduce, lru_cache

"""
1 (ЕГЭ-2022) На рисунке схема дорог Н-ского района изображена в виде графа, в таблице содержатся данные о
протяженности дорог между населёнными пунктами (в километрах). Так как таблицу и схему рисовали
независимо друг от друга, то нумерация населённых пунктов в таблице никак не связана с буквенными
обозначениями на графе.

Определите, какова сумма протяженностей дорог из пункта A в пункт D и из пункта G в пункт C.
"""
# # TODO: Ответ — 66


"""
2 Логическая функция F задаётся выражением ((z → y) ∧ (¬ x → w)) → ((z ≡ w) ∨ (y ∧ ¬ x)). На рисунке
приведён частично заполненный фрагмент таблицы истинности функции F, содержащий неповторяющиеся
строки. Определите, какому столбцу таблицы истинности функции F соответствует каждая из переменных x, y,
z, w.
В ответе напишите буквы x, y, z, w в том порядке, в котором идут
соответствующие им столбцы. Буквы в ответе пишите подряд, никаких разделителей между буквами ставить не
нужно.
"""
# # TODO: Ответ — wzyx
# print('w z y x f')
# for x, y, z, w in product((0, 1), repeat=4):
#     f = int(not ((not z or y) and (x or w)) or ((z == w) or (y and not x)))
#     if not f:
#         print(w, z, y, x, f)


"""
3 (Е. Джобс) В файле 3-2.xls приведён фрагмент базы данных «Рейсы» о рейсах самолетов. База данных состоит
из одной таблицы. Таблица «Рейсы» содержит записи о городах отправления и прибытия, и также номер борта,
совершающего рейс. На рисунке приведена схема данных.
Используя информацию из приведённой базы данных, определите какой борт больше всего
летал по маршруту Екатеринбург — Краснодар. В ответе запишите только число – номер борта.
"""
# # TODO: Ответ — 100


"""
4 Для кодирования некоторой последовательности, состоящей из букв А, Б, В, Г и Д, используется
неравномерный двоичный код, позволяющий однозначно декодировать полученную двоичную
последовательность. Вот этот код:
А – 00; Б – 101; В – 011; Г – 111; Д – 110.
Как можно сократить длину кодового слова для буквы Б так, чтобы код по-прежнему можно было
декодировать однозначно? Коды остальных букв меняться не должны. Если есть несколько вариантов,
выберите кодовое слово с минимальным значением.
"""
# # TODO: Ответ — 01


"""
5 На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим
образом.
1. Строится двоичная запись числа N.
2. К этой записи дописываются справа ещё два разряда по следующему правилу:
а) складываются все цифры двоичной записи, и остаток от деления суммы на 2 дописывается в конец числа
(справа). Например, запись 11100 преобразуется в запись 111001;
б) над этой записью производятся те же действия – справа дописывается остаток от деления суммы цифр на 2.
Полученная таким образом запись (в ней на два разряда больше, чем в записи исходного числа N) является
двоичной записью искомого числа R. Укажите такое наименьшее число N, для которого результат работы
алгоритма больше 137. В ответе это число запишите в десятичной системе счисления.
"""
# # TODO: Ответ — 35
# for n in range(10000):
#     r = bin(n)[2:]
#     for _ in range(2):
#         r += str(sum(map(int, r)) % 2)
#     if int(r, 2) > 137:
#         print(n)
#         break


"""
6 (А. Кабанов) Исполнитель Черепаха действует на плоскости с декартовой системой координат. В начальный
момент Черепаха находится в начале координат, её голова направлена вдоль положительного направления оси
ординат, хвост опущен. При опущенном хвосте Черепаха оставляет на поле след в виде линии. В каждый
конкретный момент известно положение исполнителя и направление его движения. У исполнителя существует
две команды: Вперёд n (где n – целое число), вызывающая передвижение Черепахи на n единиц в том
направлении, куда указывает её голова, и Направо m (где m – целое число), вызывающая изменение
направления движения на m градусов по часовой стрелке. Запись
Повтори k [Команда1 Команда2 … КомандаS]
означает, что последовательность из S команд повторится k раз. Черепахе был дан для исполнения следующий
алгоритм:
Повтори 100 [Вперёд 10 Направо 80]
Определите, из какого количества отрезков будет состоять фигура, заданная данным алгоритмом.
"""
# # TODO: Ответ — 9
# from turtle import *
#
# m = 30
# screensize(10000, 10000)
# color('red', 'blue')
# speed(0)
# left(90)
# begin_fill()
#
# for _ in range(100):  # for _ in range(9) так же может построить эту фигуру
#     forward(10 * m)
#     right(80)
#
# end_fill()
# mainloop()


"""
7 Для хранения в информационной системе документы сканируются с разрешением 200 dpi и цветовой
системой, содержащей 256 цветов. Методы сжатия изображений не используются. Средний размер
отсканированного документа составляет 6 Мбайт. Для повышения качества представления информации было
решено перейти на разрешение 300 dpi и цветовую систему, содержащую 2**16 = 65536 цветов. Сколько Мбайт
будет составлять средний размер документа, отсканированного с изменёнными параметрами?
"""
# # TODO: Ответ — 27
# print(6 * (16 / 8) * ((300 * 300) / (200 * 200)))


"""
8 (А. Богданов) Оля составляет слова перестановкой букв слова СПОРТЛОТО, оставляя только слова с
гласной и в начале, и в конце слова. Сколько различных слов может составить Оля?
"""
# # TODO: Ответ — 2520
# vowels = 'О'
# c = 0
# for s in set(permutations('СПОРТЛОТО')):
#     if s[0] in vowels and s[-1] in vowels:
#         c += 1
# print(c)


"""
9 (Е. Джобс) Откройте файл электронной таблицы 9-j5.xls, содержащей вещественные числа – количество
баллов, которое набрали участники тестирования. В первой строке указаны дисциплины, во второй –
максимальный балл за тест по дисциплине, в левом столбце – фамилии участников. Считается, что тест
пройден, если участник тестирования набрал больше 60% от максимального балла. В качестве ответа укажите,
сколько участников тестирования прошли больше трёх тестов.
"""
# # TODO: Ответ — 18


"""
10 С помощью текстового редактора определите, сколько раз, не считая сносок, встречается слово «слезы»
или «Слезы» (в любом падеже) в тексте романа А.С. Пушкина «Капитанская дочка» (файл 10-34.docx). В ответе
укажите только число.
"""
# # TODO: Ответ — 13


"""
11 Каждый сотрудник предприятия получает электронный пропуск, на котором записаны личный код
сотрудника, код подразделения и некоторая дополнительная информация. Личный код состоит из 11 символов,
каждый из которых может быть заглавной латинской буквой (используется 15 различных букв) или одной из
цифр от 0 до 9. Для записи кода на пропуске отведено минимально возможное целое число байт. При этом
используют посимвольное кодирование, все символы кодируют одинаковым минимально возможным
количеством бит. Код подразделения состоит из 8 символов: в каждой из пяти первых позиций стоит одна из
26 латинских букв, затем – три десятичных цифры. Код подразделения записан на пропуске как двоичное число
(используется посимвольное кодирование) и занимает минимально возможное целое число байт. Всего на
пропуске хранится 30 байт данных. Сколько байт выделено для хранения дополнительных сведений об одном
сотруднике? В ответе запишите только целое число – количество байт.
"""
# # TODO: Ответ — 18
# print(30 - (ceil((5*11)/8)+ceil((5*5+3*4)/8)))


"""
12 (Е. Джобс) Исполнитель Редактор получает на вход строку цифр и преобразовывает её. Редактор может
выполнять две команды, в обеих командах v и w обозначают цепочки символов.
1. заменить (v, w)
2. нашлось (v)
Первая команда заменяет в строке первое слева вхождение цепочки v на цепочку w. Если цепочки v в строке
нет, эта команда не изменяет строку. Вторая команда проверяет, встречается ли цепочка v в строке исполнителя
Редактор.
Дана программа для исполнителя Редактор:
ПОКА нашлось(42) или нашлось(32)
ЕСЛИ нашлось(42)
ТО заменить(42, 51)
ИНАЧЕ заменить(32, 61)
КОНЕЦ ПОКА
На вход программе подана строка, содержащая только 20 двоек, 15 троек и 10 четверок. Порядок символов
заранее неизвестен. Определите максимально возможную сумму всех цифр в конечной строке.
"""
# # TODO: Ответ — 155
# s = '32' * 15 + '42' * 5 + '4' * 5
# while '42' in s or '32' in s:
#     if '42' in s:
#         s = s.replace('42', '51', 1)
#     else:
#         s = s.replace('32', '61', 1)
# print(sum(map(int, s)))


"""
13 На рисунке изображена схема дорог, связывающих города А, Б, В, Г, Д, Е, Ж, З, И, К, Л, М. По каждой
дороге можно двигаться только в одном направлении, указанном стрелкой. Сколько существует различных
путей из города А в город М, не проходящих через город Е?
"""
# # TODO: Ответ — 30


"""
14 В системе счисления с основанием p выполняется равенство
4x46 + xx17 = y386y
Буквами x и y обозначены некоторые цифры из алфавита системы счисления с основанием p. Определите
значение числа xyxyp и запишите это значение в десятичной системе счисления.
"""
# # TODO: Ответ — 17545
# a = [chr(i) for i in range(ord('0'), ord('9') + 1)] + [chr(l) for l in range(ord('A'), ord('Z') + 1)]
# term = lambda s, x, y: s.replace('x', a[x]).replace('y', a[y])
# for p in range(9, 37):
#     for x, y in product(range(p), repeat=2):
#         exp = int(term('4x46', x, y), p) + int(term('xx17', x, y), p) == int(term('y386y', x, y), p)
#         if exp:
#             print(int(term('xyxy', x, y), p))


"""
15 На числовой прямой даны два отрезка: P=[15;33] и Q=[45;68]. Укажите наибольшую возможную длину
такого отрезка A, что формула
( (x ∈ A) ∧ ¬(x ∈ Q)) → ((x ∈ P) ∨ (x ∈ Q))
"""
# # TODO: Ответ — 23


"""
16 Алгоритм вычисления значения функции F(n), где n – целое число, задан следующими соотношениями:
F(n) = 1, при n < 2,
F(n) = F(n/2) + 1, когда n ≥ 2 и чётное,
F(n) = F(n - 3) + 3, когда n ≥ 2 и нечётное.
Назовите минимальное значение n, для которого F(n) равно 31.
"""
# # TODO: Ответ — 893
# def F(n):
#     if n < 2:
#         return 1
#     return F(n // 2) + 1 if not n & 1 else F(n - 3) + 3
#
#
# for n in range(1000):
#     if F(n) == 31:
#         print(n)
#         break


"""
17 (П. Финкель) В файле 17-346.txt содержится последовательность целых чисел. Элементы последовательности
могут принимать целые значения от 1 до 200 000 включительно. Определите количество троек
последовательности, для которых произведение всех цифр трёх чисел не превосходит 2·10
9 и удовлетворяет
маске «43*6*». В качестве ответа укажите количество таких троек и наибольшее произведение их цифр. В
данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.
"""
# # TODO: Ответ — 10 438939648
# with open('data/17-346.txt') as f:
#     data = list(map(int, f.readlines()))
# c = 0
# mx = 0
# for i in range(len(data) - 2):
#     prod = reduce(lambda a, b: int(a) * int(b), ''.join(map(str, data[i:i + 3])))
#     if prod <= 2 * 10 ** 9 and re.match(r'43\d*6\d*', str(prod)) is not None:
#         c += 1
#         mx = max(mx, prod)
# print(c, mx)


"""
18 Квадрат разлинован на N×N клеток (1 < N < 20). Исполнитель Робот может перемещаться по клеткам,
выполняя за одно перемещение одну из трёх команд: вправо, вниз или вправо-вниз. По команде вправо Робот
перемещается в соседнюю правую клетку, по команде вниз – в соседнюю нижнюю, а по команде вправо-вниз –
на одну клетку вправо и вниз по диагонали. При попытке выхода за границу квадрата Робот разрушается. Перед
каждым запуском Робота в каждой клетке квадрата записана величина вознаграждения от 1 до 100. Попав в
клетку после хода вправо или вниз, Робот получает указанное в ней вознаграждение, а если он попал в клетку
после выполнения команды вправо-вниз, вознаграждение удваивается. Это также относится к начальной и
конечной клетке маршрута Робота. Определите максимальное и минимальное вознаграждение, которое может
получить Робот, пройдя из левой верхней клетки в правую нижнюю. В ответе укажите два числа – сначала
максимальное вознаграждение, затем минимальное.
Исходные данные для Робота записаны в файле 18-95.xls в виде прямоугольной таблицы, каждая ячейка
которой соответствует клетке квадрата
"""
# # TODO: Ответ — 740 353


"""
19, 20, 21 Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежат две кучи камней. Игроки
ходят по очереди, первый ход делает Петя. За один ход игрок может добавить в одну из куч один камень или
увеличить количество камней в куче в два раза. Чтобы делать ходы, у каждого игрока есть неограниченное
количество камней. Игра завершается в тот момент, когда суммарное количество камней в кучах становится не
менее 63. Победителем считается игрок, сделавший последний ход, т. е. первым получивший позицию, в
которой в кучах будет 63 или больше камней.
В начальный момент в первой куче было 5 камней, во второй куче – S камней, 1 ≤ S ≤ 57. Будем говорить, что
игрок имеет выигрышную стратегию, если он может выиграть при любых ходах противника.
Ответьте на следующие вопросы:
Вопрос 1. Известно, что Ваня выиграл своим первым ходом после неудачного первого хода Пети. Назовите
минимальное значение S, при котором это возможно.
Вопрос 2. Найдите два таких значения S, при которых у Пети есть выигрышная стратегия, причём Петя не
может выиграть первым ходом, но может выиграть своим вторым ходом независимо от того, как будет ходить
Ваня. Найденные значения запишите в ответе в порядке возрастания.
Вопрос 3. Укажите минимальное значение S, при котором у Вани есть выигрышная стратегия, позволяющая
ему выиграть первым или вторым ходом при любой игре Пети, и при этом у Вани нет стратегии, которая
позволит ему гарантированно выиграть первым ходом
"""
# # TODO: Ответ —
# #  1) 15
# #  2) 26 28
# #  3) 25
# @lru_cache(None)
# def game(a, b):
#     if a + b >= 63:
#         return 0
#     tmp = [game(a + 1, b), game(a, b + 1),
#            game(a * 2, b), game(a, b * 2)]
#     ng = [i for i in tmp if i <= 0]
#     return -max(ng) + 1 if ng else -max(tmp)
#
#
# print(*[s for s in range(1, 58) if game(5, s) == 2])
# print(min(s for s in range(1, 58) if game(5, s) == -2))


"""
22 (А. Кожевникова) В файле 22-5.xls содержится информация о вычислительных процессов проектов P1 и P2,
которые могут выполняться параллельно или последовательно. Будем говорить, что процесс B зависит от
процесса A, если для выполнения процесса B необходимы результаты выполнения процесса A. В этом случае
процессы могут выполняться только последовательно. Информация о процессах представлена в файле в виде
таблицы. В первом столбце таблицы указан идентификатор процесса (ID), во втором столбце таблицы – время
его выполнения в миллисекундах, в третьем столбце перечислены с разделителем «;» ID процессов, от которых
зависит данный процесс. Если процесс является независимым, то в таблице указано значение 0.
Типовой пример организации данных в файле:
В данном случае независимые процессы 1 и 2 могут выполняться
параллельно, при этом процесс 1 завершится через 4 мс, а процесс 2 – через 3 мс с момента старта. Процесс 3
может начаться только после завершения обоих процессов 1 и 2, то есть, через 4 мс после старта. Он длится 1
мс и закончится через 4 + 1 = 5 мс после старта. Выполнение процесса 4 может начаться только после
завершения процесса 3, то есть, через 5 мс. Он длится 7 мс, так что минимальное время завершения всех
процессов равно 5 + 7 = 12 мс.
Найдите минимальное время завершения процесса 4 из проекта P2.
"""
# # TODO: Ответ — 16


"""
23 Исполнитель преобразует число, записанное на экране. У исполнителя есть две команды, которым
присвоены номера:
1. Прибавь 1
2. Припиши 1
Первая команда увеличивает число на экране на 1, вторая приписывает 1 в начало десятичной записи числа.
Программа для исполнителя – это последовательность команд. Например, если в начальный момент на экране
находится число 1, то программа 212 последовательно преобразует его в 11, 12, 112. Сколько существует
различных программ, которые преобразуют исходное число 1 в число 512?
"""
# # TODO: Ответ — 865
# def f(x, end):
#     if x == end:
#         return 1
#     if x > end:
#         return 0
#     return f(x + 1, end) + f(int('1' + str(x)), end)
#
#
# print(f(1, 512))


"""
24 Текстовый файл 24-s2.txt состоит не более чем из 10**6 заглавных латинских букв. Определите символ,
который чаще всего встречается в файле между буквами A и C, так что A стоит слева от него, а C – справа. В
ответе запишите сначала этот символ, а потом сразу (без разделителя) сколько раз он встретился между
буквами A и C. Если таких символов несколько, нужно вывести тот, который стоит раньше в алфавите.
Например, в тексте ABCCAAСZABCADCDD между буквами A и C два раза стоит B, по одному разу – A и D.
Для этого текста ответом будет B2.
"""
# # TODO: Ответ — T72
# with open('data/24-s2.txt') as f:
#     s = f.read()
# comb = re.findall(r"A\wC" ,s)
# print(*sorted(((i[1], comb.count(i)) for i in set(comb)), key=lambda x: (-x[1], x[0]))[0], sep='')

"""
25 Найдите все натуральные числа, N, принадлежащие отрезку [150 000 000; 300 000 000], которые можно
представить в виде N = 2**m * 3**n, где m – чётное число, n – нечётное число. В ответе запишите все найденные
числа в порядке возрастания, а справа от каждого числа – сумму m+n.
"""
# # TODO: Ответ —
# #  181398528 21
# #  201326592 27
# #  229582512 19
# #  254803968 25
# two_pow = [(m, 2**m) for m in range(30) if not m & 1]
# three_pow = [(n, 3**n) for n in range(30) if n & 1]
# res = []
# for m in two_pow:
#     for n in three_pow:
#         N = m[1] * n[1]
#         if 150000000 <= N <= 300000000:
#             res.append((N, m[0] + n[0]))
# [print(*i) for i in sorted(res)]


"""
26 На складе требуется разместить N контейнеров различного размера, каждый из которых имеет форму куба.
Чтобы сэкономить место, контейнеры вкладывают друг в друга. Один контейнер можно вложить в другой,
если размер стороны внешнего контейнера превышает размер стороны внутреннего на K и более условных
единиц. Группу вложенных друг в друга контейнеров называют блоком. Количество контейнеров в блоке
может быть любым. Каждый блок, независимо от количества и размера входящих в него контейнеров, а также
каждый одиночный контейнер, не входящий в блоки, занимает при хранении одну складскую ячейку.
Определите минимальное количество ячеек, которые потребуются для хранения всех контейнеров, и
максимальное количество контейнеров в одном блоке.
Входные данные представлены в файле 26-101.txt следующим образом. В первой строке входного файла
записано число N – количество контейнеров (натуральное число, не превышающее 20 000) и число K (1 ≤ K ≤
1000) – наименьшая допустимая разница размеров вложенных соседних контейнеров. Каждая из следующих N
строк содержит одно натуральное число, не превышающее 10000 – длину стороны очередного контейнера.
Пример входного файла::
7 9
2
18
47
16
38
55
48
Для таких контейнеров можно составить три блока, удовлетворяющих условию: (55, 38, 18, 2), (48, 16) и (47).
Наибольшее количество контейнеров – в первом блоке – 4. Ответ: 3 4.
"""
# # TODO: Ответ — 19 1045
# with open('data/26-101.txt') as f:
#     n, k = map(int, f.readline().split())
#     data = list(map(int, f.readlines()))
# data.sort(reverse=True)
# res = []
# for elem in data:
#     add = False
#     for view in res:
#        if view[-1] - elem >= k:
#            view.append(elem)
#            add = True
#            break
#     if not add:
#         res.append([elem])
# print(len(res), max(len(i) for i in res))


"""
27 На вход программе подается последовательность целых чисел. Рассматриваются все непрерывные
подпоследовательности исходной последовательности, сумма элементов которых кратна K. Программа должна
вывести одно число – количество таких подпоследовательностей. Гарантируется, что в последовательности
такая подпоследовательность есть.
Входные данные. Даны два входных файла (файл A и файл B), содержит в первой строке натуральное число N
– количество чисел в последовательности (100 ≤ N ≤ 5000000) и натуральное число K. В каждой из следующих
N строк записано одно целое число, не превышающее по модулю 10000.
Пример входного файла:
7 11
11
15
8
14
22
24
10
В этом наборе есть 4 подпоследовательности, сумма элементов которых кратна 11: (11), (8, 14), (8, 14, 22) и (22).
Ответ: 4.
В ответе укажите два числа: сначала искомое значение для файла А, затем для файла B.
"""
# # TODO: Ответ — 614
def solution(n, k, data):
    pref = [0]
    for i in data:
        pref += [pref[-1] + i]
    res = []
    for i in range(n):
        for j in range(i+1, n):
            summ = (pref[j]-pref[i])
            if summ % k == 0:
                res.append(summ)
    return len(res)

with open('data/27-97t.txt') as f:
    n, k = map(int, f.readline().split())
    data = list(map(int, f.readlines()))
print(solution(n, k, data))

with open('data/27-97a.txt') as f:
    n, k = map(int, f.readline().split())
    data = list(map(int, f.readlines()))
print(solution(n, k, data))

with open('data/27-97b.txt') as f:
    n, k = map(int, f.readline().split())
    data = list(map(int, f.readlines()))
print(solution(n, k, data))
