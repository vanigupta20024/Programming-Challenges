def insert(arr, n):
    i = n
    temp = arr[n]
    while i > 0 and temp > arr[i//2]:
        arr[i] = arr[i//2]
        i = i//2
    arr[i] = temp

def createHeap():
    arr = [10,20,30,25,5,40,35]
    for i in range(len(arr)):
        insert(arr, i)
        print(arr)
    
createHeap()
