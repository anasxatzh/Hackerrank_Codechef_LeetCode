# Plus_Minus

n = int(input())
arr = list(map(int,input().split()))
pos = []
neg = []
zer = []
  


def plusMinus(arr):
    for i in range(len(arr)):     
        if arr[i]>0:
            pos.append(arr[i])          
        if arr[i] == 0:
            zer.append(arr[i])           
        if arr[i] < 0:
            neg.append(arr[i])
    print('{:.6f}'.format(len(pos) / len(arr)) )
    print('{:.6f}'.format(len(neg) / len(arr)) )
    print('{:.6f}'.format(len(zer) / len(arr)) )
print(plusMinus(arr))
    
   
