i = 7
with open("Text.txt", "r", encoding='utf-8') as file:
    line = file.readline()
    d = dict.fromkeys(line, i)
    i += 1
    while line:
        other = {i: line}
        d.update(other)
        i = i + 1
        print(line, end="")
        line = file.readline()
print(d.values())