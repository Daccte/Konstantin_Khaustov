import os

directory = r'.'
my_list = [1000, 10000, 100000, 1000000]
result = dict.fromkeys(my_list, 0)

for path_top, path_bot, files in os.walk(directory):
    for file in files:
        path = os.path.join(path_top, file)
        size = os.path.getsize(path)
        to_group = min(filter(lambda x: size < x, my_list))
        result[to_group] += 1

print(result)
