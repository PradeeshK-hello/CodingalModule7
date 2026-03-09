def missingNumber(arr,arr_size):
    total_sum = 0
    for i in range(0, arr_size):
        total_sum += arr[i]
    return int((arr_size + 1) * (arr_size + 2) / 2 - total_sum)
arr = [1,2,3,5]
arr_size = len(arr)
print("Array:",arr)
print("Missing Number:",missingNumber(arr,arr_size))