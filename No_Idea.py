# No idea problem:
# Hhappiness problem


n,m = map(int, input('Enter the number of integers in array and sets:').split())
elements_n  = list(map(int,input().split()))
elements_m_A = list(map(int,input().split()))
elements_m_B = list(map(int, input().split()))
A = set(elements_m_A)
B = set(elements_m_B)
happiness = 0 #initialize the happiness value       
while A.isdisjoint(B) and len(elements_m_A) == len(elements_m_B) and (len(elements_n) == n or len(elements_m_A) == m or len(elements_m_A) == m):
    
##    happiness = 0 #initialize the happiness value
    for i in range(len(elements_n)):
        for j in range(len(elements_m_A)):
            if elements_n[i] == elements_m_A[j]:
                happiness += 1
            elif elements_n[i] == elements_m_B[j]:
                    happiness -= 1
    print(happiness)

    break
