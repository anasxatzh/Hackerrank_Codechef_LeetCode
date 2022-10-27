# Palindrome string:

def IsPalindrome(n):
    if n == n[::-1]:
        print('The string is a palindrome')

    else:
        print('The string is not a plindrome')

n = str(input('Enter a string:'))
print(IsPalindrome(n))
