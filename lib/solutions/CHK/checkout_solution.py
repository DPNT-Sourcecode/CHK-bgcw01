import pytest
class CheckoutSolution:

    def computeTotal(self, item, itemNumber, numOfBs):
        prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
        discounts = {"A": True, "B": True, "C": False, "D": False, "E": True}
        amountForDiscount = {"A": [5,3], "B": [2], "C": [0], "D": [0], "E" : [2]}
        offerPrice = {"A5": 500, "A3": 130, "B2": 45, "C": 0, "D": 0, "E2": -45}
        runningTotal = 0
        discountItems = 0

        #Compute discount if any per item
        bestIndex = 0

        #check if
        if discounts[item] == True:
            for i in range(0, len(amountForDiscount[item])):
                discountItems = itemNumber // amountForDiscount[item][i]
                if discountItems != 0:
                    break
            if item == "E":
                if (numOfBs % 2) != 0:
                    runningTotal
            itemNumber -= (discountItems * amountForDiscount[item][bestIndex])
            key = item + bestIndex
            runningTotal += offerPrice[key] * discountItems

        runningTotal += prices[item] * itemNumber

        return runningTotal


    # skus = unicode string

    def checkout(self, skus):

        if isinstance(skus, str):
            items = list(skus)
            total = 0
            #if "" or 0 then return 0
            if len(items) == 0 or (all(item in {""} for item in items)):
                return 0
            elif ((len(items) != 0) and (all(item in {"A", "B", "C", "D", "E"} and item != "" for item in items))):
                #count number of items
                item_counts = {}
                for i in items:
                    if i in  item_counts:
                        item_counts[i] +=1
                    else:
                        item_counts[i] = 1

                #total depending on number and sales
                #for length of dict
                for item in item_counts:
                    total += self.computeTotal(item, item_counts[item])

                return total
            else:
                return -1
        else:
            return -1

####------------tests
@pytest.fixture
def checkout():
    return CheckoutSolution()

def test_one(checkout):
    assert checkout.checkout("A") == 50
    assert checkout.checkout("B") == 30
    assert checkout.checkout("C") == 20
    assert checkout.checkout("D") == 15

def test_multi_no_discount(checkout):
    assert checkout.checkout("AB") == 80
    assert checkout.checkout("ACD") == 85
    assert checkout.checkout("BCD") == 65

def test_multi_discount(checkout):
    assert checkout.checkout("AAA") == 130
    assert checkout.checkout("AAAA") == 180

def test_mixed_items(checkout):
    assert checkout.checkout("AAAB") == 160
    assert checkout.checkout("AABBB") == 175
    assert checkout.checkout("AAABB") == 175

def test_empty_string(checkout):
    assert checkout.checkout("") == 0

def test_erroneous(checkout):
    assert checkout.checkout("A ") == -1




