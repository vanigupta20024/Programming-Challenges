def partition(a, p, r):
    i = p
    for j in range(p, r):
        if a[j] <= a[r]:
            a[j], a[i] = a[i], a[j]
            i += 1
    a[i], a[r] = a[r], a[i]
    return i
    
def quick_sort(a, l, h):
    if l < h:
        q = partition(a, l, h)
        quick_sort(a, l, q - 1)
        quick_sort(a, q + 1, h)
        
    return a
    
    
a = [5,6,8,3,7,1,10,9,35,12]
print(quick_sort(a, 0, len(a) - 1))
