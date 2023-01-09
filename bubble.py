def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr) - 1): # начинаем с номер i, т.к. передыдущий кусок уже отсортирован
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] #обмен значений переменных


arr = [654, 3, 654, 234, 765432, 345]
bubble_sort(arr)
print(arr)
