print('Задание: Найдите произведение a*b*c, для которой (a**2 + b**2 = c**2) и (a + b + c = 1000)')
def pifagor():
    for i in range(1, 500):
        for j in range(1, 500):
                a, b = i, j
                c = ((a ** 2) + (b ** 2)) ** 0.5
                if not (a + b + c == 1000 and (a ** 2) + (b ** 2) == (c ** 2)):
                    continue
                else:
                    new_list = [int(a), int(b), int(c), int(a*b*c)]
                    return new_list


result_list = pifagor()
print('a =', result_list[0],
      '\nb =', result_list[1],
      '\nc =', result_list[2],
      '\na * b * c =', result_list[3])
