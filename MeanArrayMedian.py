def arrayMean(arr,arr_size):
    total_sum = 0
    for i in range(0, arr_size):
        total_sum += arr[i]
    return int(total_sum/arr_size)
def arrayMedian(arr,arr_size):
    sorted(arr)
    if arr_size % 2 != 0:
        return int(arr[int(arr_size/2)])
    return int((arr[int((arr_size-1)/2)] + arr[int(arr_size/2)])/2.0)
arr = [2,3,1,6,7,9,5,4,8]
arr_size = len(arr)
print("Mean =", arrayMean(arr,arr_size))
print("Median =", arrayMedian(arr,arr_size))