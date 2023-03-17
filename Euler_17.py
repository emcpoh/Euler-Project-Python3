print('Задание: найти количество букв в записи всех чисел от 1 до N включительно')
print('PS: на вход программа может принять число не больше 1000')
dict_1 = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}
dict_11_19 = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
              18: 'eighteen', 19: 'nineteen'}
dict_20_99 = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
              90: 'ninety'}


def for1_10(number1_10):
    return len(dict_1[number1_10])


def for11_19(number11_19):
    return len(dict_11_19[number11_19])


def for20_99(number20_99):
    number20_99 = str(number20_99)
    new_key = int(number20_99[1])
    if number20_99[1] == '0':
        total_len_20_99 = len(dict_20_99[int(number20_99)])
        return total_len_20_99
    elif number20_99[0] == '2':
        total_len_20_99 = len(dict_20_99[20]) + len(dict_1[new_key])
    elif number20_99[0] == '3':
        total_len_20_99 = len(dict_20_99[30]) + len(dict_1[new_key])
    elif number20_99[0] == '4':
        total_len_20_99 = len(dict_20_99[40]) + len(dict_1[new_key])
    elif number20_99[0] == '5':
        total_len_20_99 = len(dict_20_99[50]) + len(dict_1[new_key])
    elif number20_99[0] == '6':
        total_len_20_99 = len(dict_20_99[60]) + len(dict_1[new_key])
    elif number20_99[0] == '7':
        total_len_20_99 = len(dict_20_99[70]) + len(dict_1[new_key])
    elif number20_99[0] == '8':
        total_len_20_99 = len(dict_20_99[80]) + len(dict_1[new_key])
    elif number20_99[0] == '9':
        total_len_20_99 = len(dict_20_99[90]) + len(dict_1[new_key])
    return total_len_20_99


def for100_1000(number100_1000):
    if number100_1000 == 1000:
        total_len_100_1000 = for1_10(1) + len('thousand')
        return total_len_100_1000
    number100_1000 = str(number100_1000)
    total_len_100_1000 = for1_10(int(number100_1000[0])) + len('hundred')
    if 1 <= int(number100_1000[1:]) <= 10:
        total_len_100_1000 += for1_10(int(number100_1000[1:])) + len('and')
    if 11 <= int(number100_1000[1:]) <= 19:
        total_len_100_1000 += for11_19(int(number100_1000[1:])) + len('and')
    if 20 <= int(number100_1000[1:]) <= 99:
        total_len_100_1000 += for20_99(int(number100_1000[1:])) + len('and')
    return total_len_100_1000


def identification(number):
    total_len = 0
    if 1 <= number <= 10:
        total_len = for1_10(number)
    elif 11 <= number <= 19:
        total_len = for11_19(number)
    elif 20 <= number <= 99:
        total_len = for20_99(number)
    elif 100 <= number <= 1000:
        total_len = for100_1000(number)
    return total_len


n = int(input('Введите N: '))
result = 0
for i in range(1, n + 1):
    result += identification(i)
print('Количество букв для записи всех чисел от 1 до {} включительно: '.format(n), result)
