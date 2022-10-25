from functools import lru_cache
import json
from pprint import pprint

'''
43)	(А. Кабанов) Два игрока, Петя и Ваня, играют в следующую игру.
Перед игроками лежит куча камней. Игроки ходят по очереди, первый ход делает
Петя. За один ход игрок может
а) добавить в кучу один камень;
б) добавить в кучу два камня;
в) добавить в кучу три камня;
г) увеличить количество камней в куче в два раза.
Игра завершается в тот момент, когда количество камней в куче превышает 33.
Победителем считается игрок, сделавший последний ход, то есть первым получивший
кучу, в которой будет 34 или больше камней. В начальный момент в куче было S
камней, 1 ≤ S ≤ 33.
Задание 19. 
Найдите значение S, при котором Ваня выигрывает своим первым ходом при любой
игре Пети?
Задание 20.
Найдите минимальное и максимальное значение S, при котором у Пети есть
выигрышная стратегия, причём одновременно выполняются два условия:
− Петя не может выиграть за один ход;
− Петя может выиграть своим вторым ходом независимо от того, как будет ходить
Ваня.
Найденные значения запишите в ответе в порядке возрастания.
Задание 21
Найдите значение S, при котором одновременно выполняются два условия:
– у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым
ходом при любой игре Пети;
– у Вани нет стратегии, которая позволит ему гарантированно выиграть первым
ходом. 
'''
##@lru_cache(None) # 43
##def game1(x): # создаем функцию с одним входным значением
##    if x >= 34: # условие выхода из игры
##        return 0
##    tmp = [game1(x+1), game1(x+2), game1(x+3), game1(x*2)] # массив ходов
##    negative = [i for i in tmp if i <= 0] # выборка характеристики хода
##                                          # следующего игрока
##    if len(negative) != 0: # проверка характеристики
##        return -max(negative)+1 
##    else:
##        return -max(tmp)


'''
11)	За один ход игрок может добавить в одну из куч (по своему выбору) два
камня или увеличить количество камней в куче в два раза. Игра завершается в тот
момент, когда суммарное количество камней в кучах становится не менее 62.
Победителем считается игрок, сделавший последний ход, т.е. первым получивший
такую позицию, при которой в кучах будет 62 или больше камней. В начальный
момент в первой куче было 7 камней, во второй куче – S камней; 1 ≤ S ≤ 54.
Задание 19. 
Известно, что Ваня выиграл своим первым ходом после неудачного первого хода
Пети. Укажите минимальное значение S, когда такая ситуация возможна.
Задание 20.
Найдите минимальное значение S, при котором у Пети есть выигрышная стратегия,
причём одновременно выполняются два условия:
− Петя не может выиграть за один ход;
− Петя может выиграть своим вторым ходом независимо от того, как будет ходить
Ваня.
Задание 21
Найдите два значения S, при которых одновременно выполняются два условия:
– у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым
ходом при любой игре Пети;
– у Вани нет стратегии, которая позволит ему гарантированно выиграть первым
ходом. 
Найденные значения запишите в ответе в порядке возрастания.
'''
##@lru_cache(None) # 11
##def game2(x, y):
##    if x + y >= 62:
##        return 0
##    tmp = [game2(x+2,y), game2(x, y+2),
##           game2(x*2, y), game2(x, y*2)]
##    negative = [i for i in tmp if i <= 0]
##    if len(negative) != 0:
##        return -max(negative)+1
##    else:
##        return -max(tmp)

'''
53)	(Д. Ф. Муфаззалов, г. Уфа) Два игрока, Петя и Ваня, играют в следующую игру.
Перед игроками лежит куча, состоящая из S конфет. Игроки ходят по очереди, первый ход делает Петя.
За один ход игрок может съесть не более пяти, но не менее одной конфеты или съесть половину конфет,
если число конфет четное. Съесть можно только целое количество конфет.
Игра завершается в тот момент, когда в куче останется менее десяти конфет.
Победителем считается игрок, который сделал последний ход.
Задание 19. Укажите значение S, при которых Ваня выиграет первым ходом.
Задание 20. Укажите минимальное и максимальное S, при которых Петя не может выиграть первым ходом,
но может выиграть вторым ходом при любом ходе Вани.
Задание 21. Укажите такое значение S, при котором у Вани есть выигрышная стратегия,
позволяющая ему выиграть первым или вторым ходом при любой игре Пети, и при этом у Вани нет стратегии,
которая позволит ему гарантированно выиграть первым ходом.
'''
##@lru_cache(None) # 53
##def game(x): 
##    if x < 10:
##        return 0
##    tmp = [game(x-1), game(x-2), game(x-3), game(x-4), game(x-5)]
##    if not(x % 2):
##        tmp.append(game(x//2))
##    negative = [i for i in tmp if i <= 0] 
##    if len(negative) != 0: 
##        return -max(negative)+1 
##    else:
##        return -max(tmp)


'''
65)	(А. Кабанов) Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит две кучи камней.
Игроки ходят по очереди, первый ход делает Петя.
За один ход игрок может убрать из кучи один камень или уменьшить
количество камней в любой куче в два раза (если количество камней нечётно,
то остаётся на один камень меньше, чем убирается).
Игра завершается в тот момент, когда суммарное количество камней в двух кучах становится не более 18,
побеждает игрок, сделавший последний ход. В начальный момент в первой куче было K≥1 камней,
а во второй – S≥1 камней, S+K ≥ 19.
Ответьте на следующие вопросы:
Задание 19. Известно, что из начальной позиции (M; M) Ваня выигрывает первым ходом при любой игре Пети.
При каком значении M это возможно?
Задание 20. При K=13, найдите минимальное и максимальное значение S, при котором у Пети есть выигрышная стратегия,
причём одновременно выполняются два условия:
− Петя не может выиграть за один ход;
− Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.
Найденные значения запишите в ответе в порядке возрастания.
Задание 21. При каком минимальном значении N для начальной пары (N;N) одновременно выполняются два условия:
– у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети;
– у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.
'''
##@lru_cache(None) # 65
##def game(x, y): 
##    if x + y <= 18:
##        return 0
##    tmp = []
##    if x > 1:
##        tmp.append(game(x-1,y))
##        tmp.append(game(x//2, y))
##    if y > 1:
##        tmp.append(game(x, y-1))
##        tmp.append(game(x, y//2))
##    negative = [i for i in tmp if i <= 0]
##    if len(negative) != 0:
##        return -max(negative)+1
##    else:
##        return -max(tmp)

'''
69)	Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит две кучи камней. Игроки ходят по очереди,
первый ход делает Петя. За один ход игрок может
а) добавить в любую кучу один камень;
б) добавить в любую кучу столько камней, сколько их в данный момент в другой куче.
Игра завершается в тот момент, когда суммарное количество камней в двух кучах становится не менее 64, побеждает игрок,
сделавший последний ход. В начальный момент в первой куче было 6 камней, а во второй – S камней, 1 ≤ S ≤ 57.
Задание 19. 
Известно, что Ваня выиграл своим первым ходом после первого хода Пети. Назовите минимальное значение S, при котором это
возможно.
Задание 20.
Найдите два таких значения S, при которых у Пети есть выигрышная стратегия, причём одновременно выполняются два условия:
− Петя не может выиграть за один ход;
− Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.
Найденные значения запишите в ответе в порядке возрастания.
Задание 21
Найдите значение S, при котором одновременно выполняются два условия:
– у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети;
– у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом. 
'''
##@lru_cache(None) # 69
##def game(x, y):
##    if x + y >= 64:
##        return 0
##    tmp = [game(x+1,y), game(x, y+1),
##           game(x+y, y), game(x, y+x)]
##    negative = [i for i in tmp if i <= 0]
##    if len(negative) != 0:
##        return -max(negative)+1
##    else:
##        return -max(tmp)

'''
87)	(А. Богданов) Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит три кучи камней.
Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может добавить в одну из куч 3, 13 или 23 камня.
Игра завершается в тот момент, когда в сумме в кучах будет не менее 73 камней.
Победителем считается игрок, сделавший последний ход. В начальный момент в кучах было (2, S, 2S) камней, 1 ≤ S ≤ 23.
Задание 19. 
При некотором значении S Ваня одержал победу свои первым ходом после неудачного хода Пети.
Укажите минимальное значение S, при котором это возможно.
Задание 20.
Найдите минимальное и максимальное значения S, при которых Петя выигрывает вторым ходом при любом ходе Вани.
Задание 21
Найдите два значения S, при которых выигрышная стратегия есть у Вани, но Петя может выбрать,
каким ходом выиграет Ваня – первым или вторым. 
'''


@lru_cache(None)  # 87
def game(x, y, z):
    if x + y + z >= 73:
        return 0
    tmp = [game(x + 3, y, z), game(x, y + 3, z), game(x, y, z + 3),
           game(x + 13, y, z), game(x, y + 13, z), game(x, y, z + 13),
           game(x + 23, y, z), game(x, y + 23, z), game(x, y, z + 23)]
    negative = [i for i in tmp if i <= 0]
    if len(negative) != 0:
        return -max(negative) + 1
    else:
        return -max(tmp)


################################################################################
print([i for i in range(1, 23) if game(2, i, 2 * i) == -1])
print([i for i in range(1, 23) if game(2, i, 2 * i) == 2])
print([i for i in range(1, 23) if game(2, i, 2 * i) == -2])
