
i = 7
with open("Text.txt", "r", encoding='utf-8') as file:
    TextStr = file.read()
    TextStr = TextStr.lower()
    UpdatedTextStr = ""
    for i in TextStr:
        if((i <= "я" and i >= "а") or (i == " ") or (i <= "z" and i >= "a") or (i == "-")):
            UpdatedTextStr += i
    ArrStr = UpdatedTextStr.split(" ")
    Key = 0
    Dictionary = dict.fromkeys(['a', 'b'])
    Dictionary.clear()
    for i in ArrStr:
        if(i != ""):
            for k in ArrStr:
                if (i == k):
                    Key += 1
            other = {Key: i}
            Dictionary.update(other)
            Key = 0
    print(Dictionary)
    print(Dictionary.setdefault(10))
    for i in range(1, 10):
        max_values = max(Dictionary.keys())

        print(Dictionary.pop(max_values))
