# Fib:

n = int(input('Enter a number:'))
seed_value1 = 0
seed_value2 = 1

def Fib(n):
    if n < 0:
        print('Enter a positive integer!')

    elif n == 0:
        return seed_value1
    
    elif n == 1:
        return seed_value2
    
    else:

        ans = Fib(n-1) + Fib(n-2)
        return ans

for i in range(n + 1):
    print(Fib(i))
    
  
