# CODECHEF : Encoding Message

for i in range(int(input())):
    N = int(input('Enter the length of the string:'))
    s = str(input()) # sharechat
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(0,N-1,2): # 0-->2-->4-->6
                             # 1-->3-->5-->7

        s = list(s)
        s[i],s[i+1] = s[i+1], s[i]

      
