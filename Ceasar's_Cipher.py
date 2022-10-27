# Ceasar's cipher:

n = int(input('Enter the length of the string:'))

s = str(input())
k = int(input('Enter the rotation factor:'))
new_s = ''

def ceasarCipher(s,k):
    alphabet_low = 'abcdefghijklmnopqrstuvwxyz'*5
    alphabet_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'*5
    new_s = ''
    for i in range(len(s)):
        if s[i] not in alphabet_low and s[i] not in alphabet_up:
            new_s += s[i] 
        for j in range(int(len(alphabet_low)/5)):
            if s[i] == alphabet_low[j]:
                new_s += alphabet_low[k+j]
                
            elif s[i] == alphabet_up[j]:
                new_s += alphabet_up[k+j]
 
    return new_s


print(ceasarCipher(s,k))
