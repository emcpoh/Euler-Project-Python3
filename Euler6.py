def summa_kvadratov(sk_range):
    summa_1 = 0
    for i in sk_range:
        summa_1 += i**2
    return summa_1


def kvadrat_summi(ks_range):
    summa_2 = 0
    for i in ks_range:
        summa_2 += i
    return summa_2 ** 2


print('Задание: Найдите разность между суммой квадратов и квадратом суммы первых N натуральных чисел.')
n = int(input('Введите N: '))
actual_range = range(1, n+1)
print(abs(summa_kvadratov(actual_range) - kvadrat_summi(actual_range)))
