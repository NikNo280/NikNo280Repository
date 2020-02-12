i = 7
with open("Text.txt", "r", encoding='utf-8') as file:
    TextStr = file.read()
    TextStr = TextStr.lower()
    UpdatedTextStr = ""
    for i in TextStr:
        if((i <= "я" and i >= "а") or (i == " ") or (i <= "z" and i >= "a")):
            UpdatedTextStr += i
    ArrStr = UpdatedTextStr.split(" ")
    print(ArrStr)