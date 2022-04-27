from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(a):
    new_list = []
    i = 1
    for i in range(a):
        new_str = f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}'
        new_list.append(new_str)
        i += 1
    return new_list

print(get_jokes(5))
