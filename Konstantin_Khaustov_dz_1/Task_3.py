for i in range(1, 101):
    if i % 5 == 0 or i % 10 == 0 or i == 11 or i == 12 or i == 13 or i == 14:
        print(f'{i} процентов')
    elif i % 10 == 6 or i % 10 == 7 or i % 10 == 8 or i % 10 == 9:
        print(f'{i} процентов')
    elif i == 1 or i % 10 == 1:
        print(f'{i} процент')
    elif i % 10 == 2 or i % 10 == 3 or i % 10 == 4:
        print(f'{i} процента')
