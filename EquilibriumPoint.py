def equilibriumPoint(arr):
    left_sum = 0
    right_sum = 0
    n = len(arr)
    for i in range(n):
        left_sum = 0
        right_sum = 0
        for j in range(i):
            left_sum += arr[j]
        for j in range(i+1,n):
            right_sum += j
        if left_sum == right_sum:
            return i
    return -1
arr = [-4,6,2,0,0,1,1]
print("Element:",arr[equilibriumPoint(arr)])