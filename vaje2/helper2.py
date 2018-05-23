from random import random


def buy():
    itemNo = int(input("How many things would you like to buy? (up to 50)"))
    priceAr = []
    if itemNo > 50:
        return priceAr, 0
    for i in range(itemNo):
        priceAr.append(round(random()*100, 2))
    return priceAr, round((random()*100)*itemNo)