def treug(num_1):
    chislo = 0
    i = 1
    while i <= num_1:
        chislo += i
        i += 1
    return chislo


def proverka_odnogo(num_2):
    j = 0
    for i in range(1, num_2 + 1):
        if num_2 % i == 0:
            j += 1
    return j


def srav(num_3):
    j = 0
    i = 1
    while num_3 > j:
        j = proverka_odnogo(treug(i))
        i += 1
    return treug(i-1)


print('Задание: найти первое треугольное число, у которого более пятисот делителей.\n'
      'В качестве примера, предлагаю ознакомиться с решением задачи для 200 делителей, поскольку\n'
      'решение для 500 делителей занимает большое количество и без того отсутствующего ценного времени.')
print(srav(200))  # If u need to change the original number of divisors, you can do it here.
