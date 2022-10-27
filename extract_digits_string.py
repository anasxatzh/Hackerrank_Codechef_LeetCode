# Extract digits from string:


s = str(input('Enter a string:'))

result = ''.join(filter(lambda i: i.isdigit(), s))
print(result)

# OR

##s_list = s.split()
##for i in s_list:
##    if i.isdigit():
##        print(i)
##       
