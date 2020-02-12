i = 7
with open("Text.txt", "r", encoding='utf-8') as file:
    TextStr = file.read()
    TextStr = TextStr.lower()
    UpdatedTextStr = ""
    for i in TextStr:
        if((i <= 'a' and i >= 'z') or (i <= 'а' and i >= 'я') or (i == ' ')):
            print(i)
    print(UpdatedTextStr)