from functools import lru_cache

'''
1. Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежат две кучи камней.
Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может добавить в одну из куч
три камня или увеличить количество камней в куче в два раза. Чтобы делать ходы, у каждого
игрока есть неограниченное количество камней. Игра завершается в тот момент, когда суммарное
количество камней в кучах становится не менее 79. Победителем считается игрок, сделавший
последний ход, т. е. первым получивший позицию, в которой в кучах будет 79 или больше камней.
В начальный момент в первой куче было 9 камней, во второй куче – S камней, 1 ≤ S ≤ 69. Будем
говорить, что игрок имеет выигрышную стратегию, если он может выиграть при любых ходах
противника.
Ответьте на следующие вопросы:
Вопрос 1. Известно, что Ваня выиграл своим первым ходом после неудачного первого хода Пети.
Назовите минимальное значение S, при котором это возможно.
Вопрос 2. Укажите минимальное значение S, при котором у Пети есть выигрышная стратегия,
причём Петя не может выиграть первым ходом, но может выиграть своим вторым ходом независимо
от того, как будет ходить Ваня.
Вопрос 3. Найдите два значения S, при которых у Вани есть выигрышная стратегия, позволяющая
ему выиграть первым или вторым ходом при любой игре Пети, и при этом у Вани нет стратегии,
которая позволит ему гарантированно выиграть первым ходом. Найденные значения запишите в
ответе в порядке возрастания
'''
##@lru_cache(None)
##def game(x, y):
##    if x + y >= 79:
##        return 0
##    tmp = [game(x + 3, y), game(x, y + 3),
##           game(x * 2, y), game(x, y * 2),]
##    negative = [i for i in tmp if i <= 0]
##    if len(negative) != 0:
##        return -max(negative) + 1
##    return -max(tmp)
##
##
##print(min([i for i in range(1, 70) if game(9, i) == 2]))
##print(*[i for i in range(1, 70) if game(9, i) == -2])


'''
2. (ЕГЭ-2022) Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит куча
камней. Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может добавить в кучу
один камень или увеличить количество камней в куче в два раза. Для того чтобы делать ходы, у
каждого игрока есть неограниченное количество камней. Игра завершается в тот момент, когда
количество камней в куче становится не менее 165. Победителем считается игрок, сделавший
последний ход, т.е. первым получивший такую позицию, при которой в куче будет 165 или больше
камней. В начальный момент в куче было S камней; 1 ≤ S ≤ 164.
Ответьте на следующие вопросы:
Вопрос 1. Укажите такое значение S, при котором Петя не может выиграть за один ход, но при
любом ходе Пети Ваня может выиграть своим первым ходом.
Вопрос 2. Найдите два наименьших значения S, при которых у Пети есть выигрышная стратегия,
причём одновременно выполняются два условия:
− Петя не может выиграть за один ход;
− Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.
Найденные значения запишите в ответе в порядке возрастания.
Вопрос 3. Найдите минимальное значение S, при котором одновременно выполняются два условия:
– у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при
любой игре Пети;
– у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.
'''
##@lru_cache(None)
##def game(x):
##    if x >= 165:
##        return 0
##    tmp = [game(x + 1), game(x * 2)]
##    negative = [i for i in tmp if i <= 0]
##    if len(negative) != 0:
##        return -max(negative) + 1
##    return -max(tmp)
##
##
##print(*[i for i in range(1, 165) if game(i) == -1])
##print(*sorted([i for i in range(1, 165) if game(i) == 2])[:2])
##print(min([i for i in range(1, 165) if game(i) == -2]))


'''
3. (А. Кабанов) Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит куча
камней. Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может добавить в кучу
три камня или увеличить количество камней в куче в два раза. Например, имея кучу из 15 камней, за
один ход можно получить кучу из 18 или 30 камней. У каждого игрока, чтобы делать ходы, есть
неограниченное количество камней. Игра завершается в тот момент, когда количество камней в куче
становится не менее 33. Победителем считается игрок, сделавший последний ход, то есть первым
получивший кучу, в которой будет 33 или больше камней.
В начальный момент в куче было S камней, 1 ≤ S ≤ 32.
Ответьте на следующие вопросы:
Вопрос 1. Найдите минимальное значение S, при котором Ваня выигрывает своим первым ходом
при любой игре Пети.
Вопрос 2. Сколько существует значений S, при которых у Пети есть выигрышная стратегия, причём
одновременно выполняются два условия:
− Петя не может выиграть за один ход;
− Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.
Вопрос 3. Найдите два наибольших значения S, при которых одновременно выполняются два
условия:
– у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при
любой игре Пети;– у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.
Найденные значения запишите в ответе в порядке возрастания.
'''
##@lru_cache(None)
##def game(x):
##    if x >= 33:
##        return 0
##    tmp = [game(x + 3), game(x * 2)]
##    negative = [i for i in tmp if i <= 0]
##    if negative:
##        return -max(negative) + 1
##    return -max(tmp)
##
##
##print(min([i for i in range(1, 33) if game(i) == -1]))
##print(len([i for i in range(1, 33) if game(i) == 2]))
##print(*sorted(sorted([i for i in range(1, 33) if game(i) == -2], reverse=True)[:2]))


'''
4. (А. Богданов) Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит три кучи
камней. Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может добавить в одну
из куч 3, 13 или 23 камня. Игра завершается в тот момент, когда в сумме во всех кучах будет не менее
73 камней. Победителем считается игрок, сделавший последний ход. В начальный момент в кучах
было (2, S, 2S) камней, 1 ≤ S ≤ 23.
Ответьте на следующие вопросы:
Вопрос 1. Петя сделал неудачный ход, после которого Ваня сразу выиграл своим первым ходом.
Укажите минимальное значение S, при котором это возможно.
Вопрос 2. Найдите минимальное и максимальное значения S, при которых у Пети есть выигрышная
стратегия, причём Петя может выиграть своим вторым ходом независимо от того, как будет ходить
Ваня. Найденные значения запишите в ответе в порядке возрастания.
Вопрос 3. Найдите два значения S, при котором Петя может выбрать, первым или вторым ходом
выиграет Ваня, но у Пети нет выигрышной стратегии. Найденные значения запишите в ответе в
порядке возрастания.
'''
##@lru_cache(None)
##def game(x, y, z):
##    if x + y + z >= 73:
##        return 0
##    tmp = [
##        game(x + 3, y, z), game(x, y + 3, z), game(x, y, z + 3),
##        game(x + 13, y, z), game(x, y + 13, z), game(x, y, z + 13),
##        game(x + 23, y, z), game(x, y + 23, z), game(x, y, z + 23),
##        ]
##    negative = [i for i in tmp if i <= 0]
##    if negative:
##        return -max(negative) + 1
##    return -max(tmp)
##
##
##res1 = [i for i in range(1, 24) if game(2, i, 2*i) == 2]
##print(min(res1), max(res1))
##print(*sorted([i for i in range(1, 24) if game(2, i, 2*i) == -2])[1:])


'''
5. Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит две кучи камней.
Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может добавить в любую кучу
один камень или увеличить количество камней в любой куче в четыре раза. Игра завершается в тот
момент, когда общее количество камней в двух кучах становится не менее 95. Победителем считается
игрок, сделавший последний ход. В начальный момент в первой куче было 5 камней, а во второй – S
камней, 1 ≤ S ≤ 89.
Ответьте на следующие вопросы:
Вопрос 1. Известно, что Ваня выиграл своим первым ходом после неудачного первого хода Пети.
Назовите минимальное значение S, при котором это возможно.
Вопрос 2. Найдите минимальное и максимальное значение S, при котором у Пети есть выигрышная
стратегия, причём одновременно выполняются два условия:
− Петя не может выиграть за один ход;
− Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.
Найденные значения запишите в ответе в порядке возрастания.
Вопрос 3. Найдите значение S, при котором одновременно выполняются два условия:
– у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при
любой игре Пети;
– у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.
'''
@lru_cache(None)
def game(x, y):
    if x + y >= 95:
        return 0
    tmp = [
        game(x + 1, y), game(x, y + 1),
        game(x * 4, y), game(x, y * 4),
        ]
    negative = [i for i in tmp if i <= 0]
    if negative:
        return -max(negative) + 1
    return -max(tmp)


r1 = [i for i in range(1, 90) if game(5, i) == 2]
print(min(r1), max(r1))
print(*[i for i in range(1, 90) if game(5, i) == -2])
