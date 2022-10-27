
# Amount of weapons in kids


T = int(input())
for i in range(T):
    n,k = list(map(int, input().split()))
    #minimum amount of weapons of every kid:
    min_weap = k//n
    rest_weap = k%n
    print(min_weap)



    
    kids_list = []
    weap_list = []
    dist_list = []

    for j in range(1,n+1): # kids
        kids_list.append(j)


    for e in range(0,len(kids_list) - rest_weap):
        kids_list[e] = min_weap
        dist_list.append(kids_list[e])
    for l in range(len(kids_list) - rest_weap, len(kids_list) ):
        while (kids_list[l] - kids_list[e] <= 1):
            if rest_weap / (k-n) == 1:
                kids_list[l] = (rest_weap / (k-n)) + min_weap
                dist_list.append(kids_list[l])

            break

  
