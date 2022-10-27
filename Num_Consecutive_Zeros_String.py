## Find the number of consecutive zeros in an input string:


def consecutive_zeros(n,l):
    count = 0
    result = 0
    for i in range(l):
        if n[i] == '1':
            count = 0
        else:
            count += 1
            result = max(result,count)
    return result


n = str(input('Enter a binary string:'))
l = len(n)
print(consecutive_zeros(n,l))

