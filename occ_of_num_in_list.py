# Number of occ of all items in list:

sample_list = [3,7,8,9,3,6,7,3,10,17,10,3]
occ = {}

for i in range(len(sample_list)):
    if sample_list[i] in occ:
        occ[sample_list[i]] += 1
    else:
        occ[sample_list[i]] = 1
print(occ)
       
