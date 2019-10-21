import time


def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_array = array[:mid]
        right_array = array[mid:]

        merge_sort(left_array)
        merge_sort(right_array)
        #######################
        i = 0
        j = 0
        k = 0

        while i < len(left_array) and j < len(right_array):
            if left_array[i] <= right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1

        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1


def print_merge(array):
    print("Merge Sort")
    for i in range(len(array)):
        print(array[i])


def bubble(array):
    counter = 0
    swap = 0
    start_time = time.time()
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            counter += 1
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swap += 1
    print("Bubble Sort")
    print("time", start_time)
    print("counter", counter)
    print("swap", swap)
    for i in range(len(array)):
        print(array[i])
