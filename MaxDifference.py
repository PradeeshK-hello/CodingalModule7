def maxDifference(a,max_a,min_a,largest_dif):
    max_a = max(a)
    min_a = min(a)
    largest_dif = max_a - min_a
    print(a)
    print("Largest difference is",max_a,"-",min_a,"=",largest_dif)
a = [64,65,131,139,147,166,857]
max_a = max(a)
min_a = min(a)
largest_dif = max_a - min_a
maxDifference(a,max_a,min_a,largest_dif)