price = [40, 56.67, 10.54, 30, 98, 1.04, 38.86, 39, 12, 23.04, 45.87, 87.76, ]
print(id(price))
price.sort()
print(id(price))
for i in range(len(price)):
    new_price = price.pop(0)
    if new_price % 1 == 0:
        print(f'{new_price} руб 00 коп')
    elif new_price % 1 != 0:
        new_price_1 = int((round((new_price % 1), 2) * 100))
        print(f'{int(new_price // 1)} руб {round(new_price_1, 2):02d} коп')
