
class CheckoutSolution:
    def computeDiscount(self, item, offer, offerPrice, regPrice):
        
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

        numOfADiscounts = (items_counts["A"]) // 3



