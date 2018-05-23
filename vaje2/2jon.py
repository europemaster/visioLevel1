import helper2

cart, moneyAvailable = helper2.buy() # priceArray is an array with prices for some articles, moneyAvailable is how much money for
# purchase we have

food = 4.8 # maximum price for food item
tech = 95 # ...
clothes = 31 # ...

print(cart, moneyAvailable)
# # When running program, prompt will asks us how many items
# #we want to buy and will create an array with prices. If there are
# #more than 50 items, array will be empty



Average = sum(cart)/len(cart) #///////// variable names usually begin with lower case, so average in this case
print("Average = ",Average)

print("Max = ",max(cart),"Min = ", min(cart))

##///////// names of variables should be more descriptive if there is another person looking your code
F = 0
T = 0
C = 0
nicodtega = 0

for i in cart:

    if i <= 4.8:
        F += 1

    elif i <= 31:
        C += 1

    elif i <= 95:
        T += 1
    else:
        nicodtega =+ 1

print("Food = ",F,"Clothes = ",C,"Tech = ",T,"Unknown = ",nicodtega)

if sum(cart) > moneyAvailable:
    print("Not enough money")

else:
    print("Shut up and take my money")




##### INSTRUCTIONS #####
# Create a program which:
#  - calculates average price
#  - calculates max and min price
#  - counts how many items could be food, clothes or tech and how many items are above price of any of these
#  - can I buy all the items with moneyAvailable (prints True or False)
# use loops, if/else, arrays...