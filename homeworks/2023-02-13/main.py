from itertools import product, permutations

'''
1. Для кодирования некоторой последовательности, состоящей из букв А, Б, В, Г, Д, Е, решили
использовать неравномерный двоичный код, допускающий однозначное декодирование. Для букв А,
Б, В, Г использовали соответственно кодовые слова 00, 01, 110, 111. Укажите кратчайшее возможное
кодовое слово для буквы Д, при котором код будет допускать однозначное декодирование. Если таких
кодов несколько, укажите код с наименьшим числовым значением.
'''
# # TODO: Ответ – 10


'''
2. Заглавные буквы русского алфавита закодированы неравномерным двоичным кодом, в котором
никакое кодовое слово не является началом другого кодового слова. Это условие обеспечивает
возможность однозначной расшифровки закодированных сообщений. Известно, что все кодовые
слова содержат не меньше двух и не больше трёх двоичных знаков, а слову МОЛОТ соответствует код
1010010000011. Какой код соответствует слову ТОМ?
'''
# # TODO: Ответ – 01100101


'''
3. По каналу связи передаются сообщения, содержащие только семь букв: А, И, К, Л, Р, Ц, Я. Для
передачи используется двоичный код, удовлетворяющий условию Фано. Кодовые слова для
некоторых букв известны: А – 01, Я – 11. Какое наименьшее количество двоичных знаков потребуется
для кодирования слова КИРИЛЛИЦА?
'''
# # TODO: Ответ – 28 (0000100000110010110110000101)
# l = 'АИКЛРЦЯ'
# s = 'КИРИЛЛИЦА'
# print(*sorted({i: s.count(i) for i in l}.items(), key=lambda x: x[1], reverse=True), sep='\n')
# print(len('0000100000110010110110000101'))


'''
4. Для кодирования некоторой последовательности, состоящей из букв А, Б, В, Г, Д, Е, Ж, З, решили
использовать неравномерный двоичный код, удовлетворяющий условию Фано. Для букв А, Б, В, Г, Д,
Е использовали соответственно кодовые слова 10, 110, 010, 0110, 111, 0111. Укажите кратчайшее
возможное кодовое слово для буквы Ж, при котором код будет допускать однозначное декодирование.
Если таких кодов несколько, укажите код с наименьшим числовым значением.
'''
# # TODO: Ответ – 000


'''
5. (ЕГЭ-2022) По каналу связи передаются сообщения, содержащие только шесть букв: А, И, К, Л, Н,
Т, для передачи используется двоичный код, удовлетворяющий условию Фано. Буквы Л и Н имеют
коды 0 и 11 соответственно. Укажите наименьшую возможную длину закодированной
последовательности для слова КАЛИТКА.
'''
# # TODO: Ответ – 25
# l = 'АИКЛНТ'
# s = 'КАЛИТКА'
# print(*sorted({i: s.count(i) for i in l}.items(), key=lambda x: x[1], reverse=True), sep='\n')
# print(len('1010100010110101111010100'))
# print(len('1001100001010101110011000'))


'''
6. Автомат получает на вход трёхзначное число. По этому числу строится новое число по следующим
правилам.
1. Из цифр, образующих десятичную запись N, строятся наибольшее и наименьшее возможные
двузначные числа (числа не могут начинаться с нуля).
2. На экран выводится разность полученных двузначных чисел.
Пример. Дано число N = 351. Наибольшее двузначное число из заданных цифр – 53, наименьшее – 13.
На экран выводится разность 53 – 13 = 40.
Чему равно наименьшее возможное трёхзначное число N, в результате обработки которого на экране
автомата появится число 63?
'''
# # TODO: Ответ – 309
# for n in product('0123456789', repeat=3):
#     if n[0] == '0':
#         continue
#     n = ''.join(n)
#     gen = [int(''.join(i)) for i in set(permutations(n, r=2)) if i[0] != '0']
#     if max(gen) - min(gen) == 63:
#         print(n)
#         break


'''
7. Автомат обрабатывает натуральное число N > 1 по следующему алгоритму:
1) Строится двоичная запись числа N.
2) В конец записи (справа) дописывается вторая справа цифра двоичной записи.
3) В конец записи (справа) дописывается вторая слева цифра двоичной записи.
4) Результат переводится в десятичную систему.
Пример. Дано число N = 11. Алгоритм работает следующим образом.
1) Двоичная запись числа N: 11 = 10112
2) Вторая справа цифра 1, новая запись 101112.
3) Вторая слева цифра 0, новая запись 1011102.
4) Десятичное значение полученного числа 46.
При каком наименьшем числе N в результате работы алгоритма получится R > 210? В ответе
запишите это число в десятичной системе счисления.
'''
# # TODO: Ответ – 53
# for n in range(2, 1000):
#     r = bin(n)[2:]
#     r += r[-2]
#     r += r[1]
#     r = int(r, 2)
#     if r > 210:
#         print(n)
#         break


'''
8. На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R
следующим образом.
1. Строится двоичная запись числа N.
2. К этой записи дописываются справа ещё два разряда по следующему правилу:
а) складываются все цифры двоичной записи, и остаток от деления суммы на 2 дописывается в конец
числа (справа). Например, запись 11100 преобразуется в запись 111001;
б) над этой записью производятся те же действия – справа дописывается остаток от деления суммы
цифр на 2.
Полученная таким образом запись (в ней на два разряда больше, чем в записи исходного числа N)
является двоичной записью искомого числа R. Укажите такое наименьшее число R, которое
превышает 118 и может являться результатом работы алгоритма. В ответе это число запишите в
десятичной системе счисления.
'''
# # TODO: Ответ – 120
# for n in range(1, 1000):
#     r = bin(n)[2:]
#     for _ in range(2):
#         r += str(sum(map(int, r)) % 2)
#     r = int(r, 2)
#     if r > 118:
#         print(r)
#         break


'''
9. Автомат обрабатывает десятичное натуральное число N по следующему алгоритму:
1) Строится двоичная запись числа N.
2) К полученному числу справа дописывается 0, если в числе единиц больше, чем нулей; иначе
дописывается 1.
3) Из середины двоичного числа убирается 2 разряда, если количество разрядов получилось четным,
и 3 разряда, если нечетное.
4) Результат переводится в десятичную систему.
Пример. Дано число N = 11. Алгоритм работает следующим образом.
1) Двоичная запись числа N: 11 = 10112
2) Единиц больше, чем нулей, новая запись 101102.
3) Длина начётная, удаляем три средних разряда, новая запись 102.
4) Десятичное значение полученного числа 2.
Для скольких различных значений N в результате работы автомата получается число 58?
'''
# # TODO: Ответ – 11
# c = 0
# for n in range(1, 10000):
#     r = bin(n)[2:]
#     r += '0' if r.count('1') > r.count('0') else '1'
#     r = r[:len(r) // 2 - 1] + r[len(r) // 2 + 1:] if not(len(r) % 2) else r[:len(r) // 2 - 1] + r[len(r) // 2 + 2:]
#     if r == '':
#         r = '0'
#     r = int(r, 2)
#     if r == 58:
#         c += 1
# print(c)


'''
10. Автомат обрабатывает натуральное число N по следующему алгоритму:
1. Строится двоичная запись числа N без ведущих нулей.
2. Если в полученной записи единиц больше, чем нулей, то справа приписывается единица. Если
нулей больше или нулей и единиц поровну, справа приписывается ноль.
3. Полученное число переводится в десятичную запись и выводится на экран.
Какое наименьшее число, превышающее 36, может получиться в результате работы автомата?
'''
# # TODO: Ответ – 39
# for n in range(1, 10000):
#     r = bin(n)[2:]
#     r += '1' if r.count('1') > r.count('0') else '0'
#     r = int(r, 2)
#     if r > 36:
#         print(r)
#         break


'''
11. (А.Г. Минак) Определите, при каком наименьшем положительном введённом значении
переменной s программа выведет четырехзначное число.
'''
# # TODO: Ответ – 343
# for i in range(1, 10000):
#     s = i
#     n = 127
#     while s - n > 0:
#         s = s + 15
#         n = n + 20
#     if 1000 <= s <= 9999:
#         print(i)
#         break


'''
12. Определите, при каком наибольшем введенном значении переменной x программа выведет число
724.
'''
# # TODO: Ответ – 377763840
# #  d = (724000 - 4321) / 4  —  Шаги программы для получения необходимого результата
# #  x0 = 378128000 - 2 * d - 4321  — Начальное значения цикла (примерно)
# d = (724000 - 4321) / 4
# x0 = int(378128000 - 2 * d - 4321)
# flag = False
# for i in range(x0 - 1000, x0 + 10000):
#     x = i
#     n = 4321
#     while (x+n)//1000 < 378128:
#         x = x - 2
#         n = n + 4
#     if n//1000 == 724:
#         flag = True
#         print(i)
#     elif flag:
#         break


'''
13. (А. Минак) Исполнитель Черепаха действует на плоскости с декартовой системой координат. В
начальный момент Черепаха находится в начале координат, её голова направлена вдоль
положительного направления оси ординат, хвост опущен. При опущенном хвосте Черепаха оставляет
на поле след в виде линии. В каждый конкретный момент известно положение исполнителя и
направление его движения. У исполнителя существует две команды: Вперёд n (где n – целое число),
вызывающая передвижение Черепахи на n единиц в том направлении, куда указывает её голова, и
Направо m (где m – целое число), вызывающая изменение направления движения на m градусов по
часовой стрелке. Запись
Повтори k [Команда1 Команда2 … КомандаS]
означает, что последовательность из S команд повторится k раз. Черепахе был дан для исполнения
следующий алгоритм:
Направо 30
Повтори 30 [Направо 30 Вперёд 3 Направо 30]
Определите, сколько точек с целочисленными координатами будут находиться внутри области,
ограниченной линией, заданной данным алгоритмом. Точки на линии следует учитывать.
'''
# # TODO: Ответ – 28
# from turtle import *
#
# left(90)
# m = 50
# color('black', 'red')
# begin_fill()
# speed(0)
#
# right(30)
# for i in range(30):
#     right(30)
#     forward(3 * m)
#     right(30)
#
# end_fill()
# penup()
#
# for x in range(-1 * m, 7 * m, m):
#     for y in range(-5 * m, 3 * m, m):
#         goto(x, y)
#         dot(3, 'green')
#
# mainloop()


'''
14. (Е. Джобс) Сколько существует различных значений d, оканчивающихся на 8, при вводе которых
эта приведенная программа выведет число 1247?
'''
# # TODO: Ответ – 3
# c = 0
# for i in range(1, 10000000):
#     d = i
#     S = 5
#     N = 7
#     while S <= 3011:
#         S = S + d
#         N = N + 124
#     if N == 1247 and abs(d) % 10 == 8:
#         c += 1
# print(c)


'''
15. Определите, при каком наименьшем введённом значении переменной s программа выведет число
128.
'''
# # TODO: Ответ – 22
for i in range(1, 10000000):
    s = i
    n = 4
    while s < 37:
        s = s + 3
        n = n * 2
    if n == 128:
        print(i)
        break
