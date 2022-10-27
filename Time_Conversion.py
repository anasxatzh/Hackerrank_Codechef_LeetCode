# Time conversion:

s = str(input())
new = ''
def timeConversion(s):
    k = s[0:2]
    if s[8] == 'P':
        if k == '12':
            new = s
            new = new.replace(s[8:10], '')
        else: # k == '1', '2', '3', ...
            
            k = int(k)
            new_value = k + 12
            new_value = str(new_value)
            new = s.replace(s[0:2], new_value, 1)
            new = new.replace(s[8:10], '')
            
    elif s[8] == 'A':
        if k =='12':
            new = s.replace(k, '00', 1)
            new = new.replace(s[8:10], '')
        else:
            new = s
            new = new.replace(s[8:10], '')
    return new
print(timeConversion(s))


