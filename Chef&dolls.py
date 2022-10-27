# CODECHEF : Chef and Dolls



list_dolls = []
for i in range(int(input())):
    occ = {}
    for i in range(int(input('Enter the number of dolls:'))):
        types = input().splitlines()
        result = [list_dolls.append(k) for k in types]
    for j in list_dolls:
        if j in occ:
            occ[j] +=1
        else:
            occ[j] = 1
    for key,val in occ.items():
        if val%2 == 1:
            print(list(occ.keys())[list(occ.values()).index(val)])
        else:
            pass
        
