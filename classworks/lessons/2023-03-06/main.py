from itertools import product, permutations
from math import ceil
'''
1 На рисунке справа схема дорог Н-ского района изображена в виде графа, в таблице
содержатся сведения о длинах этих дорог (в километрах).
Так как таблицу и схему
рисовали независимо друг от друга, то нумерация населённых пунктов в таблице никак не
связана с буквенными обозначениями на графе. Определите длину кратчайшего пути из
пункта В в пункт Е.
'''
### TODO: Ответ – 30

'''
2 (И. Женецкий) Логическая функция F задаётся выражением (y → z) ∧ ¬(z ∧ x). На
рисунке приведён частично заполненный фрагмент таблицы истинности функции F,
содержащий неповторяющиеся строки. Определите, какому столбцу таблицы истинности
функции F соответствует каждая из переменных x, y, z.
В ответе напишите буквы x, y, z в том порядке, в котором
идут соответствующие им столбцы. Буквы в ответе пишите подряд, никаких разделителей
между буквами ставить не нужно.
'''
### TODO: Ответ – zxy
print('z x y f')
for x, y, z in product([0, 1], repeat=3):
    f = int((not y or z) and not (z and x))
    if f:
        print(z, x, y, f)

'''
3 (А. Кабанов) В файле 3-5.xls приведён фрагмент базы фрагмент базы данных «Аудиотека».
База данных состоит из четырёх таблиц. Таблица «Альбомы» содержит записи о
записанных альбомах, а также информацию о исполнителях. Таблица «Артисты» содержит
записи о названии исполнителей. Таблица «Треки» содержит записи о записанных
композициях, а также информацию о альбомах и жанрах. Поле Длительность содержит
длительность аудиозаписи в миллисекундах, поле Размер содержит размер аудиозаписи в
байтах, а поле Стоимость содержит стоимость аудиозаписи в рублях. Таблица «Жанры»
содержит данные о названии жанров. На рисунке приведена схема указанной базы данных.
Используя информацию из
приведённой базы данных, найдите исполнителя в жанре Metal с наименьшим суммарным
размером песен в этом жанре. В ответе укажите целую часть размера его песен в
Мегабайтах
'''
### TODO: Ответ – 10


'''
4 Для кодирования некоторой последовательности, состоящей из букв А, Б, В, Г, Д, Е, Ж, З,
И, Й. решили использовать неравномерный двоичный код, удовлетворяющий условию
Фано. Для букв А, Б, В, Г, Д, Е, Ж, З, И использовали соответственно кодовые слова 1101,
111, 0101, 0110, 1001, 1011, 0100, 1010, 1000. Укажите кратчайшее возможное кодовое слово
для буквы Й, при котором код будет допускать однозначное декодирование. Если таких
кодов несколько, укажите код с наименьшим числовым значением.
'''
### TODO: Ответ – 0000


'''
5 Автомат получает на вход трёхзначное число. По этому числу строится новое число по
следующим правилам.
1. Из цифр, образующих десятичную запись N, строятся наибольшее и наименьшее
возможные двузначные числа (числа не могут начинаться с нуля).
2. На экран выводится разность полученных двузначных чисел.
Пример. Дано число N = 351. Наибольшее двузначное число из заданных цифр – 53,
наименьшее – 13. На экран выводится разность 53 – 13 = 40.
Чему равно наибольшее возможное трёхзначное число N, в результате обработки которого
на экране автомата появится число 14?
'''
### TODO: Ответ – 540
##for n in product('0123456789', repeat=3):
##    if n[0] == '0':
##        continue
##    mn, mx = 10**10, 0
##    for p in set(permutations(n, r=2)):
##        if p[0] == '0':
##            continue
##        mn = min(mn, int(''.join(p)))
##        mx = max(mx, int(''.join(p)))
##    r = mx - mn
##    if r == 14:
##        print(''.join(n))
    

'''
6 (А. Носкин). Исполнитель Черепаха действует на плоскости с декартовой системой
координат. В начальный момент Черепаха находится в начале координат, её голова
направлена вдоль положительного направления оси ординат, хвост опущен. При опущенном
хвосте Черепаха оставляет на поле след в виде линии. В каждый конкретный момент
известно положение исполнителя и направление его движения. У исполнителя существует
две команды: Вперёд n (где n – целое число), вызывающая передвижение Черепахи на n
единиц в том направлении, куда указывает её голова, и Направо m (где m – целое число),
вызывающая изменение направления движения на m градусов по часовой стрелке. Запись
Повтори k [Команда1 Команда2 … КомандаS]
означает, что последовательность из S команд повторится k раз. Черепахе был дан для
исполнения следующий алгоритм:
Вперёд 200
Повтори 4 [Направо 90 Вперёд 100]
В результате Черепаха нарисовала линию. Определите, сколько точек с целочисленными
координатами будут находиться внутри области, ограниченной этой линией, и на самой
линии.
'''
### TODO: Ответ – 10301 (101*101+100)


'''
7 Музыкальный фрагмент был оцифрован и записан в виде файла без использования сжатия
данных. Получившийся файл был передан в город А по каналу связи за 15 секунд. Затем тот
же музыкальный фрагмент был оцифрован повторно с разрешением в 2 раза выше и
частотой дискретизации в 1,5 раза меньше, чем в первый раз. Сжатие данных не
производилось. Полученный файл был передан в город Б; пропускная способность канала
связи с городом Б в 2 раза выше, чем канала связи с городом А. Сколько секунд длилась
передача файла в город Б? В ответе запишите только целое число, единицу измерения
писать не нужно.
'''
### TODO: Ответ – 10
##print(2*(1/1.5)*(1/2)*15)


'''
8 (А. Куканова) Леся составляет слова, содержащие ровно 3 буквы М, из букв Ч, О, А, Н, И,
М, Е. Слово может иметь длину от 4 до 6 букв. Сколько слов может составить Леся?
'''
### TODO: Ответ – 4704
##c = 0
##for i in range(4, 7):
##    for s in product('ЧОАНИМЕ', repeat=i):
##        if s.count('М')  == 3:
##            c += 1
##print(c)


'''
9 (Е. Джобс) На темной-темной улице живут злостные неплательщики. В файле 9-j6.xls в
таблице указано, какой баланс на счете имеют хозяева определенной квартиры вопределенном доме. В первой строке перечислены номера домов, в левом столбце – номера
квартир. Определите дом, сумма задолженностей в котором самая большая. Запишите в
ответе средний показатель задолженности для этого дома (среди должников). При
получении нецелого значения нужно взять только целую часть числа.
Примечание: Положительный баланс на счету отдельных хозяев не уменьшает сумму
задолженности дома. Средняя сумма задолженности определяется среди должников.
'''
### TODO: Ответ – 5584


'''
10 (Е. Джобс) В файле 10-212.docx приведен текст романа Л.Н.Толстого «Анна Каренина».
Определите, сколько раз встречается в тексте отдельное слово «уж». Регистр написания не
учитывать.
'''
### TODO: Ответ – 164


'''
11 При регистрации в компьютерной системе каждому пользователю присваивается
идентификатор фиксированной длины, состоящий из двух частей. Первая часть включает 12
заглавных латинских букв; каждый символ кодируется отдельно с использованием
минимально возможного количества битов. Вторая часть – целое число от 0001 до 5000, для
его кодирования используется минимальное число бит. Для кодирование полного
идентификатора выделяется целое число байтов. Кроме того, для каждого пользователя
хранятся дополнительные сведения (также целое число байтов, одинаковое для каждого
пользователя). Определите, сколько байтов занимают дополнительные сведения, если для
данные о 60 пользователях занимают 1020 байтов.
'''
### TODO: Ответ – 7
##print((1020//60) - ceil((12*5+13)/8))


'''
12 Исполнитель Редактор получает на вход строку цифр и преобразовывает её. Редактор
может выполнять две команды, в обеих командах v и w обозначают цепочки символов.
1. заменить (v, w)
2. нашлось (v)
Первая команда заменяет в строке первое слева вхождение цепочки v на цепочку w. Если
цепочки v в строке нет, эта команда не изменяет строку. Вторая команда проверяет,
встречается ли цепочка v в строке исполнителя Редактор.
Дана программа для исполнителя Редактор:
НАЧАЛО
ПОКА нашлось (333) ИЛИ нашлось (555)
ЕСЛИ нашлось (555)
ТО заменить (555, 3)
ИНАЧЕ заменить (333, 5)
КОНЕЦ ЕСЛИ
КОНЕЦ ПОКА
КОНЕЦ
Какая строка получится в результате применения приведённой выше программы к строке,
состоящей из 65 идущих подряд цифр 5? В ответе запишите полученную строку.
'''
### TODO: Ответ – 53355
##s = 65 * '5'
##while '333' in s or '555' in s:
##    if '555' in s:
##        s = s.replace('555', '3', 1)
##    else:
##        s = s.replace('333', '5', 1)
##print(s)


'''
13 (Е. Джобс) На рисунке представлена схема дорог, связывающих города А, Б, В, Г, Д, Е, Ж,
З, К. По каждой дороге можно двигаться только в одном направлении, указанном стрелкой.
Сколько существует маршрутов, начинающихся и оканчивающихся в городе Ж и не
проходящих дважды через один и тот же пункт?
'''
### TODO: Ответ – 6


'''
14 В системе счисления с основанием p выполняется равенство
87x6 + x5x8 = y7y92
Буквами x и y обозначены некоторые цифры из алфавита системы счисления с основанием
p. Определите значение числа yxxy
p
и запишите это значение в десятичной системе
счисления.
'''
### TODO: Ответ – 3289
##for p in range(10, 36):
##    for x in '0123456789abcdefghijklmnopqrstuvwxyz'[:p]:
##        for y in '0123456789abcdefghijklmnopqrstuvwxyz'[:p]:
##            if int('87' + x + '6', p) + int(x + '5' + x + '8', p) == int(y + '7' + y + '92', p):
##                print(int(y+x+x+y, p), p)


'''
15 Введём выражение M & K, обозначающее поразрядную конъюнкцию M и K (логическое
«И» между соответствующими битами двоичной записи). Определите наименьшее
натуральное число A, такое что выражение
(X & 13 = 0) → ((X & 40 ≠ 0) → (X & A ≠ 0))
тождественно истинно (то есть принимает значение 1 при любом натуральном значении
переменной X)?
'''
### TODO: Ответ – 32
##for A in range(1, 10000):
##    flag = True
##    for X in range(1, 10000):
##        f = (X & 13 != 0) or ((X & 40 == 0) or (X & A != 0))
##        if not f:
##            flag = False
##            break
##    if flag:
##        print(A)
##        break


'''
16 (А. Богданов) Алгоритм вычисления значения функции F(n), где n – целое
неотрицательное число, задан следующими соотношениями:
F(n) = 0 при n ≤ 2 или n = 8
F(n) = 1 при n = 3
F(n) = F(n–2) + F(n–1) при n > 3 и n ≠ 8
Для какого значения n значение F(n) будет равно 25?
'''
### TODO: Ответ – 13
##def F(n):
##    return 0 if n == 8 or n <= 2 else 1 if n == 3 else F(n-2) + F(n-1)
##
##for n in range(1, 10000):
##    if F(n) == 25:
##        print(n)
##        break


