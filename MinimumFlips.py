def minFlips(arr,arr_size):
    flip_count = 0
    for i in range(0,arr_size):
        if arr[i] == 0:
            flip_count += 0
        if arr[i-1] == 1 and arr[i] == 1:
            print("From index",i-1,"to",i)
            flip_count += 1
    print("Minimum number of flips:",flip_count)
arr = [0,1,1,0,0,0,1,1]
arr_size = len(arr)
minFlips(arr,arr_size)