print('Задание: Какое самое маленькое число делится нацело на все числа от 1 до N?')
n = int(input("Введите N: "))
chisla = [i for i in range(1, n+1)]  # поместил числа от 0 до N в список, для удобства перебора
j = n
flag = True
while flag is True:
    schet = 0
    j += 1
    for i in chisla:
        if j % i == 0:
            schet += 1
            if schet == n:
                print('Наименьшее число, которое делится нацело на все числа от 1 до', n, '=',j)
                flag = False
        elif j % i != 0:
            break
