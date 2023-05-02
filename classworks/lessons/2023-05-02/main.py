from itertools import product
from math import ceil

def to_base(n, b):
    a = [chr(i) for i in range(48, 58)] + [chr(l) for l in range(ord('a'), ord('z') + 1)]
    r = a[n % b]
    while n >= b:
        n //= b
        r += a[n % b]
    return r[::-1]


"""
1 (Е. Джобс) На рисунке справа схема дорог Н-ского района изображена в виде графа, в таблице звёздочками
обозначено наличие дорог.
Так как таблицу и схему рисовали независимо друг от
друга, то нумерация населённых пунктов в таблице никак не связана с буквенными обозначениями на графе.
Определите, какие номера населённых пунктов в таблице могут соответствовать населённым пунктам И и К на
схеме. В ответе запишите эти два номера в возрастающем порядке без разделителей.
"""
### TODO: Ответ — 18


"""
2 Логическая функция F задаётся выражением (x ≡ ¬y) → ((x ∧ w) ≡ z).
На рисунке приведён частично заполненный фрагмент таблицы истинности
функции F, содержащий неповторяющиеся строки. Определите, какому столбцу таблицы истинности функции
F соответствует каждая из переменных x, y, z, w.
"""
### TODO: Ответ — yzxw
##for x, y, z, w in product((0, 1), repeat=4):
##    f = int(not (x == (not y)) or ((x and w) == z))
##    if not f:
##        print(y, z, x, w, f)


"""
3 (Е. Джобс) В файле 3-2.xls приведён фрагмент базы данных «Рейсы» о рейсах самолетов. База данных состоит
из одной таблицы. Таблица «Рейсы» содержит записи о городах отправления и прибытия, и также номер борта,
совершающего рейс. На рисунке приведена схема данных.
Используя информацию из приведённой базы данных, определите сколько рейсов совершил
борт 128 таких, что Москва была одним из концов маршрута - городом отправления или городом прибытия. В
ответе запишите только число.
"""
### TODO: Ответ — 6


"""
4 Все заглавные буквы русского алфавита закодированы неравномерным двоичным кодом, для которого
выполняется условие Фано: никакое кодовое слово не совпадает с началом другого кодового слова. Известно,
что слову ТРОПОТ соответствует код 001110110001001. Какой код соответствует слову ПОРТ?
"""
### TODO: Ответ — 1000111001


"""
5 (В.Н. Шубинкин) На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R
следующим образом:
1) Строится двоичная запись числа N.
2) К этой записи дописывается ещё три или четыре разряда по следующему правилу: если N нечётное, то слева
к нему приписывается "1", а справа - "11". В противном случае слева приписывается "11", а справа "00".
Например, N = 510 = 1012 => 1101112 = 5510 = R
Полученная таким образом запись (в ней на три или четыре разряда больше, чем в записи исходного числа N)
является двоичной записью искомого числа R. Укажите наибольшее число R, меньшее 127, которое может
быть получено с помощью описанного алгоритма. В ответ запишите это число в десятичной системе
счисления.
"""
### TODO: Ответ — 120
##res = []
##for n in range(1, 1000):
##    r = bin(n)[2:]
##    r = '1' + r + '11' if int(r, 2) & 1 else '11' + r + '00'
##    if int(r, 2) < 127:
##        res.append(int(r, 2))
##print(max(res))


"""
6 Исполнитель Черепаха действует на плоскости с декартовой системой координат. В начальный момент
Черепаха находится в начале координат, её голова направлена вдоль положительного направления оси ординат,
хвост опущен. При опущенном хвосте Черепаха оставляет на поле след в виде линии. В каждый конкретный
момент известно положение исполнителя и направление его движения. У исполнителя существует две команды:
Вперёд n (где n – целое число), вызывающая передвижение Черепахи на n единиц в том направлении, куда
указывает её голова, и Направо m (где m – целое число), вызывающая изменение направления движения на m
градусов по часовой стрелке. Запись
Повтори k [Команда1 Команда2 … КомандаS]
означает, что последовательность из S команд повторится k раз. Черепахе был дан для исполнения следующийалгоритм:
Повтори 12 [Вперёд 6 Направо 120]
Определите, сколько точек с целочисленными координатами будут находиться внутри области, ограниченной
линией, заданной данным алгоритмом. Точки на линии учитывать не следует.
"""
### TODO: Ответ — 13
##from turtle import *
##
##m = 40
##screensize(10000, 10000)
##speed(0)
##color('red', 'green')
##left(90)
##begin_fill()
##
##for _ in range(12):
##    forward(6*m)
##    right(120)
##
##end_fill()
##penup()
##for x, y in product(range(-5*m, 15*m, m), repeat=2):
##    goto(x, y)
##    dot(3, 'black')
##mainloop()


"""
7 Для хранения произвольного растрового изображения размером 800x630 пикселей отведено 270 Кбайт
памяти без учёта размера заголовка файла. Для кодирования цвета каждого пикселя используется одинаковое
количество бит, коды пикселей записываются в файл один за другим без промежутков. При сохранении данные
сжимаются, размер итогового файла после сжатия становится на 35% меньше исходного. Какое максимальное
количество цветов можно использовать в изображении?
"""
### TODO: Ответ — 64
##print(2**int((270*(1/0.65)*2**13)/(800*630)))


"""
8 *(Д. Статный) Григорий придумывает 16-буквенные слова, состоящие из букв слова АНТИУТОПИЯ. Сколько
слов, содержащих комбинацию АНТИУТОПИЯ, может составить Григорий, если все гласные, не входящие в
искомую комбинацию, расположены в обратном алфавитном порядке, а согласные – алфавитном порядке, но
их не более 2-х? Буквы в словах могут повторяться любое количество раз или же не встречаться вовсе
"""
### TODO: Ответ — 61446
##vowels = 'АИУОЯ'
##consonants = 'НТП'
##c = 0
##for s in product('*АНТИУОПЯ', repeat=7):
##    if s.count('*') != 1:
##        continue
##    vowel = [i for i in s if i in vowels]
##    consonant = [i for i in s if i in consonants]
##    if vowel == sorted(vowel, reverse=True) and consonant == sorted(consonant) and len(consonant) <= 2:
##        c += 1
##print(c)


"""
9 Откройте файл электронной таблицы 9-0.xls, содержащей вещественные числа – результаты ежечасного
измерения температуры воздуха на протяжении трёх месяцев. Найдите разность между максимальным и
минимальным значениями температуры в мае во второй половине дня (с 12:00). В ответе запишите только
целую часть получившегося числа.
"""
### TODO: Ответ — 13


"""
10 В файле 10-170.docx приведена повесть-феерия А. Грина «Алые паруса». Сколько раз встречается предлог
«из» (с заглавной или строчной буквы) в тексте повести (не считая сносок)? В ответе укажите только число.
"""
### TODO: Ответ — 67


"""
11 (Е. Джобс) При регистрации в компьютерной системе каждому пользователю выдаётся пароль, состоящий
из 9 символов и содержащий только символы из 11 символьного набора: В, У, З, Н, А, Б, Ю, Д, Ж, Е, Т. В базе
данных для хранения сведений о каждом пользователе отведено одинаковое и минимально возможное целое
число байт. При этом используют посимвольное кодирование паролей, все символы кодируют одинаковым и
минимально возможным количеством бит. Кроме собственно пароля, для каждого пользователя в системе
хранятся дополнительные сведения. На хранение дополнительных сведений отведено одинаковое для каждого
пользователя целое количество байт. Для хранения сведений о 23 пользователях потребовалось 713 байт.
Сколько байт выделено для хранения дополнительных данных о пользователе? В ответе запишите только целое
число – количество байт.
"""
### TODO: Ответ — 26
##print(int(713/23)-ceil((4*9)/(2**3)))


"""
12 Исполнитель Редактор получает на вход строку цифр и преобразовывает её. Редактор может выполнять две
команды, в обеих командах v и w обозначают цепочки цифр.
1. заменить (v, w)
2. нашлось (v)
Первая команда заменяет в строке первое слева вхождение цепочки v на цепочку w, вторая проверяет,
встречается ли цепочка v в строке исполнителя Редактор. Если она встречается, то команда возвращает
логическое значение «истина», в противном случае возвращает значение «ложь».
Какая строка получится в результате применения приведённой ниже программы к строке, состоящей из 156
идущих подряд цифр 5? В ответе запишите полученную строку.
НАЧАЛО
ПОКА нашлось (333) ИЛИ нашлось (555)
ЕСЛИ нашлось (555)
ТО заменить (555, 3)
ИНАЧЕ заменить (333, 5)
КОНЕЦ ЕСЛИ
КОНЕЦ ПОКА
КОНЕЦ
"""
### TODO: Ответ — 53
##s = 156 * '5'
##while '333' in s or '555' in s:
##    if '555' in s:
##        s = s.replace('555', '3', 1)
##    else:
##        s = s.replace('333', '5', 1)
##print(s)


"""
13 (Е. Джобс) На рисунке представлена схема дорог, связывающих города А, Б, В, Г, Д, Е, Ж, З, К. По каждой
дороге можно двигаться только в одном направлении, указанном стрелкой. Какова длина самого длинного
маршрута, начинающегося и заканчивающегося в пункте Ж и не проходящих дважды через один и тот же
пункт? Длиной пути считать количество дорог, составляющих этот путь.
"""
### TODO: Ответ — 6


"""
14 Укажите наименьшее основание системы счисления, в которой запись числа 30 трёхзначна.
"""
### TODO: Ответ — 4
for base in range(4, 10):
    if len(to_base(30, base)) == 3:
           print(base)
           break
