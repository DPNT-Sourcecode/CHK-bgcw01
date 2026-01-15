
class CheckoutSolution:


    def computeTotal(self, item, itemNumber, offerPrice, regPrice):
        prices = {"A": 50, "B": 30, "C": 20, "D": 15}
        discounts = {"A": True, "B": True, "C": False, "D": False}
        amountForDiscount = {"A": 3, "B": 2, "C": 0, "D": 0}
        offerPrice = {"A": 130, "B": 45, "C": 0, "D": 0}
        total = 0
        discountItems = 0

        #Compute discount if any
        if discounts[item] == True:
            if item == "A":
                discountItems = (itemNumber["A"]) // amountForDiscount["A"]
                itemNumber =- discountItems

            elif item == "B":
        else:
            total = prices[item] * itemNumber

        return total


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

        #total depending on number and sales
        #for length of dict
        computeTotal()







