# Counting Sort

n = int(input().strip()) # 7

arr = list(map(int,input().split())) # 1 3 6 2 4 4 7
new_arr = [0]*(max(arr)+1)# [0,0,0,0]
print(new_arr)

def countingSort(arr):
    for i in range(len(arr)): # 0 1 2
        for idx in range(max(arr)+1):    
            if arr[i] == idx:
                new_arr[arr[i]] += 1
                          
    return new_arr

print(countingSort(arr))



##n = int(input())
##arr = list(map(int,input().split()))
##new_arr = [0]*(max(arr)+1)
##
##for i in range(n):
##    temp = arr[i]
##    new_arr[temp] += 1
##print(new_arr, sep = ' ')
