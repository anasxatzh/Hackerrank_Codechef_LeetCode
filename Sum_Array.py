

arr = [1,3,5,6,11,23]
sum = 9
def twosum(arr,sum):
    for i in range(len(arr) -1):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j] == sum:
                print('The two numbers are:', arr[i], 'and', arr[j])
##    return arr[i], arr[j]
print(twosum(arr, sum))
