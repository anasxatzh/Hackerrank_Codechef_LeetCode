# sum of 2d array

arr = [[1,2,3], [4,5,6]]

def Sum_Array(arr):
    two_dim_sum = 0

    for i in arr:
        for x in i:
            two_dim_sum += x
    return two_dim_sum
print(Sum_Array(arr))



##arr = [1,3,5,6,11,23]
##sum = 9
##def twosum(arr,sum):
##    for i in range(len(arr) -1):
##        for j in range(i+1, len(arr)):
##            if arr[i]+arr[j] == sum:
##                print('The two numbers are:', arr[i], 'and', arr[j])
####    return arr[i], arr[j]
##print(twosum(arr, sum))
