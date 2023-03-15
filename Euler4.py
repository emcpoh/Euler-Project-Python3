#Написано для поиска максимального палиндрома среди произведений трехзначных чисел. Для другой конфигурации необходимо править код.
maxpall = 0
for i in range(100,1000):
    for j in range(100,1000):
        multipl = str(i*j)
        if (multipl[0] == multipl[-1]) and (multipl[1] == multipl[-2]):
            if len(multipl) == 5:
                pall = multipl
            if len(multipl) == 6:
                if multipl[2] == multipl[-3]:
                    pall = multipl
            if maxpall < int(pall):
                maxpall = int(pall)
        continue
print('Максимальное число-палиндром среди суммы произведений трехзначных чисел =',maxpall)