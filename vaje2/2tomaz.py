import helper2

#cart, moneyAvailable = helper2.buy() # priceArray is an array with prices for some articles, moneyAvailable is how much money for
# purchase we have

#food = 4.8 maximum price for food item
#tech = 95  maximum price for tech item
#clothes = 31  maximum price for clothes item

#print(cart, moneyAvailable)
# # When running program, prompt will asks us how many items
# input(into(
# #we want to buy and will create an array with prices. If there are
# #more than 50 items, array will be empty

##### INSTRUCTIONS #####
# Create a program which:
#  - calculates average price
#  - calculates max and min price
#  - counts how many items could be food, clothes or tech and how many items are above price of any of these
#  - can I buy all the items with moneyAvailable (prints True or False)
# use loops, if/else, arrays...


#Average
food = [4.8]
tech = [95]
clothes = [31]

ftc = [4.8, 95, 31]

print(sum(ftc)) / (len(ftc))
