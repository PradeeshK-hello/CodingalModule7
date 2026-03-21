def longestSubarray(arr,arr_size):
    max_len = 1
    curr_len = 1
    for i in range(1, arr_size):
        if (arr[i] % 2 == 0 and arr[i - 1] % 2 != 0) or \
            (arr[i] % 2 != 0 and arr[i - 1] % 2 == 0):
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 1
    return max_len
arr = [10, 12, 14, 7, 8]
arr_size = len(arr)
print("Length of the longest alternating even odd subarray is %d"\
    ,longestSubarray(arr, arr_size))
def oddEvenAlternate(arr,arr_size):
    max_len = 1
    curr_len = 1
    for i in range(1, arr_size):
        if (arr[i] % 2 == 0 and arr[i - 1] % 2 != 0) or \
            (arr[i] % 2 != 0 and arr[i - 1] % 2 == 0):
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 1
    return max_len
arr = [10, 12, 14, 7, 8]
arr_size = len(arr)
print("Length of the longest alternating even odd subarray is %d"\
    ,oddEvenAlternate(arr, arr_size))