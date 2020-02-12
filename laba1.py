with open("Text.txt", "r", encoding='utf-8') as file:
    line = file.readline()
    while line:
        print(line, end="")
        line = file.readline()