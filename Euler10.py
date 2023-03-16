def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


print('Задание: Найдите сумму всех простых чисел меньше N.')
n = int(input('Введите N: '))
summa = 0
for j in range(2, n):
    if is_prime(j) is True:
        summa += j
print('Сумма всех простых чисел меньше ' + str(n) + ' =', summa)
