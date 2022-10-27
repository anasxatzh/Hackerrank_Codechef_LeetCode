# Chef and Sub-Arrays



T = int(input())
for i in range(T):
    n = int(input())
    A = list(map(int, input().split())) # [4,1,2,1]

    sub_arr = []
    count = 0
    prod_A = 1
    for i in A:
        sub_arr.append(i) # [1], [1,2], [1,2,2], [1,2,2,2], [1,2,2,2,2], [1,2,2,2,2,1]
        sub_arr_set = set(sub_arr)
        count = len(sub_arr_set)  # 2
    for i in range(len(A)-1):
        prod_A *= A[i]
    if sum(A) == prod_A:
        count += 1

    sum_sub = sub_arr[0] # 1
    prod_sub = sub_arr[0] # 1


    if len(sub_arr) > 1: # [1,2], [1,2,2], [1,2,2,2], [1,2,2,2,2], [1,2,2,2,2,1]
        for j in range(1,len(sub_arr)):
            sum_sub += sub_arr[j]
            prod_sub *= sub_arr[j]
##            print(sum_sub)
##            print(prod_sub)
            
            if sum_sub == prod_sub:
                count += 1
    print(count)
