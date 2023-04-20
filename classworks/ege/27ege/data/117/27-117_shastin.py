'''
Автор: Л. Шастин.

Дана последовательность N целых чисел.
Назовём "граничными" одинаковые несоседние числа.
Рассматриваются все подпоследовательности исходной последовательности
с ненулевой суммой элементов, кратной D, расположенные меж двух "граничных" чисел.
Примечание: искомые подпоследовательности могут включать себя и другие "граничные"
числа, но обязаны быть открыты и закрыты "граничными" элементами.
Найти количество таких подпоследовательностей.
Пример входных данных (N = 8; D = 2):
6 2
4
2
4
3
5
4
Ответ: 3.
Пояснение для примера: взяли подпоследовательности
- (2), она кратна D = 2 и стоит между двумя "граничными" четвёрками;
- (3 + 5 = 8), она кратна D = 2 и стоит между "граничными" четвёрками;
- (2 + 4 + 3 + 5 = 14), кратна D = 2 и расположена между четвёрками.
Нашлось три подходящих подпоследовательности.
'''

F = open('27-117a.txt')
N, D = map(int, F.readline().split())
A = [int(x) for x in F]
count = 0
for i in range(N):
    s = A[i]
    for j in range(i + 1, N):
        s += A[j]
        if A[i] == A[j] and (s - A[i] - A[j])%D == 0 and s-A[i]-A[j]:
            count += 1
print(count)
F.close()

F = open('27-117b.txt')
N, D = map(int, F.readline().split())
k = {}
count, s, l = 0, 0, -1
for i in range(N):
    x = int(F.readline())
    s += x
    if x in k:
        count += k[x][(s-x)%D] - (x == l)
        k[x][s%D] += 1
    else:
        k[x] = [0]*D
        k[x][s%D] += 1
    l = x
print(count)
F.close()

