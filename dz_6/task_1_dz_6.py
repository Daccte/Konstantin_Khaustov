def parse_file(path_file):
    if path_file:
        with open(path_file, "r", encoding="utf-8") as file:
            for line in file:
                ip = line.split(" - - ")[0]
                method_and_path = line.split('"')[1]
                method = method_and_path.split()[0]
                path = method_and_path.split()[1]
                yield ip, method, path

file = parse_file("./nginx_logs.txt")
for i in file:
    print(i)
