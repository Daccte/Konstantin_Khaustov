def odd_to_num(a):
    for num in range(1, a+1, 2):
        yield num


odd_to_15 = odd_to_num(15)

print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))

# number = int(input('Введите число: '))
# odd_to_15 = (num for num in range(1, number+1, 2))
#
#
# print(next(odd_to_15))
# print(next(odd_to_15))
# print(next(odd_to_15))
# print(next(odd_to_15))
# print(next(odd_to_15))
# print(next(odd_to_15))
# print(next(odd_to_15))
# print(next(odd_to_15))
# print(next(odd_to_15))
