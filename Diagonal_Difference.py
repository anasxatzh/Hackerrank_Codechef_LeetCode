# Diagonal Difference


n = int(input().strip())
arr = []
for i in range(n):
    r = list(map(int,input().split()))
    arr.append(r)

def diagonalDifference(arr):
    first_sum = 0
    second_sum = 0
    for i in range(len(arr)): # 3
        for j in range(len(arr[i])): # 3
            if i == j:
                first_sum += arr[i][j]
    for i in range(len(arr)-1, -1, -1): #  4 3 2 1 0
        for j in range( len(arr[i])-1-i , len(arr[i]) - 2 -i, -1 ): # 0 1 2 3 4
            second_sum += arr[i][j]
            
    res = abs(first_sum-second_sum)
    return res

print(diagonalDifference(arr))


##
