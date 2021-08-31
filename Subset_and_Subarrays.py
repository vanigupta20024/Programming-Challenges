'''
subsets and subarrays
subarrays:
    a = [10,20,30]
    => [
        [10], [20], [30]
        [10,20], [10,20,30], [20,30],
    ]
subsets:
    a = [10,20,30]
    => [
        [], [10,20,30]
        [10], [20], [30], [10, 20], [10, 30], [20, 30]
    ]
'''
def print_subsets(a):
    limit = 2 ** len(a)
    for i in range(limit):
        for j in range(len(a)):
            if(i & (1 << j) > 0):
                print(a[j], end=" ")
        print()
    
def print_subarray(a):
    for i in range(len(a)):
        for j in range(i, len(a)):
            for k in range(i, j+1):
                print(a[k], end=" ")
            print()
        
print_subsets([10,20,30])
print_subarray([10,20,30])
