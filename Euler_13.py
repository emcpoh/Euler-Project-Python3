print('Задание: Найдите первые десять цифр суммы следующих ста 50-значных чисел.'
      '\nЧисла указаны построчно в файле chisla.txt. ')
file = open('chisla.txt') #To run the program, you need to place the file chisla.txt in the same directory as the file with the code.
#File chisla.txt it is located in the repository with the main code. Or, it can be found at the link below:
#https://github.com/emcpoh/Euler-Project-Python3/blob/cd341fee297ea2097e03a1e6f3a31dfbde82780b/chisla.txt
summa = 0
for line in file:
    summa += (int(line))
summa = str(summa)
print('Первые десять цифр суммы чисел из файла —', summa[0:10])
file.close()
