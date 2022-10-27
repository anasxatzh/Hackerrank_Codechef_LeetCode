# Pilling - Up:

T = int(input('Enter the number of test cases:'))
blocks = []
for i in range(T):
    n = int(input('Enter the number of cubes:'))
    side_len = list(map(int,input('Enter the length:').split()))
    print(side_len)
    print(len(side_len))

    k = 0
    r = len(side_len) - 1
    
    while k < len(side_len):     
        if side_len[k] > side_len[r]: 
            side_len.pop(k)
            k += 1
        elif side_len[k] < side_len[r]:  
            side_len.pop(r)
            r -= 1
    
