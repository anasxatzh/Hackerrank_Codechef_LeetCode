# Lonely Integer

n = int(input())
a = list(map(int,input().split()))

def lonelyinteger(a):
    set_a = set(a) # [1,2,3,4]
    set_a = list(set_a)

    for i in range(len(set_a)):
        count = a.count(set_a[i])
        print('Number {} appears {} times in the list'.format(set_a[i],count))

        if count == 1:
            print(set_a[i])
print(lonelyinteger(a))
