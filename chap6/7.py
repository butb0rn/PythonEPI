import sys

def buySellStockTwice(prices):
    maxProfit = 0.0
    minPrice = sys.maxint
    firstSell = []
    for price in prices:
        minPrice = min(minPrice, price)
        maxProfit = max(maxProfit, price - minPrice)
        firstSell.append(maxProfit)

    maxPrice = -1.0
    totalProfit = 0
    for idx in range(len(prices)-1,0,-1):
        maxPrice = max(maxPrice, prices[idx])
        totalProfit = max(totalProfit, maxPrice - prices[idx]+firstSell[idx-1])

    return totalProfit

print buySellStockTwice([12,11,13,9,12,8,14,13,15])
