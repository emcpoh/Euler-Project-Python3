def factorial(n_1: int) -> int:
    factor = 1
    for i in range(1, n_1 + 1):
        factor *= i
    return factor


def number_sum(n_2: int) -> int:
    sum_1 = 0
    list_1 = list(str(n_2))
    for i in range(0, len(list_1)):
        sum_1 += int(list_1[i])
    return sum_1

print('Задание: найдите сумму цифр в числе N! (факториал N).')
N = int(input('Введите число N: '))
print('Сумма цифр факториала числа {} = {}'.format(N, number_sum(factorial(N))))