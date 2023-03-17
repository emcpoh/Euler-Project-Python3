print('Задание: найти сумму цифр числа 2^N')
n = int(input('Введите N: '))
num = str(2 ** n)
length = len(num)
summa = 0
for i in range(0, length):
    summa += int(num[i])
print("Сумма цифр числа 2^{}: {}".format(n, summa))
