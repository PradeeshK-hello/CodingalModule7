def minElement(a,size):
    temp = a[0]
    for i in range(1,size):
        temp = min(temp,a[i])
    return temp
def maxElement(a,size):
    temp = a[0]
    for i in range(1,size):
        temp = max(temp,a[i])
    return temp
a = [2,4,5,6,8,1,3,7,9]
size = len(a)
print("Minimum element of array:",minElement(a,size))
print("Maximum element of array:",maxElement(a,size))