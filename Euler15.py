def num_of_routes(m, n):
    m = m + 1
    n = n + 1
    num_routes = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        num_routes[i][1] = 1
    for j in range(1, n + 1):
        num_routes[1][j] = 1
    for i in range(2, m + 1):
        for j in range(2, n + 1):
            num_routes[i][j] = num_routes[i - 1][j] + num_routes[i][j - 1]
    return num_routes[m][n]


print('Задание: найти количество маршрутов перемещения по сетке размером M x N блоков, при условии, '
      'что двигаться можно только вниз и вправо.')
m_side, n_side = 20, 20  # Grid sizes
routes = num_of_routes(m_side, n_side)
print("Количество маршрутов в сетке {}x{} элементов: {}".format(m_side, n_side, routes))
