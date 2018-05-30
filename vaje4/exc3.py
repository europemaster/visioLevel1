import helper4
from time import sleep
# 1. Create an input where user inputs number of groceries that he/she wants to buy.
# Save input into variable named your_input.
# If user inputs a number greater than 40, set your_input to 0.


def customer_input():
    your_input = int(input("How many groceries would you want to buy?"))
    if your_input > 40:
        return 0
    else:
        return your_input

# Do not change line below.
price_list, groceries_list, money_available = helper4.buy(customer_input())
#

# 2. Create a function that accepts price_list as a parameter and returns average.


def price_average(price_list):
    return sum(price_list)/len(price_list)

# 3. price_list and groceries_list are arrays that are the same length. groceries_list contains names of groceries. First price in
# price_list is a price for the first grocery in groceries_list and so on.
# Create a function that prints all groceries and its price like:
# food, 15
# clothes, 9
# ...

# def chart_print2(price_list, groceries_list):
#     for index, val in enumerate(price_list):
#         print(val, groceries_list[index])
#
# chart_print2(price_list, groceries_list)

def chart_print(price_list, groceries_list):
    groceries_avg = price_average(price_list)
    print("\n----------\nAverage cart price is: {}€\n----------".format(groceries_avg))
    for index, p in enumerate(price_list):
        print("{} : {}€".format(groceries_list[index], p))
        if comparer(p, groceries_avg):
            print("This is below average price")
        else:
            print("This is above average price.")
        sleep(0.5)

# 4. Use a function from task #2 and for every grocery prints if its price is above or below average.


def comparer(price, average):
    if price < average:
        return True
    else:
        return False

chart_print(price_list, groceries_list)