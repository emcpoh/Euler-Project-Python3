print('Задание: Найдите первые десять цифр суммы следующих ста 50-значных чисел.'
      '\nЧисла указаны построчно в файле chisla.txt. ')
file = open('chisla.txt')
summa = 0
for line in file:
    summa += (int(line))
summa = str(summa)
print('Первые десять цифр суммы чисел из файла —', summa[0:10])
file.close()
