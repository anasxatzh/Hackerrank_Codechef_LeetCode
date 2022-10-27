
s = 'I am Anastasis'

count_up = 0
count_low = 0
a = s.split()


for i in range(len(a)):
    for j in range(len(a[i])):

        if a[i][j].isupper():
            count_up += 1

        elif a[i][j].islower():
            count_low += 1

print(s)
print('upper case char:', count_up)
print('lower case char:', count_low)
