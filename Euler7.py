def is_prime(num_0):
    if num_0 < 2:
        return False
    for i in range(2, int(num_0 ** 0.5) + 1):
        if num_0 % i == 0:
            return False
    return True


def nth_prime(num_1):
    count = 0
    num_2 = 2
    while True:
        if is_prime(num_2):
            count += 1
            if count == num_1:
                return num_2
        num_2 += 1


print("Задание: Найти, какое число является N-м простым числом")
n = int(input("Введите N: "))
print(str(n)+"-е просто число =", nth_prime(n))
