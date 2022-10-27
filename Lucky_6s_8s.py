

# Input a range of numbers:
# Ouput --> lucky numbers between the input range

def islucky(num):
    num = str(num)
    len_num = len(num)

    c = []

    count = 0
    for i,dig in enumerate(num):

        power_ten = len_num - i - 1

        for k in range(int(dig)):
            if (k == 6 or k == 8 or '6' in c or '8' in c):
                count += 9**power_ten
            else:
                count += 2*(9**power_ten - 8**power_ten)
        c.append(dig)
        if '6' in c and '8' in c:
            break
    return count
l,r = [int(i) for i in input().split()]
print(islucky(r+1) - islucky(l))
