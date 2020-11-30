def selection_sort(arr):
    for i in range(len(arr)):
        k = i
        for j in range(i, len(arr)):
            if arr[j] < arr[k]:
                k = j
        arr[i], arr[k] = arr[k], arr[i]
    print(arr)
