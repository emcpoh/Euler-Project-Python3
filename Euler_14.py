def collatz_len(n):
    new_list = [n]
    while n != 1:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(3 * n + 1)
        new_list.append(n)
    return len(new_list)


def maximum(m):
    maxim = 0
    max_index = 0
    for i in range(1, m + 1):
        if collatz_len(i) > maxim:
            maxim = collatz_len(i)
            max_index = i
    result = max_index, maxim
    return result


N_1 = 1000000
print('Задание: Какой начальный элемент меньше миллиона (N) генерирует самую длинную последовательность Коллатца?')
print('В случае, когда начальный элемент =', maximum(N_1)[0], ', последовательность Коллатца имеет наибольшую длину, равную', maximum(N_1)[1], 'элементов.')
