from random import random
import sys


def buy(item_number):
    if item_number < 1:
        sys.exit(0)
    price_arr = []
    groceries = []
    groceries_map = {1: "food", 2: "clothes", 3: "tech", 4: "toys"}
    if item_number > 50:
        return price_arr, 0
    for i in range(item_number):
        price_arr.append(round(random()*100, 2))
        groceries.append(groceries_map[int(random()*4)+1])
    return price_arr, groceries, round((random()*100)*item_number)


def random_winner():
    return int(random()*100)+1
