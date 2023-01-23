from typing import Callable


class Sort:
    @staticmethod
    # TODO: Bubble sorting method (https://sortvisualizer.com/bubblesort/)
    # TODO: Метод сортировки пузырьком (https://sortvisualizer.com/bubblesort/)
    def bubble(array: list | tuple | str,
               alg: Callable[[int | float | str, int | float | str], list] = lambda x, y: x < y,
               reverse: bool = False):
        tp = type(array)
        if tp != list:
            array = list(array)
        for i in range(len(array) - 1):
            for j in range(len(array) - i - 1):
                if alg(array[j + 1], array[j]) if not reverse else alg(array[j], array[j + 1]):
                    array[j + 1], array[j] = array[j], array[j + 1]
        if tp == str:
            return ''.join(array)
        return tp(array)

    @staticmethod
    # TODO: Shaker sorting method (https://sortvisualizer.com/shakersort/)
    # TODO: Метод сортировки шейкером (https://sortvisualizer.com/shakersort/)
    def shaker(array: list | tuple | str,
               alg: Callable[[int | float | str, int | float | str], list] = lambda x, y: x < y,
               reverse: bool = False):
        tp = type(array)
        if tp != list:
            array = list(array)
        left, right = 0, len(array) - 1
        while left <= right:
            for i in range(right, left, -1):
                if alg(array[i], array[i - 1]) if not reverse else alg(array[i - 1], array[i]):
                    array[i - 1], array[i] = array[i], array[i - 1]
            left += 1
            for i in range(left, right):
                if alg(array[i + 1], array[i]) if not reverse else alg(array[i], array[i + 1]):
                    array[i], array[i + 1] = array[i + 1], array[i]
            right -= 1
        if tp == str:
            return ''.join(array)
        return tp(array)

    @staticmethod
    # TODO: Insertion sorting method (https://sortvisualizer.com/shakersort/)
    # TODO: Метод сортировки вставками (https://sortvisualizer.com/shakersort/)
    def insertion(array: list | tuple | str,
                  alg: Callable[[int | float | str, int | float | str], list] = lambda x, y: x < y,
                  reverse: bool = False):
        tp = type(array)
        if tp != list:
            array = list(array)
        for i in range(1, len(array)):
            x = array[i]
            j = i - 1
            while j >= 0 and alg(x, array[j]) if not reverse else alg(array[j], x):
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = x
        if tp == str:
            return ''.join(array)
        return tp(array)

    @staticmethod
    # TODO: Counting sorting method (https://www.cs.usfca.edu /~galles/visualization/CountingSort.html )
    # TODO: Метод сортировки подсчётом (https://www.cs.usfca.edu/~galles/visualization/CountingSort.html)
    def counting(array: list | tuple,
                 reverse: bool = False):
        tp = type(array)
        array_init = [0] * (max(array) + 1)
        result = []
        for i in range(len(array)):
            array_init[array[i]] += 1
        for i in range(len(array_init)) if not reverse else range(len(array_init) - 1, -1, -1):
            if array_init[i]:
                for k in range(array_init[i]):
                    result.append(i)
        if tp == str:
            return ''.join(array)
        return tp(result)

    @staticmethod
    # TODO: Merge sorting method (https://sortvisualizer.com/mergesort/)
    # TODO: Метод сортировки слиянием (https://sortvisualizer.com/mergesort/)
    def merge(array):
        if len(array) <= 1:
            mediana = len(array) // 2
            left = array[:mediana]
            right = array[mediana:]
            Sort.merge(left)
            Sort.merge(right)
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    array[k] = left[i]
                    i += 1
                else:
                    array[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                array[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                array[k] = right[j]
                j += 1
                k += 1
        return array

    @staticmethod
    # TODO: Hoare's sorting method (https://sortvisualizer.com/quicksort/)
    # TODO: Метод сортировки Хоара (https://sortvisualizer.com/quicksort/)
    def quick(array: list | tuple | str,
              mni: int = 0,
              mxi: int | None = None,
              alg: Callable[[int | float | str, int | float | str], list] = lambda x, y: x < y,
              reverse: bool = False):
        def partition(array, mni, mxi):
            pivot = mni
            for i in range(mni + 1, mxi + 1):
                if alg(array[i], array[mni]) if not reverse else alg(array[mni], array[i]):
                    pivot += 1
                    array[i], array[pivot] = array[pivot], array[i]
            array[pivot], array[mni] = array[mni], array[pivot]
            return pivot

        tp = type(array)
        if tp != list:
            array = list(array)
        if mxi is None:
            mxi = len(array) - 1
        if mni >= mxi:
            return
        pivot = partition(array, mni, mxi)
        Sort.quick(array=array, mni=mni, mxi=pivot - 1, alg=alg, reverse=reverse)
        Sort.quick(array=array, mni=pivot + 1, mxi=mxi, alg=alg, reverse=reverse)
        if tp == str:
            return ''.join(array)
        return tp(array)


if __name__ == '__main__':
    from timeit import timeit
    from random import randint, choices

    l = 100
    array = [randint(0, 1000) for r in range(l)]
    # array = ''.join(choices(''.join(chr(i) for i in range(65, 91)), k=l))
    operations = 100000

    print('Bubble:')
    print('Before: {}'.format(array))
    print('After: {}'.format(Sort.bubble(array[:])))
    print('{} operations per {}\n'.format(operations, timeit('Sort.bubble({})'.format(array[:]) if type(array) != str
                                                             else 'Sort.bubble("{}")'.format(array[:]),
                                                             'from __main__ import Sort', number=operations)))
    print('Shaker:')
    print('Before: {}'.format(array))
    print('After: {}'.format(Sort.shaker(array[:])))
    print('{} operations per {}\n'.format(operations, timeit('Sort.shaker({})'.format(array[:]) if type(array) != str
                                                             else 'Sort.shaker("{}")'.format(array[:]),
                                                             'from __main__ import Sort', number=operations)))
    print('Insertion:')
    print('Before: {}'.format(array))
    print('After: {}'.format(Sort.insertion(array[:])))
    print('{} operations per {}\n'.format(operations, timeit('Sort.insertion({})'.format(array[:]) if type(array) != str
                                                             else 'Sort.insertion("{}")'.format(array[:]),
                                                             'from __main__ import Sort', number=operations)))

    if type(array) != str:
        print('Counting:')
        print('Before: {}'.format(array))
        print('After: {}'.format(Sort.counting(array[:], reverse=True)))
        print('{} operations per {}\n'.format(operations, timeit('Sort.counting({})'.format(array[:]),
                                                                 'from __main__ import Sort', number=operations)))

    print('Merge:')
    print('Before: {}'.format(array))
    print('After: {}'.format(Sort.bubble(array[:])))
    print('{} operations per {}\n'.format(operations, timeit('Sort.merge({})'.format(array[:]) if type(array) != str
                                                             else 'Sort.merge("{}")'.format(array[:]),
                                                             'from __main__ import Sort', number=operations)))

    print('Quick:')
    print('Before: {}'.format(array))
    print('After: {}'.format(Sort.quick(array[:])))
    print('{} operations per {}'.format(operations, timeit('Sort.quick({})'.format(array[:]) if type(array) != str
                                                           else 'Sort.quick("{}")'.format(array[:]),
                                                           'from __main__ import Sort', number=operations)))
