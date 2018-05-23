from time import sleep
import exc3
import helper4

# for starter data use helper4.buy function
# use functions that were done in exercise 3

# Do not change line below.
price_list, groceries_list, money_available = helper4.buy(exc3.customer_input())
print(price_list)

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

# 2 create a function that simulates purchases
# let's say there are 100 purchases in a lifetime of a program where a timeout
# between the two is 3 seconds. `sleep(3)`
# use helper4.random_winner() function to get winning number
# if the winning number equals the number of the customer, purchase is free,
# use function from exercise #1, wait for 10 seconds, and move on to the next customer
# function returns the number of money earned, if the customer does not have enough money
# print "customer without money" and move on. this customer's purchase is not added
# to the money earned