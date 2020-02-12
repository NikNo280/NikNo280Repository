def main():
    WordCount("Text.txt")
    for fib in fibonacci(20):
        print(fib, end = " ")
    print()
    pass


def WordCount(FileName):
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
            if (i != ""):
                for j in ArrStr:
                    if(i == j):
                        Key += 1
                other = {i: Key}
                Dictionary.update(other)
                Key = 0
        print(Dictionary)
        EndStr = ""
        for i in range(0, 10):
            MaxValue = max(Dictionary.values())
            for j in Dictionary.items():
                if(j[1] == MaxValue):
                    EndStr += j[0] + " "
                    Dictionary.pop(j[0])
                    break
        print(EndStr)
    pass


def fibonacci(n):
    fib1 = 0
    fib2 = 1
    for i in range(n):
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        yield fib1

main()