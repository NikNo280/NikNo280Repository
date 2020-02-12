
i = 7
with open("Text.txt", "r", encoding='utf-8') as file:
    TextStr = file.read()
    TextStr = TextStr.lower()
    UpdatedTextStr = ""
    for i in TextStr:
        if((i <= "я" and i >= "а") or (i == " ") or (i <= "z" and i >= "a")):
            UpdatedTextStr += i
    ArrStr = UpdatedTextStr.split(" ")
    Key = 0
    Count = 0
    Dictionary = dict.fromkeys(['a', 'b'])
    Dictionary.clear()
    for i in ArrStr:
        for k in ArrStr:
            if(i == k):
                Key += 1
        other = {[Key, Count] : i}
        Dictionary.update(other)
        Key = 0
    print(Dictionary.keys())
    print(Dictionary.setdefault(1))
    print(Dictionary.keys())