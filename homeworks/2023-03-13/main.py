from itertools import product
from math import ceil
from functools import lru_cache

'''
1 Между населёнными пунктами A, B, C, D, E, F, Z построены дороги с односторонним
движением. В таблице указана протяжённость каждой дороги. Отсутствие числа в таблице
означает, что прямой дороги между пунктами нет. Например, из A в B есть дорога длиной 4
км, а из B в A дороги нет.
Курьеру требуется проехать из A в Z, посетив не менее 6
населённых пунктов. Пункты A и Z при подсчёте учитываются, два раза проходить через
один пункт нельзя. Какова наименьшая возможная длина маршрута курьера? В ответе
запишите натуральное число – длину минимального маршрута.
'''
# # TODO: Ответ – 17


'''
2 Логическая функция F задаётся выражением (x → y) ∧ (y → z).
На рисунке приведён фрагмент таблицы истинности функции
F. Определите, какому столбцу таблицы истинности функции F соответствует каждая из
переменных x, y, z.
'''
# # TODO: Ответ – zxy
# print('z x y f')
# for x, y, z in product([0, 1], repeat=3):
#     f = int((not x or y) and (not y or z))
#     if f:
#         print(z, x, y, f)


'''
3 В файле 3-78.xls приведён фрагмент базы данных «Продукты» о поставках товаров в
магазины районов города. База данных состоит из трёх таблиц. Таблица «Движение
товаров» содержит записи о поставках товаров в магазины в течение первой декады июня
2021 г., а также информацию о проданных товарах. Поле Тип операции содержит значение
Поступление или Продажа, а в соответствующее поле Количество упаковок, шт. занесена
информация о том, сколько упаковок товара поступило в магазин или было продано в
течение дня. Таблица «Товар» содержит информацию об основных характеристиках
каждого товара. Таблица «Магазин» содержит информацию о местонахождении магазинов.
На рисунке приведена схема указанной базы данных.
Используя информацию из приведённой базы
данных, определите на сколько увеличилось количество упаковок кефира всех сортов,
имеющихся в наличии в магазинах Первомайского района, за период с 1 по 5 июня
включительно.
'''
# # TODO: Ответ – 822


'''
4 В сообщении встречается 7 разных букв. При его передаче использован неравномерный
двоичный префиксный код. Известны коды двух букв: 10, 111. Коды остальных пяти букв
имеют одинаковую длину. Какова минимальная суммарная длина всех семи кодовых слов?
'''
# # TODO: Ответ – 20


'''
5 (А. Сардарян) На вход алгоритма подаётся четырёхзначное натуральное число N.
Алгоритм строит по нему новое число R следующим образом.
1) Если число N четное, то цифры этого числа сортируются в порядке убывания, затем
полученное число делится на 2 нацело (остаток отбрасывается). Полученное значение
является числом R.
Пример: N = 1488 => R = 8841//2 = 4420.
2) Если число N нечетное, то цифры этого числа сортируются в порядке возрастания, затем
полученное число умножается на 2. Полученное значение является числом R.
Пример: N = 3807 => R = 378·2 = 756.
Укажите наименьшее число R, которое больше соответствующего исходного числа N на 1.
'''
# # TODO: Ответ – 2105
# for n in product('0123456789', repeat=4):
#     if n[0] == '0':
#         continue
#     n = ''.join(n)
#     if not int(n) % 2:
#         r = int(''.join(sorted(n, reverse=True))) // 2
#     else:
#         r = int(''.join(sorted(n))) * 2
#     if r - int(n) == 1:
#         print(r)
#         break


'''
6 (А. Богданов) Исполнитель Черепаха действует на плоскости с декартовой системой
координат. В начальный момент Черепаха находится в начале координат, её голова
направлена вдоль положительного направления оси ординат, хвост опущен. При опущенном
хвосте Черепаха оставляет на поле след в виде линии. В каждый конкретный момент
известно положение исполнителя и направление его движения. У исполнителя существует
две команды: Вперёд n (где n – целое число), вызывающая передвижение Черепахи на n
единиц в том направлении, куда указывает её голова, и Налево m (где m – целое число),
вызывающая изменение направления движения на m градусов против часовой стрелки.
Запись
Повтори k [Команда1 Команда2 … КомандаS]
означает, что последовательность из S команд повторится k раз. Черепахе был дан для
исполнения следующий алгоритм:
Повтори 5 [
 Повтори 2 [ Вперед 3 Налево 45 Вперед 3 Направо 90 ]
 Направо 180 ]
Найдите минимальную длину линии, которой можно нарисовать эту фигуру.
'''
# # TODO: Ответ – 48
# from turtle import *
#
# res = 0
# color('black', 'red')
# m = 10
# left(90)
# speed(0)
# begin_fill()
#
# for _ in range(4):
#     for __ in range(2):
#         forward(3*m)
#         res += 3
#         left(45)
#         forward(3*m)
#         res += 3
#         right(90)
#     right(180)
#
# print(res)
# mainloop()


'''
7 (А. Кабанов) При кодировании растрового изображения для каждого пикселя используется
палитра из 224 цветов и 256 уровней прозрачности. Коды пикселей записываются в файл
один за другим без промежутков. Какой минимальный объём памяти (в Кбайт) нужно
зарезервировать, чтобы можно было сохранить любое растровое изображение размером
1024 на 768 пикселей?
'''
# # TODO: Ответ – 3072
# print((1024*768*(24+8))/(2**13))


'''
8 (А. Бриккер) Миша составляет пятибуквенные слова из букв К, О, Н, Ф, Е, Т, А. Он
выбирает слова, которые содержат не менее двух гласных, причём между любыми двумя
гласными есть хотя бы одна согласная. Сколько различных слов может составить Миша?
'''
# # TODO: Ответ – 3888
# c = 0
# for s in product('КОНФЕТА', repeat=5):
#     s1 = ''.join('1' if i in 'ОЕА' else '0' for i in s)
#     if s1.count('1') >= 2 and '11' not in s1:
#         c += 1
# print(c)


'''
9 Откройте файл электронной таблицы 9-0.xls, содержащей вещественные числа –
результаты ежечасного измерения температуры воздуха на протяжении трёх месяцев.
Найдите разность между максимальным значением температуры в апреле и её средним
арифметическим значением за тот же период. В ответе запишите только целую часть
получившегося числа.
'''
# # TODO: Ответ – 7


'''
10 В файле 10-141.docx приведена книга Н.В. Гоголя «Вечера на хуторе близ Диканьки».
Сколько раз слово «покой» (во всех формах единственного и множественного числа)
встречается в тексте повести «Страшная месть» (не считая сносок)? Регистр написания
слова не имеет значения. В ответе укажите только число.
'''
# # TODO: Ответ – 2


'''
11 (А. Жуков) При регистрации в компьютерной системе каждому пользователю выдаётся
пароль, состоящий из 10 символов. В качестве символов используют прописные буквы
латинского алфавита, т.е. 26 различных символов. В базе данных для хранения сведений о
каждом пользователе отведено одинаковое и минимально возможное целое число байт. При
этом используют посимвольное кодирование паролей, все символы кодируют одинаковым и
минимально возможным количеством бит. Кроме собственно пароля, для каждого
пользователя в системе хранятся дополнительные сведения, для чего выделено 15 байт на
одного пользователя. В компьютерной системе выделено 4 Кб для хранения сведений о
пользователях. О каком наибольшем количестве пользователей может быть сохранена
информация в системе? В ответе запишите только целое число – количество пользователей.
'''
# # TODO: Ответ – 186
# print((4*2**10)//(ceil((5*10)/8)+15))


'''
12 (А.А. Имаев) Исполнитель Редактор получает на вход строку цифр и преобразовывает её.
Редактор может выполнять две команды, в обеих командах v и w обозначают цепочки
символов.
1. заменить (v, w)
2. нашлось (v)
Первая команда заменяет в строке первое слева вхождение цепочки v на цепочку w. Если
цепочки v в строке нет, эта команда не изменяет строку. Вторая команда проверяет,
встречается ли цепочка v в строке исполнителя Редактор.
Дана программа для исполнителя Редактор:
НАЧАЛО
ПОКА нашлось (12) ИЛИ нашлось (1)
 ЕСЛИ нашлось (12)
 ТО заменить (12, 2221)
 ИНАЧЕ заменить (1,222222)
 КОНЕЦ ЕСЛИ
КОНЕЦ ПОКА
КОНЕЦ
Какая строка получится в результате применения приведённой ниже программы к строке,
состоящей одной единицы и 51 стоящих справа от неё цифр 2? В ответ, запишите, сколько
цифр 2 будет в конечной строке.
'''
# # TODO: Ответ – 159
# s = '1' + 51 * '2'
# while '12' in s or '1' in s:
#     if '12' in s:
#         s = s.replace('12', '2221', 1)
#     else:
#         s = s.replace('1', '222222', 1)
# print(s.count('2'))


'''
13 (Д. Статный) На рисунке – схема дорог, связывающих пункты A, B, C, D, E, F, G, H, I, J,
K, L, M. По каждой из них можно передвигаться только в одном направлении, указанном
стрелкой. Определите количество различных путей ненулевой длины, которые начинаются и
заканчиваются в городе E, не содержат этот город в качестве промежуточного пункта и
проходят через промежуточные города не более одного раза.
'''
# # TODO: Ответ – 16


'''
14 (А. Богданов) Операнды арифметического выражения записаны в системе счисления с
основанием 18:
9009x₁₈ + 2257x₁₈
В записи чисел переменной x обозначена неизвестная цифра из алфавита 18-ричной
системы счисления. Определите наименьшее значение x, при котором значение данного
арифметического выражения кратно 15. Для найденного значения x вычислите частное от
деления значения арифметического выражения на 15 и укажите его в ответе в десятичной
системе счисления. Основание системы счисления в ответе указывать не нужно.
'''
# # TODO: Ответ – 77888
# for x in range(18):
#     exp1 = 9 * 18 ** 4 + 0 * 18 ** 3 + 0 * 18 ** 2 + 9 * 18 ** 1 + x * 18 ** 0
#     exp2 = 2 * 18 ** 4 + 2 * 18 ** 3 + 5 * 18 ** 2 + 7 * 18 ** 1 + x * 18 ** 0
#     full_exp = exp1 + exp2
#     if not full_exp % 15:
#         print(full_exp // 15)
#         break


'''
15 На числовой прямой даны два отрезка: P = [5, 20] и Q = [25, 38]. Найдите наибольшую
возможную длину отрезка A, при котором формула
( (x &in; А) → (x &in; P) ) ∨ (x &in; Q)
тождественно истинна, то есть принимает значение 1 при любых x.
'''
# # TODO: Ответ – 15


'''
16 Алгоритм вычисления значения функции F(n), где n – целое неотрицательное число,
задан следующими соотношениями:
F(0) = 1
F(n) = 1 + F(n - 1), если n > 0 и n нечётное
F(n) = F(n / 2) в остальных случаях
Определите количество значений n на отрезке [1, 500 000 000], для которых F(n) = 4.
'''
# # TODO: Ответ – 3654
##a = set()
##def f(s):
##    if int(s, 2) > 500000000:
##        return None
##    if s.count('1') == 3:
##        a.add(s)
##        f(s + '0')
##    else:
##        f(s + '1')
##        f(s + '0')
##
##f('1')
##print(len(a))



'''
17 В файле 17-243.txt содержится последовательность целых чисел. Элементы
последовательности могут принимать целые значения от 0 до 10 000 включительно.
Определите количество пар чисел, в которых ровно один из двух элементов больше, чем
сумма цифр всех чисел в файле, делящихся на 61, а десятичная запись другого оканчивается
на 33. В ответе запишите два числа: сначала количество найденных пар, а затем –
минимальную сумму элементов таких пар. В данной задаче под парой подразумевается два
идущих подряд элемента последовательности.
'''
# # TODO: Ответ – 41 5182
##with open('data/17-243.txt') as f:
##    data = list(map(int, f.readlines()))
##summ61 = sum(sum(map(int, str(i))) for i in data if not i % 61)
##c = 0
##mn = 20000
##for i in range(len(data) - 1):
##    accept = 0
##    accept += 1 if data[i] > summ61 else 0
##    accept += 1 if data[i+1] > summ61 else 0
##    accept1 = 0
##    accept1 += 1 if data[i] > summ61 and data[i+1] % 100 == 33 else 0
##    accept1 += 1 if data[i+1] > summ61 and data[i] % 100 == 33 else 0
##    if accept == 1 and accept1 == 1:
##        c += 1
##        mn = min(mn, sum(data[i:i+2]))
##print(c, mn)


'''
18 Квадрат разлинован на N×N клеток (1 < N < 30). Исполнитель Робот может перемещаться
по клеткам, выполняя за одно перемещение одну из двух команд: влево или вниз. По
команде влево Робот перемещается в соседнюю левую клетку, по команде вниз – в
соседнюю нижнюю. Квадрат ограничен внешними стенами. В начальный момент запас
энергии робота равен числу, записанному в стартовой клетке. После каждого шага робота
запас энергии изменяется по следующим правилам: если число в очередной клетке больше
или равно предыдущему, запас увеличивается на величину этого числа, если меньше –
уменьшается на эту же величину. Определите максимальный и минимальный запас энергии,
который может быть у робота после перехода из правой верхней клетки поля в левую
нижнюю. В ответе запишите два числа: сначала максимально возможное значение, затем
минимальное.
Исходные данные для Робота записаны в файле 18-123.xls в виде прямоугольной таблицы,
каждая ячейка которой соответствует клетке квадрата.
'''
# # TODO: Ответ – 517 103



