bef_arr = [1,2,3,4,5,6,7,8,9]
def reverseArray(arr,arr_size):
    start = 0
    end = arr_size - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
arr = [1,2,3,4,5,6,7,8,9]
arr_size = len(arr)
reverseArray(arr,arr_size)
print("Array", bef_arr)
print("Reversed Array", arr)