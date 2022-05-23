import os

with open('Config/config.yaml', 'r', encoding='utf-8') as f:
    file = f.readline().replace('\n', '').split()
    os.makedirs(file[0], exist_ok=True)
    os.chdir(file[0])

    for line in f:
        new_line = line.replace('\n', '').split(' ')

        for i in range(len(new_line)):

            if new_line[0].find('\\') == -1:

                if i > 0:
                    new_path = os.path.join(new_line[0], new_line[i])
                    os.makedirs(new_line[0], exist_ok=True)
                    with open(new_path, 'a', encoding='utf-8') as file:
                        file.write(new_path)

            elif new_line[0].find('\\') != -1:
                new_file = new_line[0].split('\\')

                for _ in range(len(new_line)):
                    print(_)

                    if _ > 0:
                        new_d = os.path.join(new_file[0], new_file[1], new_file[2])
                        os.makedirs(new_d, exist_ok=True)
                        with open(f'{new_d}/{new_line[_]}', 'w', encoding='utf-8') as f:
                            f.write(new_line[_])
