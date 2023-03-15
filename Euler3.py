print('Задание: Каков самый большой делитель заданного числа, являющийся простым числом?')
num = int(input("Введите число: "))


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


for j in range(num//2, 1, -1):
    if num % j == 0 and is_prime(j):
        print("Самый большой делитель, являющийся простым числом:", j)
        break
else:
    print("Введенное число является простым числом, либо не имеет делителей-простых чисел")
