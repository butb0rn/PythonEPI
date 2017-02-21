import sys

def computeMaxProfit(prices):
    minPrice, maxProfit = sys.maxint, 0.0
    for price in prices:
        maxProfit = max(maxProfit, price - minPrice)
        minPrice  = min(minPrice, price)

    return maxProfit

l = [310,315,275,295,260,270,290,230,255,250]
print computeMaxProfit(l)
