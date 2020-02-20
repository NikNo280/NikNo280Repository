import sys
import argparse


def main():
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    if (namespace.number_func == 1):
        word_count(namespace.argument)
    elif (namespace.number_func == 2):
        quick_sort(namespace.argument)
    elif (namespace.number_func == 3):
        merge_sort(namespace.argument)
    elif (namespace.number_func == 4):
        fibonacci_factory(int(namespace.argument))
    else:
        print("Такой функции нет")
    pass


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('number_func', type=int)
    parser.add_argument('argument')
    return parser


def word_count(file_name):
    with open(file_name, "r", encoding='utf-8') as file:
        text_str = file.read()
        text_str = text_str.lower()
        updated_text_str = ""
        for i in text_str:
            if ((i <= "я" and i >= "а") or (i == " ") or (i <= "z" and i >= "a") or (i == "-")):
                updated_text_str += i
        arr_str = updated_text_str.split(" ")
        key = 0
        dictionary = dict.fromkeys(['a'])
        dictionary.clear()
        for i in arr_str:
            if (i != ""):
                for j in arr_str:
                    if (i == j):
                        key += 1
                other = {i: key}
                dictionary.update(other)
                key = 0
        print(dictionary)
        end_str = ""
        for i in range(0, 10):
            max_value = max(dictionary.values())
            for j in dictionary.items():
                if (j[1] == max_value):
                    end_str += j[0] + " "
                    dictionary.pop(j[0])
                    break
        print(end_str)
    pass


def fibonacci(n):
    fib1 = 0
    fib2 = 1
    for i in range(n):
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        yield fib1


def fibonacci_factory(n):
    for fib in fibonacci(n):
        print(fib, end=" ")


def algoritm_quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1

    def quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        quicksort(array, begin, pivot - 1)
        quicksort(array, pivot + 1, end)

    return quicksort(array, begin, end)


def partition(array, begin, end):
    pivot = begin
    for i in range(begin + 1, end + 1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def quick_sort(file_name):
    with open(file_name, "r", encoding='utf-8') as file:
        number_str = file.read()
    arr_number_str = number_str.split(" ")
    arr_number = [int(item) for item in arr_number_str]
    print(arr_number)
    algoritm_quick_sort(arr_number)
    print(arr_number)
    pass


def algoritm_merge_sort(array):
    if len(array) < 2:
        return array
    else:
        middle = int(len(array) / 2)
        left = algoritm_merge_sort(array[:middle])
        right = algoritm_merge_sort(array[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if (left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def merge_sort(file_name):
    with open(file_name, "r", encoding='utf-8') as file:
        number_str = file.read()
    arr_number_str = number_str.split(" ")
    arr_number = [int(item) for item in arr_number_str]
    print(arr_number)
    print(algoritm_merge_sort(arr_number))
    pass


main()
