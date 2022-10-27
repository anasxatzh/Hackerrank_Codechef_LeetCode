### Reverse Sort the elements in a list WITHOUT THE SORT FUNCTION:
##
##my_list = [9,10,4,8,5]
##
##for i in range(len(my_list)):
##
##    for j in range( i+1, len(my_list) ):
##
##        if my_list[j] > my_list[i]:
##            my_list[i], my_list[j] = my_list[j], my_list[i]
##print(my_list)
            
# Sort the elements in a list WITHOUT THE SORT FUNCTION:

my_list = [9,10,4,8,5]

for i in range(len(my_list)):

    for j in range( i+1, len(my_list) ):

        if my_list[j] < my_list[i]:
            my_list[i], my_list[j] = my_list[j], my_list[i]
print(my_list)
