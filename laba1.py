import random

def main():
    with open("Number.txt", "r", encoding='utf-8') as file:
        NumberStr = file.read()
        ArrNumberStr = NumberStr.split(" ")
        array = [29, 19, 47, 11, 6, 19, 24, 12, 17, 23, 11, 71, 41, 36, 71, 13, 18, 32, 26]
    ArrNumber = [int(item) for item in ArrNumberStr]
    print(ArrNumber)
    quick_sort(ArrNumber)
    print(ArrNumber)

    WordCount("Text.txt")

    for fib in fibonacci(20):
        print(fib, end = " ")
    print()
    pass


def WordCount(FileName):
    with open(FileName, "r", encoding='utf-8') as file:
        TextStr = file.read()
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


def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1

    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot - 1)
        _quicksort(array, pivot + 1, end)

    return _quicksort(array, begin, end)

def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot

main()