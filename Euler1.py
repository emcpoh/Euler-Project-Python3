def newsum(n:int):
    summa = 0
    for x in range(0, n):
        if x % 3 == 0:
            summa += x
        elif x % 5 == 0:
            summa += x
    print("Сумма всех чисел меньше ", n, " кратных 3 или 5: ", summa)
num = int(input("Введите число от 0 до 10000: "))
flag = False
while flag != True:
    if 0 <= num <= 10000:
        newsum(num)
        flag = True
    else:
        num = int(input("Вы указали неверное число, попробуйте снова:  "))
#New commit check
