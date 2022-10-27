# FIND FOUR_SUM OF ARRAY


def find_four_sum(A, foursum, l):

    for i in range(l-3):
        for k in range(i+1, l-2):
            for j in range(k+1, l-1):
                for x in range(j+1, l):
                    if A[i]+A[k]+A[j]+A[x] == foursum:
                        print('The four numbers are:', A[i], ',', A[k], ',', A[j], ',', A[x])
                        return True
    return False

A = [1, 5, 3, 9, 18, 15, 22]
foursum = 24
l = len(A)
print(find_four_sum(A,foursum,l))
