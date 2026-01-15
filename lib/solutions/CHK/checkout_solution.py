import pytest
class CheckoutSolution:

    def computeTotal(self, item, itemNumber):
        prices = {"A": 50, "B": 30, "C": 20, "D": 15}
        discounts = {"A": True, "B": True, "C": False, "D": False}
        amountForDiscount = {"A": 3, "B": 2, "C": 0, "D": 0}
        offerPrice = {"A": 130, "B": 45, "C": 0, "D": 0}
        runningTotal = 0
        discountItems = 0

        #Compute discount if any per item
        if discounts[item] == True:
            discountItems = (itemNumber[item]) // amountForDiscount[item]
            itemNumber -= discountItems
            runningTotal += offerPrice[item] * discountItems

        runningTotal += prices[item] * itemNumber

        return runningTotal


    # skus = unicode string

    def checkout(self, skus):
        items = list(skus)

        #count number of items
        item_counts = {}
        for i in items:
            if i in  item_counts:
                item_counts[i] +=1
            else:
                item_counts[i] = 1
        total = 0
        #total depending on number and sales
        #for length of dict
        for item in item_counts:
            total += self.computeTotal(item, item_counts[item])

def checkout():
    return CheckoutSolution()

def




