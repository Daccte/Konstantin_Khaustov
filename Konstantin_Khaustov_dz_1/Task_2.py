# Задание №2 вопрос а
numbers_list = []
new_numbers_list = []

for i in range(1, 1001):
    if i % 2 == 1:
        numbers_list.append(i**3)
print('Список кубов нечетных чисел: {}'.format(numbers_list))

for i in range(len(numbers_list[:])):
    new_number = str(numbers_list[i])
    new_list = list(new_number)
    numbers_sum = 0
    for i in range(len(new_list[:])):
        new_list[i] = int(new_list[i])
        numbers_sum += new_list[i]
    if numbers_sum % 7 == 0:
        new_numbers_list.append(new_number)
        print('[Задание 2 вопрос а] Сумма цифр, делящихся на 7: {}'.format(new_number))
print('[Задание 2 вопрос а] Список с числами, сумма цифр которых делится на 7:', new_numbers_list)

#Задание №2 вопрос б
new_numbers_list1 = []

for i in range(len(numbers_list[:])):
    new_numbers_listb = numbers_list[i] + 17
    new_number = str(new_numbers_listb)
    new_list = list(new_number)
    numbers_sum = 0
    for i in range(len(new_list[:])):
        new_list[i] = int(new_list[i])
        numbers_sum += new_list[i]
    if numbers_sum % 7 == 0:
        new_numbers_list1.append(new_number)
        print('[Задание 2 вопрос б] Сумма цифр, делящихся на 7: {}'.format(new_number))
print('[Задание 2 вопрос] Список с числами, сумма цифр которых делится на 7:', new_numbers_list1)
