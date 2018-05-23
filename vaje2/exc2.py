import helper2
import sys

cart, moneyAvailable = helper2.buy() # priceArray is an array with prices for some articles, moneyAvailable is how much money for
# purchase we have.

food = 4.8 # maximum price for food item
tech = 95 # ...
clothes = 31 # ...

print(cart, moneyAvailable)
# # When running program, prompt will asks us how many items
# #we want to buy and will create an array with prices. If there are
# #more than 50 items, array will be empty


####----------- SOLUTION -----------#####

#  1. calculates average price
average = sum(cart)/len(cart)

print("Average is: ", average)
#  2. calculates max and min price

max = 0
min = sys.maxint

for price in cart:
    if price > max:
        max = price
    if price < min:
        min = price

print("Maximum: ", max," Minimum: ",min)
#  3. counts how many items could be food, clothes or tech and how many items are above price of any of these

foodPrice, clothesPrice, techPrice, noneOfThis = 0, 0, 0, 0
for price in cart:
    if price <= food:
        foodPrice += 1
    elif price <= clothes:
        clothesPrice += 1
    elif price <= tech:
        techPrice += 1
    else:
        noneOfThis += 1

print(foodPrice, " could be food, ",clothesPrice, " could be clothes, ",techPrice, " could be tech, ",noneOfThis," has/have price above any of these")

#  4. can I buy all the items with moneyAvailable (prints True or False)
# use loops, if/else, arrays...

if sum(cart) > moneyAvailable:
    print("Do I have enough money? ", False)
else:
    print("Do I have enough money? ", True)
