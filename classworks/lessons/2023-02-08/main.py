from itertools import product
from math import ceil

'''
1. На рисунке схема дорог Н-ского района изображена в виде графа, в таблице содержатся сведения о
длине этих дорог в километрах.
Так как таблицу и схему рисовали
независимо друг от друга, нумерация населённых пунктов в таблице никак не связана с буквенными
обозначениями на графе. Известно, что длина дороги ЗЕ равна 15 км. Определите длину дороги БГ. В
ответе запишите целое число – длину дороги в километрах.
'''
### TODO: Ответ – 22


'''
2. Логическая функция F задаётся выражением ¬a ∨ (b ∧ ¬c). Определите, какому столбцу таблицы
истинности функции F соответствует каждая из переменных a, b, c.
В ответе напишите буквы a, b, c в том порядке, в котором идут
соответствующие им столбцы (без разделителей).
'''
### TODO: Ответ – cabf
##print('c a b f')
##for c, a, b in product([0, 1], repeat=3):
##    f = int(not a or (b and not c))
##    print(c, a, b, f)


'''
3. (Е. Джобс) В файле 3-1.xls приведён фрагмент базы данных «Рейсы» о движении грузов на базе.
База данных состоит из одной таблицы. Таблица «Рейсы» содержит записи о водителе, объеме
перевезенного груза в килограммах и характере перевозки («привоз» на базу или «вывоз» с базы). На
рисунке приведена схема данных.
Используя информацию из приведённой базы данных, определите на сколько
килограммов отличается суммарное количество вывезенных и привезенных Ивановым грузов. В
ответе запишите только число.
'''
### TODO: Ответ – 11724


'''
4. Для кодирования некоторой последовательности, состоящей из букв А, Б, В, Г и Д, используется
неравномерный двоичный код, позволяющий однозначно декодировать полученную двоичную
последовательность. Вот этот код:
А – 11; Б – 110; В – 101; Г – 000; Д – 010.
Как можно сократить длину кодового слова для буквы В так, чтобы код по-прежнему можно было
декодировать однозначно? Коды остальных букв меняться не должны. Если есть несколько вариантов,
выберите кодовое слово с минимальным значением.
'''
### TODO: Ответ – 01


'''
5. На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R
следующим образом.
1. Строится двоичная запись числа N.
2. К этой записи дописываются справа ещё два разряда по следующему правилу:
а) складываются все цифры двоичной записи, и остаток от деления суммы на 2 дописывается в конец
числа (справа). Например, запись 11100 преобразуется в запись 111001;
б) над этой записью производятся те же действия – справа дописывается остаток от деления суммы
цифр на 2.Полученная таким образом запись (в ней на два разряда больше, чем в записи исходного числа N)
является двоичной записью искомого числа R. Какое наименьшее число, большее 115, может быть
получено в результате работы автомата?
'''
### TODO: Ответ – 01
##for n in range(1, 1000):
##    r = bin(n)[2:]
##    for i in range(2):
##        r += str(sum(map(int, r)) % 2)
##    r = int(r, 2)
##    if r > 115:
##        print(r)
##        break


'''
6. (А.Г. Минак) Определите, при каком наименьшем введённом значении переменной s программа
выведет число, не меньшее, чем 30.
'''
### TODO: Ответ – 28
##for i in range(1000):
##    s = i
##    n = 32
##    while n > s:
##        s = s + 1
##        n = n - 1
##    if n >= 30:
##        print(i)
##        break


'''
7. (И. Женецкий) Каким может быть максимальное количество цветов в палитре, чтобы растровое
изображение размером 5524х8595 пикселей можно было сохранить, используя 52 Мбайт памяти? В
ответе запишите только целое число, единицу измерения писать не нужно.
'''
### TODO: Ответ – 512
##print(2**int((52*2**23)/(5524*8595)))


'''
8. Все 5-буквенные слова, составленные из букв П, О, Р, Т, записаны в алфавитном порядке и
пронумерованы. Вот начало списка:
1. ООООО
2. ООООП
3. ООООР
4. ООООТ
5. ОООПО
...
Какое количество слов находятся между словами ТОПОР и РОПОТ (включая эти слова)?
'''
### TODO: Ответ – 256
##ropot = 0
##topor = 0
##for i, elem in enumerate(product('ОПРТ', repeat=5)):
##    elem = ''.join(elem)
##    if elem == 'ТОПОР':
##        topor = i
##    if elem == 'РОПОТ':
##        ropot = i
##print(topor-ropot+1)


'''
9. (А. Комков) Откройте файл электронной таблицы 9-103.xls, содержащей в каждой строке два целых
числа – координаты точки на плоскости. Найдите наибольшее расстояние точки от начала координат.
В ответе запишите целую часть найденного расстояния.
'''
### TODO: Ответ – 425


'''
10. В файле 10-141.docx приведена книга Н.В. Гоголя «Вечера на хуторе близ Диканьки». Сколько раз
слово «что» (со строчной буквы) встречается в тексте повести «Страшная месть» (не считая сносок)?
Слова с частицами, такие как «что-нибудь», учитывать не нужно. В ответе укажите только число.
'''
### TODO: Ответ – 105 (114-8-1)


'''
11. Для регистрации на сайте необходимо продумать пароль, состоящий из 10 символов. Он должен
содержать хотя бы 3 цифры, а также строчные или заглавные буквы латинского алфавита (алфавит
содержит 26 букв). В базе данных для хранения сведения о каждом пользователе отведено одинаковое
и минимальное возможное целое число байт. При этом используют посимвольное кодирование
паролей, все символы кодируют одинаковым и минимально возможным количеством бит. Кроме
собственного пароля, для каждого пользователя в системе хранятся дополнительные сведения, для
чего выделено целое число байт одинаковое для каждого пользователя. Для хранения сведений о 30
пользователях потребовалось 870 байт. Сколько байт выделено для хранения дополнительных
сведений об одном пользователе. В ответе запишите только целое число – количество байт.
'''
### TODO: Ответ – 21
##print(((870/30)-ceil((6*10)/8)))


'''
12. Исполнитель Редактор получает на вход строку цифр и преобразовывает её. Редактор может
выполнять две команды, в обеих командах v и w обозначают цепочки символов.
1. заменить (v, w)
2. нашлось (v)Первая команда заменяет в строке первое слева вхождение цепочки v на цепочку w. Если цепочки v в
строке нет, эта команда не изменяет строку. Вторая команда проверяет, встречается ли цепочка v в
строке исполнителя Редактор.
Дана программа для исполнителя Редактор:
НАЧАЛО
ПОКА нашлось (2222) ИЛИ нашлось (666)
ЕСЛИ нашлось (2222)
ТО заменить (2222, 6)
ИНАЧЕ заменить (666, 2)
КОНЕЦ ЕСЛИ
КОНЕЦ ПОКА
КОНЕЦ
Какая строка получится в результате применения приведённой выше программы к строке, состоящей
из 79 идущих подряд цифр 2? В ответе запишите полученную строку.
'''
### TODO: Ответ – 2266222
##s = '2' * 79
##while '2222' in s or '666' in s:
##    if '2222' in s:
##        s = s.replace('2222', '6', 1)
##    else:
##        s = s.replace('666', '2', 1)
##print(s)