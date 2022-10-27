# Delete any reoccurring character in a given string:

##s = 'aaaabbbvvssss'
s = str(input())
set_s = set()
new_str = ''
for i in range(len(s)):
    if s[i] not in set_s:
        set_s.add(s[i])
        new_str += s[i]
print(new_str)
        
