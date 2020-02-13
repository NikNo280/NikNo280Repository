import sys


def main():
    if len(sys.argv) > 2:
        if (sys.argv[1] == "1"):
            WordCount(sys.argv[2])
        elif (sys.argv[1] == "2"):
            QuickSort(sys.argv[2])
        elif (sys.argv[1] == "3"):
            FibonacciFactory(int(sys.argv[2]))
    else:
        print("Такой функции нет")
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


def Fibonacci(n):
    fib1 = 0
    fib2 = 1
    for i in range(n):
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        yield fib1

def FibonacciFactory(n):
    for fib in Fibonacci(n):
        print(fib, end = " ")
    print()

def AlgorithmQuickSort(array, begin=0, end=None):
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

def QuickSort(FileName):
    with open(FileName, "r", encoding='utf-8') as file:
        NumberStr = file.read()
    ArrNumberStr = NumberStr.split(" ")
    ArrNumber = [int(item) for item in ArrNumberStr]
    print(ArrNumber)
    AlgorithmQuickSort(ArrNumber)
    print(ArrNumber)
    pass


main()