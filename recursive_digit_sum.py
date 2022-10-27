# Recursive Digit Sum

def superDigit(p):
    count = 0
    new_p = 0

    if len(p) == 1:
        new_p = p
        return new_p

    else:

        for i in p:
            new_p = sum([int(i)])
            new_p = str(new_p)
            return new_p
##        for i in range(len(p)): # 7
##            p_con = int(p[i]) 
##            count += p_con # 39 int
##
##
##        for j in range(len(str(count))): # 2
##            count_con = int(str(count)[j])
##
##            new_p += count_con
##
##            if len(str(new_p)) ==   1  :
##                break

                    

n,k = list(map(int,input().split()))
n = str(n)
p = n*k
print(superDigit(p))

