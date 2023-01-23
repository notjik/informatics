class Sort:
    @staticmethod
    # TODO: Метод сортировки пузырьком (https://sortvisualizer.com/bubblesort/)
    def bubble(array, alg=lambda x, y: x < y, reverse=False):
        for i in range(len(array) - 1):
            for j in range(len(array) - i - 1):
                if alg(array[j + 1], array[j]) if not reverse else alg(array[j], array[j + 1]):
                    array[j + 1], array[j] = array[j], array[j + 1]
        return array

    @staticmethod
    # TODO: Метод сортировки шейкером (https://sortvisualizer.com/shakersort/)
    def shaker(array, alg=lambda x, y: x < y, reverse=False):
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
        return array

    @staticmethod
    # TODO: Метод сортировки вставками (https://sortvisualizer.com/shakersort/)
    def insertion(array, alg=lambda x, y: x < y, reverse=False):
        for i in range(1, len(array)):
            x = array[i]
            j = i - 1
            while j >= 0 and alg(x, array[j]) if not reverse else alg(array[j], x):
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = x
        return array

    @staticmethod
    # TODO: Метод сортировки вставками (https://www.cs.usfca.edu/~galles/visualization/CountingSort.html)
    def counting(array, reverse=False):
        array_init = [0] * (max(array) + 1)
        result = []
        for i in range(len(array)):
            array_init[array[i]] += 1
        for i in range(len(array_init)) if not reverse else range(len(array_init) - 1, -1, -1):
            if array_init[i]:
                for k in range(array_init[i]):
                    result.append(i)
        return result

    @staticmethod
    # TODO: Метод сортировки Хоара (https://sortvisualizer.com/quicksort/)
    def quick(array, mni=0, mxi=None, alg=lambda x, y: x < y, reverse=False):
        def partition(array, mni, mxi):
            pivot = mni
            for i in range(mni + 1, mxi + 1):
                if alg(array[i], array[mni]) if not reverse else alg(array[mni], array[i]):
                    pivot += 1
                    array[i], array[pivot] = array[pivot], array[i]
            array[pivot], array[mni] = array[mni], array[pivot]
            return pivot

        if mxi is None:
            mxi = len(array) - 1

        if mni >= mxi:
            return
        pivot = partition(array, mni, mxi)
        Sort.quick(array=array, mni=mni, mxi=pivot - 1, alg=alg, reverse=reverse)
        Sort.quick(array=array, mni=pivot + 1, mxi=mxi, alg=alg, reverse=reverse)
        return array


if __name__ == '__main__':
    from timeit import timeit
    from random import randint

    array = [randint(0, 1000) for r in range(10)]
    operations = 100000
    print('\nBubble:')
    print('Before: {}'.format(array))
    print('After: {}'.format(Sort.bubble(array=array[:])))
    print('{} operations per {}'.format(operations, timeit('Sort.bubble({})'.format(array),
                                                           'from __main__ import Sort', number=operations)))
    print('\nShaker:')
    print('Before: {}'.format(array))
    print('After: {}'.format(Sort.shaker(array=array[:])))
    print('{} operations per {}'.format(operations, timeit('Sort.shaker({})'.format(array),
                                                           'from __main__ import Sort', number=operations)))
    print('\nInsertion:')
    print('Before: {}'.format(array))
    print('After: {}'.format(Sort.insertion(array=array[:])))
    print('{} operations per {}'.format(operations, timeit('Sort.insertion({})'.format(array),
                                                           'from __main__ import Sort', number=operations)))
    print('\nCounting:')
    print('Before: {}'.format(array))
    print('After: {}'.format(Sort.counting(array=array[:], reverse=True)))
    print('{} operations per {}'.format(operations, timeit('Sort.counting({})'.format(array),
                                                           'from __main__ import Sort', number=operations)))
    print('\nQuick:')
    print('Before: {}'.format(array))
    print('After: {}'.format(Sort.quick(array=array[:])))
    print('{} operations per {}'.format(operations, timeit('Sort.quick({})'.format(array),
                                                           'from __main__ import Sort', number=operations)))
