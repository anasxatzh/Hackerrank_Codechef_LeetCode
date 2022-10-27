# Check if an integer is a palinrome or not:

n = int(input('Enter a number to check whether it is a Palindrome or not:'))

temp = n
res = 0 # Initialize the result

while n > 0: # say number n = 555
    
    dig = n%10


    res = res*10 + dig 
 



    n //= 10
 

if res == temp:
    print('The number is a Palindrome')
else:
    print('the number is not a palindrome')
    
