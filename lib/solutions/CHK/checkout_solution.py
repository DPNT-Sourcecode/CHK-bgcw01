
class CheckoutSolution:
    def computeDiscount(self, itemNum, offer, offerPrice, regPrice):
        numOfDiscoun = (items_counts["A"]) // offer
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
        computeDiscount()






