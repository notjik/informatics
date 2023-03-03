from itertools import product, permutations
from math import ceil
from functools import lru_cache


def to_base(n, b):
    a = '0123456789abcdefghijklmnopqrstuvwxyz'
    r = a[n % b]
    while n >= b:
        n //= b
        r += a[n % b]
    return r[::-1]

'''
1. На рисунке справа схема дорог Н-ского района изображена в виде графа, в таблице содержатся
сведения о длинах этих дорог (в километрах).
Так как таблицу и схему рисовали
независимо друг от друга, то нумерация населённых пунктов в таблице никак не связана с
буквенными обозначениями на графе. Известно, что длина кратчайшего пути из пункта A в пункт Ж
превышает 30 километров. Определите длину кратчайшего пути между пунктами В и Е.
'''
### TODO: Ответ – 26


'''
2. (Е. Джобс) Логическая функция F задаётся выражением ¬w ∧ (y ∨ z → ¬x ∧ y).
На рисунке приведён частично заполненный фрагмент
таблицы истинности функции F, содержащий неповторяющиеся строки. Определите, какому столбцу
таблицы истинности функции F соответствует каждая из переменных x, y, z, w.
'''
### TODO: Ответ – wzyx
##print('w z y x f')
##for w, z, y, x in product([0, 1], repeat=4):
##    f = int(not w and (not (y or z) or (not x and y)))
##    if f:
##        print(w, z, y, x, f)


'''
3. (ЕГЭ-2022) В файле 3-0.xls приведён фрагмент базы данных «Продукты» о поставках товаров в
магазины районов города. База данных состоит из трёх таблиц. Таблица «Движение товаров»
содержит записи о поставках товаров в магазины в течение первой декады июня 2021 г., а также
информацию о проданных товарах. Поле Тип операции содержит значение Поступление или
Продажа, а в соответствующее поле Количество упаковок, шт. занесена информация о том, сколько
упаковок товара поступило в магазин или было продано в течение дня. Таблица «Товар» содержит
информацию об основных характеристиках каждого товара. Таблица «Магазин» содержит
информацию о местонахождении магазинов. На рисунке приведена схема указанной базы данных.
Используя информацию из приведённой базы
данных, определите, на сколько увеличилось количество упаковок всех видов молока, имеющихся в
наличии в магазинах Заречного района, за период с 5 по 8 июня включительно.
'''
### TODO: Ответ – 1871


'''
4. По каналу связи передаются сообщения, содержащие только семь букв: А, Б, В, Г, Д, Е и Ж. Для
передачи используется двоичный код, удовлетворяющий условию Фано. Для буквы А используется
кодовое слово 10; для буквы Б используется кодовое слово 011. Какова минимальная общая длина
кодовых слов для всех семи букв?
'''
### TODO: Ответ – 20
##print(len('10 011 000 001 010 110 111'.replace(' ', '')))


'''
5. На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R
следующим образом.
1. Строится двоичная запись числа N.
2. К этой записи дописываются справа ещё два разряда по следующему правилу:
а) складываются все цифры двоичной записи, и остаток от деления суммы на 2 дописывается в конец
числа (справа). Например, запись 11100 преобразуется в запись 111001;
б) над этой записью производятся те же действия – справа дописывается остаток от деления суммы
цифр на 2.Полученная таким образом запись (в ней на два разряда больше, чем в записи исходного числа N)
является двоичной записью искомого числа R. Сколько различных чисел, меньших 100, могут
появиться на экране в результате работы автомата?
'''
### TODO: Ответ – 24
##c = 0
##for n in range(1, 100000):
##    r = bin(n)[2:]
##    for i in range(2):
##        r += str(sum(map(int, r)) % 2)
##    r = int(r, 2)
##    if r < 100:
##        c += 1
##print(c)


'''
6. (А. Богданов) Исполнитель Черепаха действует на плоскости с декартовой системой координат. В
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
Повтори 5 [ Повтори 3 [ Вперед 2 Направо 270] Вперед 4]
Найдите минимальную площадь выпуклого многоугольника, включающего фигуру
'''
### TODO: Ответ – 36
##from turtle import *
##
##left(90)
##m = 20
##color('black', 'red')
##begin_fill()
##speed(1)
##
##for _ in range(5):
##    for __ in range(3):
##        forward(2*m)
##        right(270)
##    forward(4*m)
##
##end_fill()
##penup()
##for x in range(-10*m, 10*m, m):
##    for y in range(-10*m, 10*m, m):
##        goto(x, y)
##        dot(3, 'green')
##mainloop()

'''
7. Автоматическая фотокамера каждые 6 с создаёт черно-белое растровое изображение, содержащее
256 оттенков. Размер изображения – 128×256 пикселей. Все полученные изображения и коды
пикселей внутри одного изображения записываются подряд, никакая дополнительная информация не
сохраняется, данные не сжимаются. Сколько Мбайтов нужно выделить для хранения всех
изображений, полученных за сутки?
'''
### TODO: Ответ – 450
##print(ceil((((24*60*60)//6)*(8*(128*256)))/(2**23)))


'''
8. Петя составляет шестибуквенные слова перестановкой букв слова АДЖИКА. При этом он избегает
слов с двумя подряд одинаковыми буквами. Сколько всего различных слов может составить Петя?
'''
### TODO: Ответ – 240
##c = 0
##for s in set(permutations('АДЖИКА')):
##    s = ''.join(s)
##    if 'АА' not in s:
##        c += 1
##print(c)


'''
9. (Е. Джобс) Ямой называется такая ячейка электронной таблицы, значение которой меньше любого
из значений соседних ячеек слева, справа, сверху и снизу. Глубиной ямы назовем разницу между
наименьшим значением соседних клеток и значением ячейки с «ямой». В диапазоне D6:L21
определите глубину самой глубокой ямы и количество ям с максимальной глубиной в электронной
таблице, хранящейся в файле 9-j8.xls. В ответе сначала укажите максимальную глубину, затем
найденное количество.
'''
### TODO: Ответ – 15 3


'''
10. В файле 10-141.docx приведена книга Н.В. Гоголя «Вечера на хуторе близ Диканьки». Сколько раз
союз «Но» (с заглавной буквы) встречается в тексте повести «Страшная месть» (не считая сносок)? В
ответе укажите только число.
'''
### TODO: Ответ – 34


'''
11. Каждый сотрудник предприятия получает электронный пропуск, на котором записаны личный код,
состоящий из двух частей. Первая часть кода содержит 10 символов, каждый из которых может быть
одной из 26 заглавных латинских букв. Вторая часть кода содержит 5 символов, каждый из которых
может быть одной из десятичных цифр. При этом в базе данных сервера формируется запись,
содержащая этот код и дополнительную информацию о пользователе. Для представления кода
используют посимвольное кодирование, все символы в пределах одной части кода кодируют
одинаковым минимально возможным для этой части количеством битов, а для кода в целом
выделяется минимально возможное целое количество байтов. Для хранения данных о 40
пользователях потребовалось 1800 байт. Сколько байтов выделено для хранения дополнительной
информации об одном пользователе? В ответе запишите только целое число – количество байтов.
'''
### TODO: Ответ – 36
##print((1800//40) - ceil((5*10+5*4)/8))


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
ПОКА нашлось (10) ИЛИ нашлось (1)
ЕСЛИ нашлось (10)
ТО заменить (10, 001)ИНАЧЕ заменить (1, 00)
КОНЕЦ ЕСЛИ
КОНЕЦ ПОКА
КОНЕЦ
Какая строка получится в результате применения приведённой ниже программы к строке, состоящей
из одной единицы и 75 стоящих справа от нее нулей? В ответе запишите, сколько нулей будет в
конечной строке.
'''
### TODO: Ответ – 152
##s = '1' + '0' * 75
##while '10' in s or '1' in s:
##    if '10' in s:
##        s = s.replace('10', '001', 1)
##    else:
##        s = s.replace('1', '00', 1)
##print(s.count('0'))


'''
13. На рисунке представлена схема дорог, связывающих города А, Б, В, Г, Д, Е, Ж, З, И, К, Л, М. По
каждой дороге можно двигаться только в одном направлении, указанном стрелкой. Сколько
существует различных путей из города А в город М, проходящих через город В?
'''
### TODO: Ответ – 24


'''
14. (В. Шелудько) Значение выражения 7103 + 6∙7104 – 3∙757 + 98 записали в системе счисления с
основанием 7. Сколько цифр 6 содержится в этой записи?
'''
### TODO: Ответ – 46
##print(to_base(7**103 + 6*7**104 - 3*7**57 + 98, 7).count('6'))


'''
15. Введём выражение M & K, обозначающее поразрядную конъюнкцию M и K (логическое «И»
между соответствующими битами двоичной записи). Определите наименьшее натуральное число A,
такое что выражение
(X & 87 = 0) → ((X & 31 ≠ 0) → (X & A ≠ 0))
тождественно истинно (то есть принимает значение 1 при любом натуральном значении переменной
X)?
'''
### TODO: Ответ – 8
##for a in range(1, 100000):
##    flag = True
##    for x in range(1, 100000):
##        f = not (x & 87 == 0) or (not (x & 31 != 0) or (x & a != 0))
##        if not f:
##            flag = False
##            break
##    if flag:
##        print(a)
##        break


'''
16. (Е. Джобс) Алгоритм вычисления значения функции F(n), где n – натуральное число, задан
следующими соотношениями:
F(n) = 1 при n = 0
F(n) = 2·F(1-n) + 3·F(n-1) + 2, если n > 0,
F(n) = - F(-n), если n < 0.
Чему равна сумма цифр значения F(50)?
'''
### TODO: Ответ – 6
##@lru_cache(None)
##def F(n):
##    if n == 0:
##        return 1
##    return 2*F(1-n) + 3*F(n-1) + 2 if n > 0 else -F(-n)
##
##print(sum(map(int, str(F(50)))))


'''
17. (В. Шубинкин) В файле 17-2.txt содержится последовательность целых чисел. Элементы
последовательности могут принимать целые значения от -10 000 до 10 000 включительно. Определите
и запишите в ответе сначала количество элементов последовательности, которые равны её
наименьшему элементу, затем позицию последнего такого элемента в последовательности при
подсчёте с единицы. Например, в последовательности 7; -12; 10; 4; 7; -12; 10; -12; 3 три элемента
равны минимальному, позиция последнего из них - 8. Ответом для данного примера будет пара чисел
3 и 8.
'''
### TODO: Ответ – 3 7783
##with open('data/17-2.txt') as f:
##    data = list(map(int, f.readlines()))
##mn = min(data)
##c = 0
##pos = -1
##for i, elem in enumerate(data):
##    if elem == mn:
##        c += 1
##        pos = i + 1
##print(c, pos)


'''
18. Дана последовательность вещественных чисел. Из неё необходимо выбрать несколько подряд
идущих чисел так, чтобы каждое следующее число отличалось от предыдущего не более чем на 2.
Какую максимальную сумму могут иметь выбранные числа? В ответе запишите только целую часть
максимально возможной суммы.
Исходные данные записаны в виде столбца электронной таблицы в файле 18-77.xls
'''
### TODO: Ответ – 58


'''
19. Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежат две кучи камней.
Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может добавить в одну из куч
один камень или увеличить количество камней в куче в два раза. Чтобы делать ходы, у каждого
игрока есть неограниченное количество камней. Игра завершается в тот момент, когда суммарное
количество камней в кучах становится не менее 75. Победителем считается игрок, сделавший
последний ход, т. е. первым получивший позицию, в которой в кучах будет 75 или больше камней.
В начальный момент в первой куче было 8 камней, во второй куче – S камней, 1 ≤ S ≤ 66. Будем
говорить, что игрок имеет выигрышную стратегию, если он может выиграть при любых ходах
противника.Ответьте на следующие вопросы:
Вопрос 1. Известно, что Ваня выиграл своим первым ходом после неудачного первого хода Пети.
Назовите минимальное значение S, при котором это возможно.
Вопрос 2. Найдите два таких значения S, при которых у Пети есть выигрышная стратегия, причём
Петя не может выиграть первым ходом, но может выиграть своим вторым ходом независимо от того,
как будет ходить Ваня. Найденные значения запишите в ответе в порядке возрастания.
Вопрос 3. Укажите минимальное значение S, при котором у Вани есть выигрышная стратегия,
позволяющая ему выиграть первым или вторым ходом при любой игре Пети, и при этом у Вани нет
стратегии, которая позволит ему гарантированно выиграть первым ходом.
'''
### TODO: Ответ –
###  1: 17
###  2: 29 32
###  3: 28
##@lru_cache(None)
##def game(x, y):
##    if x + y >= 75:
##        return 0
##    tmp = [game(x + 1, y), game(x, y + 1),
##           game(x * 2, y), game(x, y * 2)]
##    negative = [i for i in tmp if i <= 0]
##    if len(negative) != 0:
##        return -max(negative) + 1
##    else:
##        return -max(tmp)
##
##
##print(*[s for s in range(1, 67) if game(8, s) == 2]) # '*' -> раскрывает список
##print(min([s for s in range(1, 67) if game(8, s) == -2]))


'''
20. (В. Шубинкин) В файле 22-3.xls содержится информация о совокупности N вычислительных
процессов, которые могут выполняться параллельно или последовательно. Будем говорить, что
процесс B зависит от процесса A, если для выполнения процесса B необходимы результаты
выполнения процесса A. В этом случае процессы могут выполняться только последовательно.
Информация о процессах представлена в файле в виде таблицы. В первом столбце таблицы указан
идентификатор процесса (ID), во втором столбце таблицы – время его выполнения в миллисекундах, в
третьем столбце перечислены с разделителем «;» ID процессов, от которых зависит данный процесс.
Если процесс является независимым, то в таблице указано значение 0.
Определите минимальное время, через которое завершится выполнение всей совокупности
процессов, при условии, что все независимые друг от друга процессы могут выполняться
параллельно.
Типовой пример организации данных в файле:
В данном случае независимые процессы 1 и 2
могут выполняться параллельно, при этом процесс 1 завершится через 4 мс, а процесс 2 – через 3 мс с
момента старта. Процесс 3 может начаться только после завершения обоих процессов 1 и 2, то есть,
через 4 мс после старта. Он длится 1 мс и закончится через 4 + 1 = 5 мс после старта. Выполнение
процесса 4 может начаться только после завершения процесса 3, то есть, через 5 мс. Он длится 7 мс,
так что минимальное время завершения всех процессов равно 5 + 7 = 12 мс.
'''
### TODO: Ответ – 36


'''
21. Исполнитель Калькулятор преобразует число на экране. У исполнителя есть три команды,
которым присвоены номера:
1. Прибавить 1
2. Прибавить 3
3. Умножить на 2
Программа для исполнителя Калькулятор – это последовательность команд. Сколько существует
программ, для которых при исходном числе 1 результатом является число 13, и при этом траектория
вычислений содержит числа 4 и 9?
'''
### TODO: Ответ – 75
##def calc(start, end):
##    if start > end:
##        return 0
##    if start == end:
##        return 1
##    return calc(start + 1, end) + calc(start + 3, end) + calc(start * 2, end)
##
##print(calc(1, 4) * calc(4, 9) * calc(9, 13))


'''
22. (В. Якшигулов) Текстовый файл 24-178.txt состоит не более чем из 106 символов и содержит
только заглавные буквы латинского алфавита (A..Z). Строка замыкается в кольцо, то есть за
последним символом снова идёт первый. Определите в таком кольце максимальную длину цепочки, в
которой все символы расположены в алфавитном порядке (одинаковые символы могут стоять рядом).
Например, для строки CDEABCABC ответом будет 6 (цепочка ABCCDE).
'''
### TODO: Ответ – 3
##with open('data/24-178.txt') as f:
##    s = f.readline().strip()
##    s *= 2
##mxc = 0
##c = 0
##for i in range(len(s) - 1):
##    if ord(s[i+1]) - ord(s[i]) == 1:
##        c += 1
##    else:
##        c = 0
##    mxc = max(mxc, c)
##print(mxc)


'''
23. Пусть S(N) – сумма трёх наибольших нетривиальных делителей числа N (не считая единицы и
самого числа). Если у числа N меньше трёх таких делителей, то S(N) считается равным 0. Найдите 5
наименьших натуральных чисел, превышающих 10 000 000, для которых в десятичной записи S(N)
все цифры расположены в порядке неубывания. В ответе запишите найденные значения S(N) в
порядке возрастания соответствующих им чисел N.
'''
### TODO: Ответ –
###  2569999
###  467999
###  2444457
###  4457789
###  4446677
##def S(N):
##    r = []
##    i = 2
##    while i**2 < N:
##        if i**2 == N:
##            r.append(i)
##        elif N % i == 0:
##            r += [i, N // i]
##        i += 1
##    return sum(sorted(r)[-3:]) if len(r) >= 3 else 0
##
##c = 0
##for i in range(10000000, 1000000000):
##    sdiv = S(i)
##    if sdiv != 0 and str(sdiv) == ''.join(sorted(str(sdiv))):
##        print(sdiv)
##        c += 1
##        if c == 5:
##            break


'''
24. (Е. Джобс) Спутник принимает сигналы от разных станций на земле. Каждый сигнал имеет
координату источника – широту и долготу с точностью до десятых, выраженных целочисленными
значениями – удесятеренными координатами. Например, координаты (55,7°; 37,6°) записываются как
пара чисел 557 376.
Найдите значение долготы, с которой отправлено максимальное количество сигналов, а такжеколичество
различных градусов широты (от -90° до 90°, с отбрасыванием дробной части), с которых
пришли сигналы для найденной долготы. Если из нескольких долгот пришло одинаковое число
сигналов, следует выбрать долготу с наибольшим значением.
Входные данные представлены в файле 26-96.txt следующим образом. В первой строке входного
файла находится число N – количество сигналов (натуральное число, не превышающее 100 000).
Каждая из следующих N строк содержит два натуральных числа, значение широты (-900 до 900) и
значение долготы (-1800 до 1800).
Запишите в ответе два целых числа: значение долготы и количество целых градусов широты для нее.
Пример входного файла::
7
-123 407
-125 52
-128 52
802 407
809 52
805 407
850 53
Для приведённого примера видим две долготы с тремя сигналами: 5,2° и 40,7°. Cчитаем количество
целых значений широт для наибольшей долготы 40,7° (–12,3°; 80,2°; 80,5°). Следовательно, принято
три сигнала с двух различных широт: –12° и 80°. Ответ: 407 2.
'''
### TODO: Ответ – -162 31
##with open('data/26-96.txt') as f:
##    n = int(f.readline())
##    data = list(map(lambda x: tuple(map(int, x.split())), f.readlines()))
##res = {}
##for signal in data:
##    if signal[1] in res.keys():
##        res[signal[1]].append(int(signal[0] / 10))
##    else:
##        res[signal[1]] = [int(signal[0] / 10)]
##res = sorted(res.items(), key=lambda x: len(x[1]), reverse=True)
##res = list(filter(lambda x: len(x[1]) == len(res[0][1]), res))
##res = sorted(res, key=lambda x: x[0], reverse=True)[0]
##print(res[0], len(set(res[1])))


'''
25. (Д.Ф. Муфаззалов) Дан набор данных, состоящий из неотрицательных целых чисел. Из данного
набора выбрали некоторые (или все) числа и записали их подряд без пробелов в произвольном
порядке. Определите наибольшее значение с симметричной записью (читается справа налево и слева
направо одинаково), кратное числу 5, которое может быть получено таким образом. Гарантируется,
что искомое значение получить можно. Программа должна напечатать одно число – сумму цифр
искомого значения.
Входные данные. Даны два входных файла (файл A и файл B), каждый из которых содержит в первой
строке количество чисел N (1 ≤ N ≤ 100000). Каждая из следующих N строк содержит одно целое
неотрицательное число, каждое из которых меньше числа 10.
Пример входного файла:
10
8
3
2
3
5
9
5
3
9
9
Для указанных входных данных значением искомой суммы должно быть число 43. Соответствующее
ей симметричное число – 5939395.
В ответе укажите два числа: сначала значение искомой суммы для файла А, затем для файла B.
'''
### FIXME: Ответ – 
##with open('data/27-38a.txt') as f:
##    n = int(f.readline())
##    data = list(map(lambda x: x.strip(), f.readlines()))
##mx = 0
##print(data)
##for i in range(n, 1, -1):
##    for mk in set(elem for elem in permutations(data, r=i) if elem[0] != '0'):
##        mk = ''.join(mk)
##        if mk == mk[::-1] and not int(mk) % 5:
##            mx = max(mx, int(mk))
##            print(mk, sum(map(int, str(mx))))
##print(sum(map(int, str(mx))))