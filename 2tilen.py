# -*- coding: utf-8 -*-
#import helper2
import math
#cart, moneyAvailable = helper2.buy() # priceArray is an array with prices for some articles, moneyAvailable is how much money for
# purchase we have

food = 4.8 # maximum price for food item
tech = 95 # ...
clothes = 31 # ...

cart = []
for i in range(int(input("How many items will you buy?: "))): #user inputs how many items will he buy
 cart.append(input("which item would you like to buy? ")) #cart get size of the array
print ('Items in cart: ', len(cart)) #prints prices of items

total = sum(cart) #sums up items
print ('Total price: ', total)#prints total price

average = [sum(cart) / len(cart)] #total price / št. v cartu
print ('Average price: ', average) #prints average price

# for i in :
#  print('Max: ')
#  print('Min: ')

#print(cart)
# # When running program, prompt will asks us how many items
# #we want to buy and will create an array with prices. If there are
# #more than 50 items, array will be empty

##### INSTRUCTIONS #####
# Create a program which:
# - calculates average price
# - calculates max and min price
# - counts how many items could be food, clothes or tech and how many items are above price of any of these
# - can I buy all the items with moneyAvailable (prints True or False)
# use loops, if/else, arrays...

