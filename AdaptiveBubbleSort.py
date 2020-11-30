'''
If list is already sorted, takes O(n) to execute.
'''

def bubble_sort(arr):
  for i in range(len(arr)):
    flag = 0
    for j in range(0, len(arr) - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        flag = 1
    if flag == 0:
      break
  return arr
