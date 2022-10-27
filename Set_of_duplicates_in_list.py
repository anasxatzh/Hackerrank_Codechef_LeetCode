# Print set of duplicates in a list:

my_list = [1,5,2,3,7,5,2,1,7,6,9,88,66,55]
counts = []
for i in range(len(my_list)):
    if my_list.count(my_list[i]) > 1:
        counts.append(my_list[i])
print('Set_Of_Duplicates : ', set(counts))
# number of duplicates:
print('Number of Duplicates : ', len(set(counts)))

