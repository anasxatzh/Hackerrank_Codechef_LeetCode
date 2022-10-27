
# Mini-Max-Sum

arr = list(map(int,input().split()))
print(arr)

def miniMaxSum(arr):
    maximum = max(arr)
    minimum = min(arr)
    # to find the maximum sum:
    # we have to extract the minimum element of the array
    arr.remove(minimum)
    # we have to create a new list
    print(arr)
    # so we say:
    maximum_sum = sum(arr)

    arr.append(minimum)
    arr.remove(maximum)
    print(arr)
    minimum_sum = sum(arr)

    print(minimum_sum, end = ' ')
    print(maximum_sum)
    
print(miniMaxSum(arr))    

