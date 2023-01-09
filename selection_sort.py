def selection_sort(arr): # сортировка выбором
    index = 0
    while index < len(arr) - 1:
        min_index = index
        j = index + 1
        # поиск номера минимального элемента начиная с номера i до конца списка
        while j < len(arr):
            if arr[j] < arr[min_index]:
                min_index = j
            j = j + 1
        # поменять местами
        arr[index], arr[min_index] = arr[min_index], arr[index]
        index = index + 1


arr = [43, 67, 88, 2, 77, 44, 1243, 66]
selection_sort(arr)
print(arr)
