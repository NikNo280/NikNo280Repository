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
        SetOfWords = ""
        for i in range(0, 10):
            max_values = max(Dictionary.keys())
            SetOfWords += Dictionary.pop(max_values) + " "
    return SetOfWords

main()