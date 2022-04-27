from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(a, not_replay=False):
    new_list = []
    i = 1
    for i in range(a):
        random_nouns = choice(nouns)
        random_adverbs = choice(adverbs)
        random_adjectives = choice(adjectives)
        new_str = f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}'
        new_list.append(new_str)
        i += 1
        new_list_2 = []
        if not_replay == True:
            new_list_2 = new_str.split()
            for i in nouns:
                for f in new_list_2:
                    if i == f:
                        nouns.remove(i)
            for i in adverbs:
                for f in new_list_2:
                    if i == f:
                        adverbs.remove(i)
            for i in adjectives:
                for f in new_list_2:
                    if i == f:
                        adjectives.remove(i)
    return new_list

print(get_jokes(5, True))
