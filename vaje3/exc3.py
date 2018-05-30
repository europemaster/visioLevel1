import helper3
from time import sleep
# 1. Create an input where user inputs number of groceries that he/she wants to buy.
# Save input into variable named your_input.
# If user inputs a number greater than 40, set your_input to 0.
def your_input():
    your_input = int(input("How many groceries would you want to buy?"))
    if your_input > 40:
        your_input = 0
    return  your_input

number = your_input()
# Do not change line below.
price_list, groceries_list, money_available = helper3.buy(your_input)
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


def chart_print(price_list, groceries_list):
    groceries_avg = price_average(price_list)
    print("\n----------\nAverage cart price is: {:0.2f}€\n----------".format(groceries_avg))
    for index, p in enumerate(price_list):
        print("{0} : {1}€".format(groceries_list[index], p))
        if comparer(p, groceries_avg):
            print("This is below average price")
        else:
            print("This is above average price.")

# 4. Use a function from task #2 and for every grocery prints if its price is above or below average.


def comparer(price, average):
    if price < average:
        return True
    else:
        return False

chart_print(price_list, groceries_list)