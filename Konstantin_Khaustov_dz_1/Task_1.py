duration = int(input('Введите число: '))

if duration < 60:
    print(f'{duration} сек')
elif 60 <= duration < 3600:
    dur_1 = duration // 60
    dur_2 = duration % 60
    print(f'{dur_1} мин {dur_2} сек')
elif 3600 <= duration < 86400:
    dur_1 = duration // 3600
    dur_2 = ((duration % 3600) // 60)
    dur_3 = ((duration % 3600) % 60)
    print(f'{dur_1} час {dur_2} мин {dur_3} сек')
elif duration >= 86400:
    dur_1 = duration // 86400
    dur_2 = (duration % 86400) // 3600
    dur_3 = ((duration % 86400) % 3600) // 60
    dur_4 = ((duration % 86400) % 3600) % 60
    print(f'{dur_1} д {dur_2} час {dur_3} мин {dur_4} сек')
