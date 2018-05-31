from time import sleep
import helper4

# for starter data use helper4.buy function
# use functions that were done in exercise 3

# use code for input from exercise 3 and create a function that returns that input
# save it to the variable named `your_input`
def your_input():
    inpt = int(input("How many groceries would you want to buy?"))
    if inpt > 40:
        return 0
    return  inpt
# Do not change line below.

# 1. Create function which creates and prints a pyramid like this:
#                * (1 STAR)
#               *** ...
#              *****
#             *******
#            ********* ...
#           *********** (11 STARS)
#     !!! CONGRATULATIONS !!!
#           ***********
#            *********
#             *******
#              *****
#               ***
#                *

def rhombus():
    odmik = " "*6
    for i in range(6):
        num_empty = 5-i
        num_stars =  (i*2)+1
        print(odmik + " "*num_empty + "*"*num_stars + " "*num_empty)
    print("!!! CONGRATULATIONS !!!")
    for j in range(6):
        num_stars = 11-(j*2)
        print(odmik + " "*j +"*"*num_stars +" "*j)

def shop():
    total = 0
    for i in range(100):
        price_list, groceries_list, money_available = helper4.buy()
        if i == helper4.random_winner():
            rhombus()
        else:
            if money_available < sum(price_list):
                print("NO MONEY")
            else:
                total = total + money_available
                print("Purchase is worth: {}\nmoney available: {}".format(sum(price_list), money_available))
    print("Money earned in a day: {}€".format(total))

shop()









# 2 create a function that simulates purchases
# let's say there are 100 purchases in a lifetime of a program where a timeout
# between the two is 3 seconds. `sleep(3)`
# use helper4.random_winner() function to get winning number
# if the winning number equals the number of the customer, purchase is free,
# use function from exercise #1, wait for 10 seconds, and move on to the next customer
# function returns the number of money earned, if the customer does not have enough money
# print "customer without money" and move on. this customer's purchase is not added
# to the money earned