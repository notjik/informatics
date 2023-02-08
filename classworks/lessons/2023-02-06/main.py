from itertools import product

'''
1. На рисунке справа схема дорог Н-ского района изображена в виде графа,
в таблице содержатся сведения о длинах этих дорог (в километрах).
Так как таблицу и схему рисовали независимо друг от друга,
то нумерация населённых пунктов в таблице никак не связана с буквенными
обозначениями на графе. Определите длину кратчайшего пути из пункта В в пункт К.
'''
### TODO: Ответ - 45


'''
2. На рисунке справа схема дорог Н-ского района изображена в виде графа,
в таблице содержатся сведения о длинах этих дорог (в километрах).
Так как таблицу и схему рисовали независимо друг от друга,
то нумерация населённых пунктов в таблице никак не связана
с буквенными обозначениями на графе. Выпишите последовательно,
без пробелов и знаков препинания, указанные на графе буквенные обозначения
пунктов от П1 до П7: сначала букву, соответствующую П1, затем букву,
соответствующую П2, и т. д.
'''
### TODO: Ответ - жвегабд


'''
3. Между населёнными пунктами A, B, C, D, E, F построены дороги,
протяжённость которых приведена в таблице. Отсутствие числа в таблице означает,
что прямой дороги между пунктами нет.
Определите длину кратчайшего пути между пунктами A и F,
не проходящего через пункт C (при условии,
что передвигаться можно только по построенным дорогам).
'''
### TODO: Ответ - 11


'''
4. (Е. Джобс) На рисунке справа схема дорог Н-ского района изображена
в виде графа, в таблице звёздочками обозначено наличие дорог.
Так как таблицу и схему рисовали независимо друг от друга,
то нумерация населённых пунктов в таблице никак не связана
с буквенными обозначениями на графе. Определите номер,
соответствующий населённому пункту В.
'''
### TODO: Ответ - 7


'''
5. (Е. Джобс) На рисунке справа схема дорог Н-ского района изображена
в виде графа, в таблице приведены длины дорог между пунктами.
Так как таблицу и схему рисовали независимо друг от друга,
то нумерация населённых пунктов в таблице никак не связана
с буквенными обозначениями на графе.
Найдите длину кратчайшего маршрута из А в Е, если известно,
что самая длинная дорога из С ведет в Е.
'''
### TODO: Ответ - 25


'''
6. Логическая функция F задаётся выражением (x → y) ∧ (y → z).
На рисунке приведён фрагмент таблицы истинности функции F.
Определите, какому столбцу таблицы истинности функции F соответствует
каждая из переменных x, y, z.
'''
### TODO: Ответ - yxz
##x, y, z, f = 'x', 'y', 'z', 'f'
##s = '{} {} {} {}'.format(y, x, z, f)
##print(s)
##for x, y, z in product([0, 1], repeat=3):
##    f = int((not x or y) and (not y or z))
##    print('{} {} {} {}'.format(y, x, z, f))


'''
7. (Е. Джобс) Логическая функция F задаётся выражением
(a → b) ∧ ¬(b ≡ c) ∧ (d → a). На рисунке приведён частично заполненный
фрагмент таблицы истинности функции F, содержащий неповторяющиеся наборы
аргументов, при которых функция F истинна. Определите, какому столбцу таблицы
истинности функции F соответствует каждая из переменных a, b, c, d.
В ответе напишите буквы a, b, c, d в том порядке, в котором идут
соответствующие им столбцы. Буквы в ответе пишите подряд,
никаких разделителей между буквами ставить не нужно.
'''
### TODO: Ответ - cdab
##a, b, c, d, f = 'a', 'b', 'c', 'd', 'f'
##s = '{} {} {} {} {}'.format(c, d, a, b, f)
##print(s)
##for c, d, a, b in product([0, 1], repeat=4):
##    f = int((not a or b) and (b != c) and (not d or a))
##    if f:
##        print('{} {} {} {} {}'.format(c, d, a, b, f))


'''
8. Логическая функция F задаётся выражением (w → y) ∧ ((x → z) ≡ (y → x)).
На рисунке приведён частично заполненный фрагмент таблицы истинности функции
F, содержащий неповторяющиеся строки. Определите, какому столбцу таблицы
истинности функции F соответствует каждая из переменных x, y, z, w.
'''
### TODO: Ответ - wzyx
##x, y, z, w, f = 'x', 'y', 'z', 'w', 'f'
##s = '{} {} {} {} {}'.format(w, z, y, x, f)
##print(s)
##for x, y, z, w in product([0, 1], repeat=4):
##    f = int((not w or y) and ((not x or z) == (not y or x)))
##    if f:
##        print('{} {} {} {} {}'.format(w, z, y, x, f))


'''
9. Логическая функция F задаётся выражением
((x → z) ∧ (z → w)) ∨ (y ≡ (x ∨ z)).
На рисунке приведён частично заполненный фрагмент таблицы истинности функции F,
содержащий неповторяющиеся строки. Определите, какому столбцу таблицы
истинности функции F соответствует каждая из переменных x, y, z, w.
'''
### TODO: Ответ - yzwx
##x, y, z, w, f = 'x', 'y', 'z', 'w', 'f'
##s = '{} {} {} {} {}'.format(y, z, w, x, f)
##print(s)
##for x, y, z, w in product([0, 1], repeat=4):
##    f = int(((not x or z) and (not z or w)) or (y == (x or z)))
##    if not f:
##        print('{} {} {} {} {}'.format(y, z, w, x, f))


'''
10. (А. Богданов) Миша заполнял таблицу истинности функции
(x → y) ∧ (y → z) ∧ (z → w), но успел заполнить лишь фрагмент из
трёх различных её строк, даже не указав, какому столбцу таблицы
соответствует каждая из переменных. Определите, какому столбцу
таблицы истинности функции F соответствует каждая из переменных x, y, z, w.
В ответе напишите буквы x, y, z, w в том порядке, в котором идут
соответствующие им столбцы. Буквы в ответе пишите подряд, никаких
разделителей между буквами ставить не нужно.
'''
### TODO: Ответ - zywx
##x, y, z, w, f = 'x', 'y', 'z', 'w', 'f'
##s = '{} {} {} {} {}'.format(z, y, w, x, f)
##print(s)
##for x, y, z, w in product([0, 1], repeat=4):
##    f = int((not x or y) and (not y or z) and (not z or w))
##    if f:
##        print('{} {} {} {} {}'.format(z, y, w, x, f))


'''
11. Заглавные буквы русского алфавита закодированы неравномерным двоичным кодом,
в котором никакое кодовое слово не является началом другого кодового слова.
Это условие обеспечивает возможность однозначной расшифровки закодированных
сообщений. Известно, что все кодовые слова содержат не меньше двух двоичных
знаков, а слову ГОЛОД соответствует код 0100001100111.
Какой код соответствует слову ДОГ?
'''
### TODO: Ответ - 11100010


'''
12. Для кодирования некоторой последовательности,
состоящей из букв А, Б, В, Г, Д, Е, Ж, З, И, Й. решили использовать
неравномерный двоичный код, удовлетворяющий условию Фано.
Для букв А, Б, В, Г, Д, Е, Ж, З, И использовали соответственно
кодовые слова 0011, 1011, 1111, 0110, 0001, 1100, 0010, 0111, 0000.
Укажите кратчайшее возможное кодовое слово для буквы Й, при котором код
будет допускать однозначное декодирование. Если таких кодов несколько,
укажите код с наименьшим числовым значением.
'''
### TODO: Ответ - 010


'''
13. По каналу связи передаются сообщения, содержащие только семь букв:
А, Б, К, О, Т, Р, Я . Для передачи используется двоичный код,
удовлетворяющий условию Фано. Кодовые слова для некоторых букв известны:
А – 101, О – 11, Я – 011. Какое наименьшее количество двоичных знаков
потребуется для кодирования слова КАТОК?
'''
### TODO: Ответ - 12


'''
14. По каналу связи передаются сообщения, содержащие только четыре буквы:
А, Б, В, Г; для передачи используется двоичный код,
удовлетворяющий условию Фано. Для букв А и Б используются такие кодовые слова:
А – 0; Б – 1011. Укажите сумму длин кратчайших кодовых слов для букв В и Г,
при котором код будет допускать однозначное декодирование.
'''
### TODO: Ответ - 5


'''
15. (А.Н. Носкин) Для кодирования некоторой последовательности,
состоящей из букв А, Б, В, Г, Д, решили использовать неравномерный двоичный код,
удовлетворяющий условию Фано. Для букв А, Б, В, Г использовали
соответственно кодовые слова 011, 010, 001, 0001. Укажите возможное
кодовое слово для буквы Д, при котором код будет допускать однозначное
декодирование. Если таких кодов несколько, укажите код с наименьшим
числовым значением.
'''
### TODO: Ответ - 0000


'''
16. Автомат обрабатывает натуральное число N > 1 по следующему алгоритму:
1) Строится двоичная запись числа N.
2) В конец записи (справа) дописывается вторая справа цифра двоичной записи.
3) В конец записи (справа) дописывается вторая слева цифра двоичной записи.
4) Результат переводится в десятичную систему.
Пример. Дано число N = 11. Алгоритм работает следующим образом.
1) Двоичная запись числа N: 11 = 10112
2) Вторая справа цифра 1, новая запись 101112.
3) Вторая слева цифра 0, новая запись 1011102.
4) Десятичное значение полученного числа 46.
При каком наибольшем числе N в результате работы алгоритма получится число,
не превышающее 165? В ответе запишите это число в десятичной системе счисления.
'''
### TODO: Ответ - 41
##for n in range(2, 1000):
##    r = bin(n)[2:]
##    r += r[-2]
##    r += r[1]
##    r = int(r, 2)
##    if r <= 165:
##        print(n)


'''
17. На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему
новое число R следующим образом.
1. Строится двоичная запись числа N.
2. К этой записи дописываются справа ещё два разряда по следующему правилу:
а) складываются все цифры двоичной записи, и остаток от деления суммы
на 2 дописывается в конец числа (справа). Например, запись 11100
преобразуется в запись 111001;
б) над этой записью производятся те же действия – справа дописывается остаток
от деления суммы цифр на 2.
Полученная таким образом запись (в ней на два разряда больше,
чем в записи исходного числа N) является двоичной записью искомого числа R.
Укажите такое наименьшее число R, которое превышает 180 и может являться
результатом работы алгоритма. В ответе это число запишите в десятичной системе
счисления.
'''
### TODO: Ответ - 184
##for n in range(1000):
##    r = bin(n)[2:]
##    for i in range(2):
##        r += str(sum(map(int, r)) % 2)
##    r = int(r, 2)
##    if r > 180:
##        print(r)
##        break
    

'''
18. На вход алгоритма подаётся натуральное число N. Алгоритм строит
по нему новое число R следующим образом.
1. Строится двоичная запись числа N.
2. К этой записи дописываются справа ещё два разряда по следующему правилу:
а) складываются все цифры двоичной записи, и остаток от деления суммы
на 2 дописывается в конец числа (справа). Например, запись 11100
преобразуется в запись 111001;
б) над этой записью производятся те же действия – справа дописывается остаток
от деления суммы цифр на 2.
Полученная таким образом запись (в ней на два разряда больше,
чем в записи исходного числа N) является двоичной записью искомого числа R.
Укажите такое наименьшее число R, которое превышает 150 и может являться
результатом работы алгоритма. В ответе это число запишите в десятичной системе
счисления.
'''
### TODO: Ответ - 154
##for n in range(1000):
##    r = bin(n)[2:]
##    for i in range(2):
##        r += str(sum(map(int, r)) % 2)
##    r = int(r, 2)
##    if r > 150:
##        print(r)
##        break


'''
19. (А. Сардарян) На вход алгоритма подаётся два натуральных числа N и M.
Алгоритм строит по ним новое число R следующим образом.
1) Вычисляется число SN как квадрат суммы цифр двоичной записи числа N.
2) Вычисляется число SM как квадрат суммы цифр двоичной записи числа M.
3) Результат R вычисляется как SN – SM.
Укажите минимальную сумму чисел N и M, при которых получается R = 33.
'''
### TODO: Ответ - 142
##res = []
##for n in range(1000):
##    for m in range(1000):
##        r = sum(map(int,bin(n)[2:]))**2 - sum(map(int,bin(m)[2:]))**2
##        if r == 33:
##            res.append(n + m)
##print(min(res))


'''
20. (Досрочный ЕГЭ-2018) На вход алгоритма подаётся натуральное число N.
Алгоритм строит по нему новое число следующим образом.
1) Строится двоичная запись числа N.
2) К этой записи дописываются справа ещё два разряда по следующему правилу:
если N чётное, в конец числа (справа) дописываются два нуля,
в противном случае справа дописываются две единицы.
Например, двоичная запись 1001 числа 9 будет преобразована в 100111.
Полученная таким образом запись
(в ней на два разряда больше, чем в записи исходного числа N)
является двоичной записью числа – результата работы данного алгоритма.
Укажите минимальное число N, для которого результат работы алгоритма будет
больше 115. В ответе это число запишите в десятичной системе счисления.
'''
### TODO: Ответ - 29
for n in range(1000):
    r = bin(n)[2:]
    if not (n % 2):
        r += '00'
    else:
        r += '11'
    r = int(r, 2)
    if r > 115:
        print(n)
        break