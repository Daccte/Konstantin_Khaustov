new_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
            'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in range(len(new_list)):
    new_list_1 = new_list.pop(0)
    index_for_name = new_list_1.rfind(' ')
    print('Hello, {}!'.format(new_list_1[index_for_name:].title()))
