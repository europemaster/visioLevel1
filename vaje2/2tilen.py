# -*- coding: utf-8 -*-
import helper2

cart, moneyAvailable = helper2.buy() # priceArray is an array with prices for some articles, moneyAvailable is how much money for
# purchase we have

food = 4.8 # maximum price for food item
tech = 95 # ...
clothes = 31 # ...

foodcount = 0
techcount = 0
clothescount = 0
overprice = 0
totalprice = sum(cart)

print(cart, moneyAvailable)
totalprice = sum(cart)  #///////// already defined in line 15
print 'Totalprice in cart: ', totalprice #///////// not needed

average = [sum(cart) / len(cart)] #total price / št. v cartu #///////// you defined an array, no need for this
print 'Average price: ', (average) #prints average price

for i in cart:
    if food<=i:
     foodcount=foodcount+1
    print ('foodcount',foodcount) #prints price how many items could be food
    # ///////// this is printed on every loop
    # ///////// algorithm is wrong
    if tech<=i:
     techcount=techcount+1
    print ('techcount: ', techcount) #prints price how many items could be tech
    if clothes<=i:
     clothescount=clothescount+1
    print ('clothescount: ', clothescount) #prints price how many items could be clothes
    if i>tech:
     overprice=overprice+1
    print ('overprice: ',overprice) #prints price over tech
    if totalprice<=moneyAvailable:
     print('buy!!')
    else:
        print('Go home!')

print 'This is min price: ',min(cart)
print 'This is max price: ',max(cart)
print 'Average price: ', (average)
print 'Total price in cart: ', totalprice
print 'Total available money: ', moneyAvailable
print 'This is count of food items: ', foodcount
print 'This is count of tech items: ',   techcount
print 'This is count of clothes items: ',   clothescount

# # When running program, prompt will asks us how many items
# #we want to buy and will create an array with prices. If there are
# #more than 50 items, array will be empty

##### INSTRUCTIONS #####
# Create a program which:
# - calculates average price *
# - calculates max and min price
# - counts how many items could be food, clothes or tech and how many items are above price of any of these *
# - can I buy all the items with moneyAvailable (prints True or False)
# use loops, if/else, arrays...