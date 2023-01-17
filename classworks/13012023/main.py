from itertools import product

'''
2. Логическая функция F задаётся выражением (¬x ∨ z) ∧ (¬x ∨ ¬y ∨ ¬z).
На рисунке приведён фрагмент таблицы истинности функции F,
содержащий все наборы аргументов, при которых функция F ложна. Определите, какому столбцу
таблицы истинности функции F соответствует каждая из переменных x, y, z.
'''
##print('y x z f')
##for y, x, z in product([0, 1], repeat=3):
##    f = int((not x or z) and (not x or not y or not z))
##    if not f:
##        print(y, x, z, f)


'''
5. На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R
следующим образом.
1) Строится двоичная запись числа N.
2) Затем справа дописываются два разряда: символы 01, если число N чётное, и 10, если нечётное.
Полученная таким образом запись (в ней на два разряда больше, чем в записи исходного числа N)
является двоичной записью искомого числа R. Укажите минимальное число N, после обработки
которого автомат получает число, большее 138. В ответе это число запишите в десятичной системе
'''
##for n in range(1, 100):
##    r = int(bin(n)[2:] + '10', 2) if n % 2 else int(bin(n)[2:] + '01', 2)
##    if r > 138:
##        print(n)
##        break


'''
6. (А. Богданов) Исполнитель Черепаха действует на плоскости с декартовой системой координат. В
начальный момент Черепаха находится в начале координат, её голова направлена вдольположительного направления оси ординат, хвост опущен. При опущенном хвосте Черепаха оставляет
на поле след в виде линии. В каждый конкретный момент известно положение исполнителя и
направление его движения. У исполнителя существует две команды: Вперёд n (где n – целое число),
вызывающая передвижение Черепахи на n единиц в том направлении, куда указывает её голова, и
Направо m (где m – целое число), вызывающая изменение направления движения на m градусов по
часовой стрелке. Запись
Повтори k [Команда1 Команда2 … КомандаS]
означает, что последовательность из S команд повторится k раз. Черепахе был дан для исполнения
следующий алгоритм:
Повтори 4 [ Повтори 4 [ Повтори 4
[ Вперед 3 Направо 120 ] Вперед 3 ] Вперед 6 ]
Сколько равносторонних треугольников можно найти на полученной фигуре?
'''
##from turtle import *
##left(90)
##m = 20
##color('black', 'red')
##begin_fill()
##speed(0)
##
##for i in range(4):
##    for j in range(4):
##        for k in range(4):
##            forward(3 * m)
##            right(120)
##        forward(3 * m)
##    forward(6 * m)
##
##mainloop()


'''
8. Сколько слов длины 5, начинающихся с гласной буквы, можно составить из букв Е, Г, Э? Каждая
буква может входить в слово несколько раз. Слова не обязательно должны быть осмысленными
словами русского языка
'''
##c = 0
##for s in product('ЕГЭ', repeat=5):
##    s = ''.join(s)
##    if s[0] in 'ЕЭ':
##        c += 1
##print(c)


'''
12. Исполнитель Редактор получает на вход строку цифр и преобразовывает её. Редактор может
выполнять две команды, в обеих командах v и w обозначают цепочки символов.
1. заменить (v, w)
2. нашлось (v)
Первая команда заменяет в строке первое слева вхождение цепочки v на цепочку w. Если цепочки v в
строке нет, эта команда не изменяет строку. Вторая команда проверяет, встречается ли цепочка v в
строке исполнителя Редактор.
Дана программа для исполнителя Редактор:
НАЧАЛО
ПОКА НЕ нашлось(00)
заменить(01, 21022) 2131310
заменить(02, 310)
заменить(03, 230112) 23213131213131310
КОНЕЦ ПОКА
КОНЕЦ
Известно, что исходная строка начиналась с нуля и заканчивалась нулём, а между ними были только
цифры 1, 2 и 3. После выполнения данной программы получилась строка, содержащая 104 единицы,
39 двоек и 83 тройки. Сколько цифр было в исходной строке?
'''
for i in range(50):
    for j in range(50):
        for k in range(50):
            if 3*i + j + 7*k == 104 and i + 3*k == 39 and 2*i + j + 6*k == 83:
                print(i + j + k + 2)
                break
    