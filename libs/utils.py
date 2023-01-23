from time import time


class DivFunc:
    @staticmethod
    # TODO: Поиск всех делителей
    def divisor(x: int) -> list:
        a = []
        i = 1
        while i ** 2 <= x:
            if i ** 2 == x:
                a.append(i)
            elif x % i == 0:
                a += [i, x // i]
            i += 1
        a.sort()
        return a

    @staticmethod
    # TODO: Поиск нетривиальных делителей
    def nontrivial_divisor(x: int) -> list:
        a = []
        i = 2
        while i ** 2 <= x:
            if i ** 2 == x:
                a.append(i)
            elif x % i == 0:
                a += [i, x // i]
            i += 1
        a.sort()
        return a

    @staticmethod
    def is_prime(n):
        for i in range(2, (n // 2) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def is_square(n):
        return (n ** 0.5) % 1 == 0


class NumeralSystem:
    @staticmethod
    # TODO: Перевод в другую систему счисления
    def to_base(n: int, b: int) -> str:
        alpha = '0123456789abcdefghijklmnopqrstuvwxyz'
        r = alpha[n % b]
        while n >= b:
            n //= b
            r += alpha[n % b]
        return r[::-1]


class PerformanceTracking:
    # TODO: Инициализация класса, начало отсчёта
    def __init__(self):
        self.start = time()

    # TODO: Удаление объекта, окончание отсчёта
    def __del__(self):
        print('\nThe program was completed in {} second!'.format(time() - self.start))
