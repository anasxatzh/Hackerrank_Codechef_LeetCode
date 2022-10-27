
jack_cost, sock_cost, money = list(map(int,input().split()))
# cost of the jackt , cost of a single sock , initial amount of money

money_after_jack = money - jack_cost # money left after the purch of the jacket


if money_after_jack >=  sock_cost:
    number_socks = money_after_jack // sock_cost

    if number_socks %2 == 0: # if it is even
        print('Lucky chef')
    else:
        print('Unlucky chef')


    
elif money_after_jack ==  sock_cost:
    
    print('Lucky chef')

## 1 2 10 --> 9%2 = 1
            #9//2 = 4 socks
