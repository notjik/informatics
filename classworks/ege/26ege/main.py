from time import time
from bisect import bisect_left

start = time()


def timecomplete() -> None:
    print('\nThe program was completed in {} second!'.format(time() - start))
    return None


'''
1) В текстовом файле 26-1.txt находятся данные в формате, описанном выше в
формулировке задачи Р00. Решите задачу Р00.

Р-00 (демо-2021). Системный администратор раз в неделю создаёт архив
пользовательских файлов. Однако объём диска, куда он помещает архив,
может быть меньше, чем суммарный объём архивируемых файлов. Известно,
какой объём занимает файл каждого пользователя. По заданной информации
об объёме файлов пользователей и свободном объёме на архивном диске
определите максимальное число пользователей, чьи файлы можно сохранить в архиве,
а также максимальный размер имеющегося файла, который может быть сохранён
в архиве, при условии, что сохранены файлы максимально возможного числа
пользователей. 
Входные данные. В первой строке входного файла 26.txt находятся два числа:
S – размер свободного места на диске (натуральное число, не превышающее 100 000)
и N – количество пользователей (натуральное число, не превышающее 10000).
В следующих N строках находятся значения объёмов файлов каждого пользователя
(все числа натуральные, не превышающие 100), каждое в отдельной строке.
Запишите в ответе два числа: сначала наибольшее число пользователей,
чьи файлы могут быть помещены в архив, затем максимальный размер имеющегося
файла, который может быть сохранён в архиве, при условии, что сохранены
файлы максимально возможного числа пользователей. 
Пример входного файла:
100 4
80
30
50
40
При таких исходных данных можно сохранить файлы максимум двух пользователей.
Возможные объёмы этих двух файлов 30 и 40, 30 и 50 или 40 и 50.
Наибольший объём файла из перечисленных пар – 50, поэтому ответ для
приведённого примера:
2 50
'''
##with open('data/26-1.txt') as f: # v1
##    m, n = map(int, f.readline().split())
##    data = list(map(int, f.readlines()))
##s = m
##data.sort()
##a = []
##i = 0
##flag = True
##while flag:
##    if s - data[i] >= 0:
##        s -= data[i]
##        a.append(data[i])
##    else:
##        if sum(a[:-1] + [data[i]]) <= m:
##            a.pop(-1)
##            s -= data[i]
##            a.append(data[i])
##        else:
##            flag = False
##    i += 1
##
##print(len(a), max(a))
##timecomplete()

##with open('data/26-1.txt') as f: # v2
##    s, n = map(int, f.readline().split())
##    data = list(map(int, f.readlines()))
##data.sort()
##res, c, i = 0, 0, 0
##while res + data[i] <= s:
##    res, c, i = res + data[i], c + 1, i + 1
##res -= data[i-1]
##while res + data[i] <= s:
##    i += 1
##res += data[i-1]
##print(c, data[i-1])
##timecomplete()


'''
11) В текстовом файле 26-11.txt находятся данные в формате,
описанном выше в формулировке задачи Р00. Решите задачу Р00.

Р-00 (демо-2021). Системный администратор раз в неделю создаёт архив
пользовательских файлов. Однако объём диска, куда он помещает архив,
может быть меньше, чем суммарный объём архивируемых файлов. Известно,
какой объём занимает файл каждого пользователя. По заданной информации
об объёме файлов пользователей и свободном объёме на архивном диске
определите максимальное число пользователей, чьи файлы можно сохранить в архиве,
а также максимальный размер имеющегося файла, который может быть сохранён
в архиве, при условии, что сохранены файлы максимально возможного числа
пользователей. 
Входные данные. В первой строке входного файла 26.txt находятся два числа:
S – размер свободного места на диске (натуральное число, не превышающее 100 000)
и N – количество пользователей (натуральное число, не превышающее 10000).
В следующих N строках находятся значения объёмов файлов каждого пользователя
(все числа натуральные, не превышающие 100), каждое в отдельной строке.
Запишите в ответе два числа: сначала наибольшее число пользователей,
чьи файлы могут быть помещены в архив, затем максимальный размер имеющегося
файла, который может быть сохранён в архиве, при условии, что сохранены
файлы максимально возможного числа пользователей. 
Пример входного файла:
100 4
80
30
50
40
При таких исходных данных можно сохранить файлы максимум двух пользователей.
Возможные объёмы этих двух файлов 30 и 40, 30 и 50 или 40 и 50.
Наибольший объём файла из перечисленных пар – 50, поэтому ответ для
приведённого примера:
2 50
'''
# with open('data/26-11.txt') as f:
#    m, n = map(int, f.readline().split())
#    data = list(map(int, f.readlines()))
# s = m
# data.sort()
# a = []
# i = 0
# flag = True
# while flag:
#    try:
#        if s - data[i] >= 0:
#            s -= data[i]
#            a.append(data[i])
#        else:
#            if sum(a[:-1] + [data[i]]) <= m:
#                a.pop(-1)
#                s -= data[i]
#                a.append(data[i])
#            else:
#                flag = False
#        i += 1
#    except IndexError:
#        print('Full')
#        break
#
# print(len(a), max(a))
# timecomplete()


'''
21) (А.М. Кабанов, г. Тольятти) В магазине электроники раз в месяц
проводится распродажа. Из всех товаров выбирают K товаров с самой большой
ценой и делают на них скидку в 20%. По заданной информации о цене каждого
из товаров и количестве товаров, на которые будет скидка, определите цену
самого дорогого товара, не участвующего в распродаже, а также целую часть
от суммы всех скидок.
Входные и выходные данные. В первой строке входного файла 26-k1.txt находятся
два числа, записанные через пробел: N – общее количество цен
(натуральное число, не превышающее 10 000) и K – количество товаров со скидкой.
В следующих N строках находятся значения цены каждого из товаров
(все числа натуральные, не превышающие 10 000), каждое в отдельной строке.
Запишите в ответе два числа: сначала цену самого дорогого товара,
не участвующего в распродаже, а затем целую часть от суммы всех скидок.
Пример входного файла: 
10 3
1800
3600
3700
800
2600
2500
1800
1500
1900
1200
При таких исходных данных ответ должен содержать два числа – 2500 и 1980.
Пояснение: скидка будет на товары стоимостью 3700, 3600, 2600.
Тогда самый дорогой товар без скидки стоит 2500,
а сумма скидок 740+720+520 = 1980.
'''
# with open('data/26-k1.txt') as f: # v1
#    n, k = map(int, f.readline().split())
#    data = list(map(int, f.readlines()))
# data.sort(reverse=True)
# print(data[k], sum(data[:k]) * 0.2)
# timecomplete()
#
# with open('data/26-k1.txt') as f: # v2
#    n, k = map(int, f.readline().split())
#    data = list(map(int, f.readlines()))
# data.sort()
# res = sum([data.pop() for i in range(k)])
# print(data[-1], res * 0.2)
# timecomplete()


'''
24) (А.М. Кабанов, г. Тольятти) По итогам проверочной работы учащиеся школ
города получили определённое количество баллов, различное у каждого из
участников. K учеников с самым высоким результатом относят к группе отличников,
а K следующих за ними – к группе хорошистов. По заданной информации
о результатах каждого из учащихся, а также количеству учащихся в каждой группе
определите целую часть среднего балла в группе отличников и группе хорошистов.
Входные и выходные данные. В первой строке входного файла 26-k4.txt находится
два числа, записанные через пробел: N – общее количество результатов учащихся
(натуральное число, не превышающее 10 000), K – количество учащихся в каждой
из групп. В следующих N строках находятся количества баллов конкретных учащихся
(все числа натуральные, не превышающие 1000), каждое в отдельной строке.
Запишите в ответе два числа: сначала целую часть среднего балла у хорошистов,
а затем целую часть среднего балла у отличников.
Пример входного файла: 
10 2
298
28
293
214
209
54
24
157
247
52
При таких исходных данных ответ должен содержать 2 числа – 230 и 295.
Пояснение: Отличники набрали 298 и 293 балла, а хорошисты 247 и 214 баллов.
Тогда средний балл хорошистов 230,5, а средний балл отличников 295,5.
'''
# with open('data/26-k4.txt') as f: # v1
#    n, k = map(int, f.readline().split())
#    data = list(map(int, f.readlines()))
# data.sort(reverse=True)
# print(int(sum(data[k:2*k])/k), int(sum(data[:k])/k))


'''
30) (Е. Джобс) Для уменьшения аварий на центральной дороге в городе X
дорожная служба решила выровнять ямы. Новая яма будет иметь объем (в литрах),
равный значению медианы между объемами её самой и соседних слева и справа
ям до ремонта. При этом размеры первой и последней ямы решили не менять. 
Ночью перед ремонтом дороги в городе X прошел проливной дождь, поэтому все
ямы до краев заполнены водой. Сколько литров воды выльется обратно на
дорогу после проведения ремонта?
Примечание: медианой называется такое значение, относительно которого
в отсортированной последовательности слева и справа находится одинаковое
количество элементов.
Входные данные. 
В первой строке входного файла 26-J5.txt находится число N – количество
ям на дороге (натуральное число, не превышающее 10 000). В следующих N
строках находятся значения объемов ям (все числа натуральные,
не превышающие 25), каждое в отдельной строке. 
Запишите в ответе два числа: количество ям с наименьшим объемом и общий
объем воды, вылившейся из ям обратно на дорогу. 
Пример входного файла: 
8 
10
12
8
6
20
12
16
10
При таких исходных данных после ремонта объем ям будет выглядеть следующим
образом 10, 10, 8, 8, 12, 16, 12, 10. В ответе необходимо указать два числа
– 2 и 14.
'''
# with open('data/26-J5.txt') as f:
#    n = int(f.readline())
#    data = list(map(int, f.readlines()))
# res1, res2 = data.copy(), data.copy()
# for i in range(1, n - 1):
#    res1[i] = sorted(data[i-1:i+2])[1]
#    res2[i] = res1[i] if res1[i] < data[i] else data[i]
# print(res1.count(min(res1)), sum(data) - sum(res2))
# timecomplete()


'''
31) Магазин предоставляет оптовому покупателю скидку по следующим правилам:
− на каждый второй товар ценой больше 100 рублей предоставляется скидка 10 %;
− общая цена покупки со скидкой округляется вверх до целого числа рублей;
− порядок товаров в списке определяет магазин и делает это так,
чтобы общаясумма скидки была наименьшей.
Вам необходимо определить общую цену закупки с учётом скидки и цену самого
дорогого товара, на который будет предоставлена скидка.
Входные данные. Первая строка входного файла 26-s1.txt содержит число
N – общее количество купленных товаров. Каждая из следующих N строк
содержит одно целое число – цену товара в рублях. В ответе запишите два целых
числа: сначала общую цену покупки с учётом скидки, затем цену самого дорогого
товара, на который предоставлена скидка.
Пример входного файла
7
225
160
380
95
192
310
60
В данном случае товары с ценой 60 и 95 не участвуют в определении скидки,
остальные товары магазину выгодно расположить в таком порядке цен:
380, 160, 225, 192, 310. Скидка предоставляется на товары ценой 160 и 192.
Суммарная цена этих двух товаров со скидкой составит 316,8 руб.,
после округления – 317 руб. Общая цена покупки составит:
60 + 95 + 317 + 380 + 225 + 310 = 1387 руб. Самый дорогой товар,
на который будет получена скидка, стоит 192 руб. В ответе нужно записать числа
1387 и 192.
'''
# with open('data/26-s1.txt') as f:
#    n = int(f.readline())
#    data = list(map(int, f.readlines()))
# data100 = sorted([i for i in data if i > 100])
# datau100 = [i for i in data if i <= 100]
# mx = 0
# for i in range(len(data100[:len(data100) // 2])):
#    mx = max(mx, data100[i])
#    data100[i] = data100[i] * 0.9
# print(ceil(sum(data100 + datau100)), mx)
# timecomplete()


"""
35) (Е. Джобс) В проекте «СкупойПлатитДважды» 1 января решено тратить
на развитие 60% накоплений всех участников. При этом 20% самых богатых
участников вносят  80% от своих накоплений, остальные участники вносят
равный процент таким образом, чтобы общая сумма взносов всех участников
составила 60%, обозначенные выше.
Запишите в ответе два целых числа: сумма взноса от всех «богатых» участников
проекта и сумма взноса участника с самым небольшим размером накоплений.
Если в результате получаются дробные числа, нужно записать их целые части.
Входные данные.  В первой строке файла 26-j7.txt записано натуральное число
N – количество участников проекта (20 ≤ N ≤ 1000). В следующих N строках
находятся значения – размер накоплений всех пользователей
(все числа натуральные, не превышающие 1000), каждое в отдельной строке. 
Пример входного файла: 
10
10
12
25
25
40
35
18
19
10
12
При таких исходных данных ответ должен содержать 2 числа – 60 и 4.
Примечание: если при нахождении 20% от количества участников получается
нецелое число, нужно взять его целую часть.
"""
### TODO: Ответ – 143518 4
##with open('data/26-j7.txt') as f:
##    n = int(f.readline())
##    data = list(map(int, f.readlines()))
##data.sort(reverse=True)
##fee = sum(data)*0.6
##rich = sum(data[i] * 0.8 for i in range(int(n * 0.2)))
##remains = fee - rich
##for p in range(1, 101):
##    poor = [data[i] * (p/100) for i in range(int(n * 0.2) + 1, n)]
##    if sum(poor) >= remains:
##        print(int(rich), int(min(poor)))
##        break
    

'''
37) (А.М. Кабанов) На складе лежат пакеты с углём различного веса и стоимости.
Вес и стоимость записаны на каждом пакете как натуральные числа:
вес не превосходит 100, стоимость не превосходит 10000.
Для транспортировки отбираются K пакетов с самой низкой ценой угля за единицу
веса; при равной стоимости за единицу веса выбираются пакеты с большим весом.
По заданной информации о пакетах с углём и количестве транспортируемых пакетов
определите суммарный вес угля в отправленных пакетах и стоимость самого
тяжёлого отправленного пакета. 
Входные данные представлены в файле 26-k6.txt следующим образом.
В первой строке через пробел записаны числа N - количество пакетов на складе
(натуральное число, не превышающее 1000) и K –  количество пакетов на отправку
(натуральное число, не превосходящее 100). В каждой из последующих N строк
через пробел записаны два числа – вес и стоимость каждого пакета.
Запишите в ответе два числа – сначала суммарный вес угля в отправленных
пакетах, затем стоимость самого тяжёлого отправленного пакета.
Пример организации исходных данных во входном файле: 
10 4
47 470
50 600
60 480
45 540
30 300
15 180
70 560
30 360
91 910
40 320
При таких исходных данных самая низкая стоимость угля в пакетах весом
60, 70, 40; затем – у пакетов весом 91, 30, 47. Поэтому наибольший возможный
вес к отправке равен 70+60+40+91 = 261, а стоимость самого тяжёлого
отправленного пакета равна 910.
'''
##with open('data/26-k6.txt') as f:
##    n, k = map(int, f.readline().split())
##    data = list(map(lambda x: tuple(map(int, x.split())), f.readlines()))
##for i in range(n - 1):
##    for j in range(n - i - 1):
##        if (data[j + 1][0] / data[j + 1][1]) > (data[j][0] / data[j][1]) or \
##                ((data[j + 1][0] / data[j + 1][1]) == (data[j][0] / data[j][1]) and data[j + 1][0] > data[j][0]):
##            data[j + 1], data[j] = data[j], data[j + 1]
##res = data[:k]
##print(sum(i[0] for i in res), res[0][-1])


"""
39) Для перевозки партии грузов различной массы выделен грузовик,
но его грузоподъёмность ограничена, поэтому перевезти сразу все грузы
не удастся. Грузы массой от 180 до 200 кг включительно грузят в первую очередь,
выбирая грузы по убыванию массы, начиная с самого тяжёлого.
На оставшееся после этого место стараются взять как можно большее количество
грузов. Если это можно сделать несколькими способами, выбирают тот способ,
при котором самый большой из выбранных грузов имеет наибольшую массу.
Если и при этом условии возможно несколько вариантов, выбирается тот,
при котором наибольшую массу имеет второй по величине груз, и т.д.
Известны количество грузов, масса каждого из них и грузоподъёмность грузовика.
Необходимо определить количество и общую массу грузов, которые будут вывезены
при погрузке по вышеописанным правилам.
Входные данные представлены в файле 26-39.txt следующим образом.
В первой строке входного файла записаны два целых числа:
N – общее количество грузов и M – грузоподъёмность грузовика в кг.
Каждая из следующих N строк содержит одно целое число – массу груза в кг.
В ответе запишите два целых числа: сначала максимально возможное количество
грузов, затем их общую массу.
Пример организации исходных данных во входном файле: 
6 700
100
185
120
160
140
300
В данном случае сначала нужно взять груз массой 185 кг. Остается 515 кг.
После этого можно вывезти ещё максимум 3 груза.
Это можно сделать четырьмя способами:
100 + 120 + 140, 100 + 140 + 160, 100 + 120 + 160, 120 + 140 + 160.
Выбираем способ, при котором вывозится груз наибольшей возможной массы.
Таких способов три: 100 + 120 + 160, 100 + 140 + 160, 120 + 140 + 160.
Из этих способов выбираем те, при которых больше масса второго по величине
груза, то есть 100 + 140 + 160 и 120 + 140 + 160.
Их них нужно выбрать вариант 120 + 140 + 160, так как в этом случае третий
по величине груз наиболее тяжёлый. Всего получается 4 груза общей массой 605 кг.
Ответ: 4 605.
"""
### TODO: Ответ – 118 6982 (118 10000) 
with open('data/26-39.txt') as f:
    n, m = map(int, f.readline().split())
    data = list(map(int, f.readlines()))
first = sorted(list(filter(lambda x: 180 <= x <= 200, data)), reverse=True)
data = sorted(list(filter(lambda x: x < 180 or x > 200, data)))
remains = m - sum(first)
pos = []
for i in range(len(data)):
    if remains - data[i] >= 0:
        pos.append(i)
        remains -= data[i]
for i in range(len(pos) - 1, -1, -1):
    start = pos[i]
    end = len(data) if i == len(pos) - 1 else pos[i+1]
    remains += data[start]
    p = start
    for j in range(start, end):
        if remains >= data[j]:
            p = j
    remains -= data[p]
    pos[i] = p
print(len(pos) + len(first), m - sum(first) - remains)


'''
42) Предприятие производит оптовую закупку изделий A и Z, на которую
выделена определённая сумма денег. У поставщика есть в наличии партии этих
изделий различных модификаций по различной цене. На выделенные деньги
необходимо приобрести как можно больше изделий Z (независимо от модификации).
Закупать можно любую часть каждой партии. Если у поставщика закончатся изделия
Z, то на оставшиеся деньги необходимо приобрести как можно больше изделий A.
Известна выделенная для закупки сумма, а также количество и цена различных
модификаций данных изделий у поставщика. Необходимо определить, сколько будет
закуплено изделий A и какая сумма останется неиспользованной. Если возможно
несколько вариантов решения (с одинаковым количеством закупленных изделий А),
нужно выбрать вариант, при котором оставшаяся сумма максимальна.
Входные данные представлены в файле 26-42.txt следующим образом.  Первая строка
входного файла содержит два целых числа: N – общее количество партий изделий у
поставщика и S – сумма выделенных на закупку денег (в рублях).
Каждая из следующих N строк описывает одну партию изделия: сначала записана
буква A или Z (тип изделия), а затем – два целых числа: цена одного изделия в
рублях и количество изделий в партии. Все данные в строках входного файла
разделены одним пробелом.
В ответе запишите два целых числа: сначала количество закупленных изделий типа
A, затем оставшуюся неиспользованной сумму денег.
Пример входного файла
4 1000
A 14 12 
Z 30 7 
A 40 24 
Z 50 15
В данном случае сначала нужно купить изделия Z: 7 изделий по 30 рублей и 15
изделий по 50 рублей. На это будет потрачено 960 рублей.
На оставшиеся 40 рублей можно купить 2 изделия A по 14 рублей.
Таким образом, всего будет куплено 2 изделия A и останется 12 рублей.
В ответе надо записать числа 2 и 12.
'''
# with open('data/26-42.txt') as f:
#    n, s = map(int, f.readline().split())
#    data = [(i[0], int(i[1]), int(i[2]))
#            for i in map(lambda x: tuple(x.split()),f.readlines())]
# dataz = list(filter(lambda x: x[0] == 'Z', data))
# buya = s - sum([i[1] * i[2] for i in dataz])
# dataa = list(filter(lambda x: x[0] == 'A', data))
# dataa.sort(key=lambda x: x[1])
# c = 0
# for p in dataa:
#    if buya >= p[1] * p[2]:
#        c += p[2]
#        buya -= p[1] * p[2]
#    else:
#        for i in range(p[2]):
#            if buya >= p[1]:
#                c += 1
#                buya -= p[1]
#            else:
#                break
# print(c, buya)
# timecomplete()


'''
45) (А. Кабанов) В текстовом файле записан набор натуральных чисел.
Гарантируется,  что  все  числа  различны.  Необходимо  определить,
сколько в наборе  таких  пар чисел с чётной суммой,  что  их  среднее
арифметическое  тоже присутствует в файле, и чему равно наибольшее из
средних арифметических таких пар.
Входные данные представлены в файле 26-45.txt следующим образом.
Первая строка содержит целое число N – общее количество чисел в наборе.
Каждая из следующих N строк содержит одно число, не превышающее 109. 
В  ответе  запишите  два  целых  числа:  сначала  количество  пар,
затем наибольшее среднее арифметическое.
Пример входного файла:
6 
3 
8 
14 
11 
2 
17
В данном случае есть три подходящие пары: 8 и 14 (среднее арифметическое 11),
14 и 2 (среднее арифметическое 8), 11 и 17 (среднее арифметическое 14).
В ответе надо записать числа 3 и 14.
'''
# with open('data/26-45.txt') as f:
#    n = int(f.readline())
#    data = list(map(int, f.readlines()))
# data.sort()
# c, mxavg = 0, 0
# for i in range(n):
#    for j in range(i + 1, n):
#        if not ((data[i] + data[j]) % 2):
#            avg = (data[i] + data[j]) // 2
#            p = bisect_left(data, avg)
#            if data[p] == avg:
#                c += 1
#                mxavg = max(mxavg, avg)
# print(c, mxavg)
# timecomplete()


'''
57) (А. Богданов) Начинающему админу Ване для тренировки выдали аппарат для
сварки оптоволокна и N кусков оптоволокна, из которых попросили получить
цельные куски по M метров. С целью снижения затухания сигнала в полученном
кабеле нужно минимизировать количество сварок. Да и работы меньше.
Укажите в ответе два числа: сколько всего сварок будет в цельных кусках и
сколько останется кусков, из которых не сварить цельный кусок требуемой длины.
Ваня выбирал куски строго по уменьшению длины, за исключением последнего,
который выбирался исходя из минимизации длины каждого обрезка.
Обрезок идет обратно в пучок кусков для следующего использования. 
Входные данные представлены в файле 26-57.txt следующим образом.
В первой строке входного файла записаны значения N
(количество кусков оптоволокна) и M (длина необходимого цельного куска).
Каждая из следующих N строк содержит одно целое число – длину очередного куска.
Пример входного файла:
10 30
17 15 14 12 11 8 6 5 4 2
Сперва взяли 17 и 14, обрез 1 обратно в кучу [15,12,11,8,6,5,4,2,1] – одна
сварка.  Затем взяли 15,12 и 4, обрез длиной 1 обратно в кучу [11,8,6,5,2,1,1]
– две сварки. И затем взяли 11,8,6 и 5, ровно 30, без обреза – три сварки.
Итого: 6 сварок и 3 оставшихся куска оптоволокна. 
'''
# with open('data/26-57.txt') as f: # TODO: dont complete
#     n, m = map(int, f.readline().split())
#     data = list(map(int, f.readlines()))
# c = 0
# while sum(data) > m:
#     data.sort()
#     tmp = 0
#     while tmp < m:
#         c += 1
#         find = bisect_left(data, m - tmp)
#         if find == len(data):
#             tmp += data.pop()
#         else:
#             tmp += data.pop(find)
#     d = tmp - m
#     if d:
#         data.append(tmp - m)
# print(c, len(data))
# timecomplete()

# with open('data/26-57.txt') as f:
#     n, m = map(int, f.readline().split())
#     data = list(map(int, f.readlines()))
# data.sort()
# res = rest = 0
# while len(data):
#     tmp = m
#     count = 0
#     while data and tmp:
#         find: int = bisect_left(data, tmp)
#         if find == len(data):
#             tmp -= data.pop()
#             count += 1
#         elif data[find] <= tmp:
#             tmp -= data.pop(find)
#             count += 1
#         elif data[find] > tmp:
#             r = data[find] - tmp
#             data.pop(find)
#             tmp = 0
#             find = bisect_left(data, r)
#             data.insert(find, r)
#             count += 1
#     if not tmp:
#         res += count - 1
#     else:
#         rest = count
# print(res, rest)
# timecomplete()


'''
79)	(Досрочный ЕГЭ-2022) В лесополосе осуществляется посадка деревьев:
саженцы высаживают рядами на одинаковом расстоянии. Спустя некоторое время с
помощью аэросъемки выясняют, какие саженцы прижились. Необходимо определить
ряд с максимальным номером, в котором есть подряд ровно K неприжившихся
саженцев при условии, что справа и слева от них саженцы прижились.  В ответе
запишите сначала наибольший номер ряда, затем наименьший номер неприжившегося
саженца.
Входные данные представлены в файле 26-79.txt следующим образом.
В первой строке записаны два числа: N – количество занятых мест
(натуральное число, не превышающее 10 000) и K – длина цепочки неприжившихся
саженцев, которую нужно найти. Каждая из следующих N строк содержит сведения
об одном прижившемся саженце – два натуральных числа, не превышающих 100 000:
номер ряда и номер саженца в ряду.
Пример входного файла:
6 3
40 30 
40 34 
50 125 
50 129 
50 64 
50 68
В примере требуется найти 3 подряд идущих неприжившихся саженца. Ответ: 50 65.
'''
##with open('data/26-79.txt') as f:
##    n, k = map(int, f.readline().split())
##    d = {}
##    for i in f:
##        try:
##            r, c = map(int, i.split())
##            if r in d:
##                d[r].append(c)
##            else:
##                d[r] = [c]
##        except ValueError:
##            pass
##for r in d:
##    d[r].sort()
##keys = sorted(d.keys())
##for r in keys[::-1]:
##    for i in range(len(d[r]) - 1):
##        if d[r][i+1] - d[r][i] - 1 == k:
##            print(r, d[r][i] + 1)
##            raise SystemExit(0)

        
'''
81) (М. Ишимов) Семья М. собирается купить билеты на самолет, чтобы полететь
на отдых. Они выбрали рейс с двухэтажным самолётом. Так как в составе семьи,
помимо папы и мамы, имеется двое детей, билеты смотрят так, чтобы вся семья
летела в одном ряду. Каждый из них боится высоты, поэтому места у окон должны
быть заняты другими людьми. Места у окон считаются самые крайние места в
каждом ряду (первое и последнее). 
Известно, какие места уже куплены (заняты). Найдите ряд с наибольшим номером,
в котором можно забронировать подходящие места для всей семьи. Гарантируется,
что есть хотя бы один ряд, удовлетворяющий этому условию. 
Входные данные представлены в файле 26-81.txt следующим образом.
В первой строке входного файла записаны два числа, разделённые пробелом:
N – количество занятых мест (натуральное число, не превышающее 20 000) и
K – количество мест в каждом ряду самолета.
Каждая из следующих N строк содержит три натуральных числа, не превышающих
100 000: номер этажа, номер ряда и номер занятого места в этом ряду.
Запишите в ответе два числа: максимальный номер ряда и общее количество таких
рядов, в которых можно забронировать подряд идущие свободные места без мест
у окон.
Пример входного файла:
7 6
1 50 2
2 23 1
1 50 6
1 1 1
2 30 5
2 23 6
1 1 6
Для этих данных можно забронировать 4 соседних места в двух рядах: в 1-м ряду
на 1-м этаже и в 23-м ряду на 2-м этаже. Ответ: 23 2.
'''
##with open('data/26-81.txt') as f:
##    n, k = map(int, f.readline().split())
##    d = {1: {}, 2:{}}
##    for i in f:
##        try:
##            h, r, c = map(int, i.split())
##            if r in d[h]:
##                d[h][r].append(c)
##            else:
##                d[h][r] = [c]
##        except ValueError:
##            pass
##for r in d[1]:
##    d[1][r] = list(set(d[1][r]))
##    d[1][r].sort()
##for r in d[2]:
##    d[2][r] = list(set(d[2][r]))
##    d[2][r].sort()
##keys1 = sorted(d[1].keys())
##keys2 = sorted(d[2].keys())
##res = []
##for r in keys1[::-1]:
##    if 1 in d[1][r] and k in d[1][r] and k - len(d[1][r]) >= 4:
##        res.append(r)
##for r in keys2[::-1]:
##    if 1 in d[2][r] and k in d[2][r] and k - len(d[2][r]) >= 4:
##        res.append(r)
##print(max(res), len(res))


"""
82) При проведении эксперимента заряженные частицы попадают на чувствительный
экран, представляющий из себя матрицу размером 10000 на 10000 точек.
При попадании очередной частицы на экран в файл записываются координаты
чувствительного элемента: номер строки (целое число от 1 до 10000) и номер
позиции в строке (целое число от 1 до 10000). Точка экрана, в которую попала
хотя бы одна частица, считается светлой, точка, в которую ни одна частица не
попала, – тёмной.
Вам необходимо по заданному протоколу определить номер строки с наибольшим
количеством светлых точек в чётных позициях. Если таких строк несколько,
укажите номер первой из подходящих строк.
Входные данные представлены в файле 26-82.txt следующим образом.
В первой строке входного файла записано целое число N – количество частиц,
попавших на экран. В каждой из следующих N строк записаны по два числа,
разделённые пробелом: номер строки и номер позиции в строке.
Запишите в ответе два числа: сначала наибольшее количество светлых точек
в чётных позициях одной строки, затем – номер строки, в которой находятся
эти точки.
Пример входного файла:
7
1 2
2 3
3 6
2 5
1 4
2 5
2 3
При таких исходных данных в строке 1 имеются две точки в чётных позициях
(2 и 4). Ответ: 2 1.
"""
##with open('data/26-82.txt') as f:
##    n = int(f.readline())
##    data = list(map(lambda x: list(map(lambda y: int(y) - 1, x.split())), f.readlines()))
##matrix = [[0 for _ in range(10000)] for __ in range(10000)]
##for i in data:
##    matrix[i[0]][i[1]] = 1
##index_column = -1
##result = []
##for i, ie in enumerate(matrix):
##    even_column = [je for j, je in enumerate(ie) if j % 2]
##    if sum(even_column) > sum(result):
##        index_column = i + 1
##        result = even_column
##print(sum(result), index_column)


"""
83) При проведении эксперимента заряженные частицы попадают на чувствительный
экран, представляющий из себя матрицу размером 10000 на 10000 точек.
При попадании очередной частицы на экран в файл записываются координаты
чувствительного элемента: номер строки (целое число от 1 до 10000) и номер
позиции в строке (целое число от 1 до 10000). Точка экрана, в которую попала
хотя бы одна частица, считается светлой, точка, в которую ни одна частица
не попала, – тёмной.
Вам необходимо по заданному протоколу определить номер строки с наибольшим
количеством светлых точек в нечётных позициях. Если таких строк несколько,
укажите номер первой из подходящих строк.
Входные данные представлены в файле 26-82.txt следующим образом.
В первой строке входного файла записано целое число N – количество частиц,
попавших на экран. В каждой из следующих N строк записаны по два числа,
разделённые пробелом: номер строки и номер позиции в строке.
Запишите в ответе два числа: сначала наибольшее количество светлых точек
в нечётных позициях одной строки, затем – номер строки, в которой находятся
эти точки.
Пример входного файла:
7
1 2
2 3
3 6
2 5
1 4
2 5
2 3
При таких исходных данных в строке 2 имеются две точки в чётных позициях
(3 и 5). Ответ: 2 2.
"""
##with open('data/26-82.txt') as f:
##    n = int(f.readline())
##    data = list(map(lambda x: list(map(lambda y: int(y) - 1, x.split())), f.readlines()))
##matrix = [[0 for _ in range(10000)] for __ in range(10000)]
##for i in data:
##    matrix[i[0]][i[1]] = 1
##index_column = -1
##result = []
##for i, ie in enumerate(matrix):
##    odd_column = [je for j, je in enumerate(ie) if not(j % 2)]
##    if sum(odd_column) > sum(result):
##        index_column = i + 1
##        result = odd_column
##print(sum(result), index_column)


'''
84) (99 баллов) В университете Инфаполис учится N групп студентов,
для обучения которых используется N аудиторий. Известно количество студентов
в каждой группе и количество мест в каждой аудитории. Группа всегда занимает
целую аудиторию (группы не объединяются). Администрацию университета
заинтересовал вопрос: сколько существует способов рассадить все группы
по аудиториям, и сколько групп (по одной) вмещаются в самую маленькую аудиторию.
Входные данные представлены в файле 26-84.txt следующим образом.
В первой строке записано натуральное число N (1 ≤ N ≤ 100 000) – количество
аудиторий (и количество групп). В следующей строке записано N натуральных
чисел – количество студентов в каждой группе (целые числа, не превышающие
1 000 000). В третьей строке записано N натуральных чисел – количество мест
в каждой аудитории (целые числа, не превышающие 1 000 000). 
Запишите в ответе два числа: сначала количество способов рассадить всех
по аудиториям по модулю 100000007 (то есть, остаток от деления искомого числа
на 100000007), затем количество групп, каждая из которых помещается в самую
маленькую аудиторию.
Пример входного файла:
3
2 3 4
5 6 3
При таких исходных данных всего есть 4 варианта размещения
(A5: 2 означает, что в аудитории вместимостью 5 человек размещается группа
из 2-х человек): 
1)	A5: 2, A6: 4, A3: 3,
2)	A5: 4, A6: 2, A3: 3,
3)	A5: 4, A6: 3, A3: 2,
4)	A5: 3, A6: 4, A3: 2. 
В самой маленькой аудитории (на 5 человек) можно разместить одну из двух
2 групп (из 2-х или 3-х человек). Ответ: 4 2.
'''
##with open('data/26-84.txt') as f:
##    n = int(f.readline())  # кол-во аудиторий и групп
##    groups = sorted(list(map(int, f.readline().split()))) # группы
##    auditories = sorted(list(map(int, f.readline().split()))) # аудитории
##pick = [] # в какое кол-во аудиторий поместиться каждая из групп
##for i in groups: # проходимся по каждой группе
##    position = bisect_left(auditories, i) # ищем крайний индекс (в котором лежал бы элемент) подходящей аудитории
##    pick.append(len(auditories) - position) # записываем кол-во аудиторий, в которые помещаются группы
##result = pick[-1] # берём самую большую группу
##k = len(pick) # количество групп
##for i in range(k - 2, -1, -1): # проходимся по найденным значениям
##    result *= (pick[i] - (k - i - 1)) # находим количество подходящих значений
##print(result % 100000007) # выводим ответ
##print(sum([1 for i in groups if auditories[0] - i  >= 0])) # находим кол-во групп, вмещаемых в самую маленькую аудиторию
