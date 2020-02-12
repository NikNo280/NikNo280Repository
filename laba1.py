def main():
    print(wordcount("Text.txt"))
    pass


def wordcount(FileName):
    with open(FileName, "r", encoding='utf-8') as file:
        TextStr = file.read()
        file.close()
        TextStr = TextStr.lower()
        UpdatedTextStr = ""
        for i in TextStr:
            if((i <= "я" and i >= "а") or (i == " ") or (i <= "z" and i >= "a") or (i == "-")):
                UpdatedTextStr += i
        ArrStr = UpdatedTextStr.split(" ")
        Key = 0
        Dictionary = dict.fromkeys(['a'])
        Dictionary.clear()
        for i in ArrStr:
            for j in ArrStr:
                if(i == j):
                    Key += 1
            other = {i : Key}
            Dictionary.update(other)
            Key = 0
    return Dictionary

main()