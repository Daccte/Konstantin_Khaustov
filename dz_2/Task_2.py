new_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i in range(len(new_list)):
    value = new_list.pop(0)
    if value.isdigit():
        new_list.append('"')
        new_list.append(f'{int(value):02d}')
        new_list.append('"')
    elif (value[0] == '+' or value[0] == '-') and value[1].isdigit():
        new_list.append('"')
        new_list.append(f'+{int(value):02d}')
        new_list.append('"')
    else:
        new_list.append(value)

print(' '.join(new_list))
