number = input('Введите число от 1 до 10 на английском языке: ')

all_number = {'one': 'один',
              'two': 'два',
              'three': 'три',
              'four': 'четыре',
              'five': 'пять',
              'six': 'шесть',
              'seven': 'семь',
              'eight': 'восемь',
              'nine': 'девять',
              'ten': 'десять'
              }

def num_translate(number):
    if number.istitle() == True:
        first_number = number.lower()
        my_number = str(all_number.get(first_number))
        print(my_number.title())
    elif number:
        print(all_number.get(number))
    else:
        print(None)

num_translate(number)

# def num_translate(number):
#     if number == 'one':
#         print('один')
#     elif number == 'One':
#         print('Один')
#     elif number == 'two':
#         print('два')
#     elif number == 'Two':
#         print('Два')
#     elif number == 'three':
#         print('три')
#     elif number == 'Three':
#         print('Три')
#     elif number == 'four':
#         print('четыре')
#     elif number == 'Four':
#         print('Четыре')
#     elif number == 'five':
#         print('пять')
#     elif number == 'Five':
#         print('Пять')
#     elif number == 'six':
#         print('шесть')
#     elif number == 'Six':
#         print('Шесть')
#     elif number == 'seven':
#         print('семь')
#     elif number == 'Seven':
#         print('Cемь')
#     elif number == 'eight':
#         print('восемь')
#     elif number == 'Eight':
#         print('Восемь')
#     elif number == 'nine':
#         print('девять')
#     elif number == 'Nine':
#         print('Девять')
#     elif number == 'ten':
#         print('десять')
#     elif number == 'Ten':
#         print('Десять')
#     else:
#         print(None)
#
# num_translate(number)
