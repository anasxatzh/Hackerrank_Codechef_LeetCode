# Tower Breakers

r = list(map(int,input().split()))
n = int(r[0]) # the number of towers
m = int(r[1]) # the height of each tower

ans = ''
def towerbreakers(n,m):
    if m == 1:
        ans = '2'
    else: # m>1   
        if n == 1:
            ans = '1'
        else: # n>1
            if n%2 == 0:
                ans = '2'
            else:
                ans = '1'

    return ans  
        
print(towerbreakers(n,m))       
