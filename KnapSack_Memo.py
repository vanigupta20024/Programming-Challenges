# 0-1 Knapsack DP(Recursive & Memoization)
def memo_knapsack():
    
    def helper(W, wt, val, n):
        # base case, smallest valid input
        # if no elements or capacity of knapsack is 0
        if n == 0 or W == 0:
            return 0
        
        # memoized result
        if mat[W - 1][n - 1] != -1:
            return mat[W - 1][n - 1]
        
        # if we have the possibiloty to choose or not to choose the element
        # MAXimize profit from our CHOICE
        if (W >= wt[n - 1]):
            mat[W - 1][n - 1] = max(val[n - 1] + helper(W - wt[n - 1], wt[:n - 1], val[:n - 1], n - 1),
            helper(W, wt[:n - 1], val[:n - 1], n - 1))
            return mat[W - 1][n - 1]
        # weight of the element exceeds current capacity of knapsack
        else:
            mat[W - 1][n - 1] = helper(W, wt[:n - 1], val[:n - 1], n - 1)
            return mat[W - 1][n - 1]
    
    
    values = [360, 83, 59, 130, 431, 67, 230, 52, 93, 125, 670, 892, 600, 38, 48, 147,
    78, 256, 63, 17, 120, 164, 432, 35, 92, 110, 22, 42, 50, 323, 514, 28,
    87, 73, 78, 15, 26, 78, 210, 36, 85, 189, 274, 43, 33, 10, 19, 389, 276, 312]
    
    weights = [7, 0, 30, 22, 80, 94, 11, 81, 70, 64, 59, 18, 0, 36, 3, 8, 15, 42, 9, 0,
    42, 47, 52, 32, 26, 48, 55, 6, 29, 84, 2, 4, 18, 56, 7, 29, 93, 44, 71,
    3, 86, 66, 31, 65, 0, 79, 20, 65, 52, 13]
    
    knapsack_capacity = 850
    
    n = len(weights)
    
    mat = []
    for i in range(knapsack_capacity):
        temp = []
        for j in range(n):
            temp.append(-1)
        mat.append(temp)
    
    return helper(knapsack_capacity, weights, values, n)


print(memo_knapsack())
