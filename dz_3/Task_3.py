def thesaurus(*args):
    new_dict = {}
    for name in args:
        key = name[0]
        if key not in new_dict:
            new_dict[key] = []
        new_dict[key].append(name)
    print(new_dict)

thesaurus('Иван', 'Мария', 'Петр', 'Илья', 'Марина')
