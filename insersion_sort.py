def insertion_sort(arr):
    for i in range(1, len(arr)):
        elem = arr[i]
        j = i - 1
        while (j >= 0 and elem < arr[j]):
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = elem


arr = [543, 2, 543, 333, 22, 11, 666, 74]
insertion_sort(arr)
print(arr)
