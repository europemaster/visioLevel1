import helper3

# 1. Create an input where user inputs number of groceries that he/she wants to buy.
# Save input into variable named your_input.
# If user inputs a number greater than 40, set your_input to 0.
your_input = int(input('Enter the number of groceries you want to buy: '))
if your_input > 40:
    your_input = 0
    print("Value too high")

# Do not change line below.
price_list, groceries_list, money_available = helper3.buy(your_input)
#
print(price_list)
# 2. Create a function that accepts price_list as a parameter and returns average.
def average_calc(price_list):
    average = sum(price_list)/len(price_list)
    return average
print(average_calc(price_list))

# 3. price_list and groceries_list are arrays that are the same length. groceries_list contains names of groceries. First price in
# price_list is a price for the first grocery in groceries_list and so on.
# Create a function that prints all groceries and its price like:
# food, 15
# clothes, 9
# ...
#print(price_list)
#print(groceries_list)
def cart(price_list, groceries_list):
    for i in range(len(price_list)):
        print(groceries_list[i] + "," + str(price_list[i]))
cart(price_list, groceries_list)

#Druga opcija za tocko 3
#for i, j in zip(price_list,groceries_list):
    #print(j + "," + str(i))




# 4. Use a function from task #2 and for every grocery prints if its price is above or below average.
for i in range(len(price_list)):
    print(i)
    if price_list[i] < average_calc(price_list):
        print(groceries_list[i]+","+(str(price_list[i]))+"=Price is below average")
    else:
        print(groceries_list[i]+","+(str(price_list[i]))+"=Price is above average")
