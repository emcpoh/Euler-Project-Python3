N = int(input("Введите число от 0 до 10000: "))
if 0 <= N <= 10000:
    summa = 0
    for x in range(0, N):
        if x % 3 == 0:
            summa += x
        elif x % 5 == 0:
            summa += x
    print("Сумма всех чисел меньше ", N, " кратных 3 или 5: ", summa)
else:
    N = int(input("Введите число от 0 до 10000: "))


