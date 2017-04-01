def pickUpCoins(coins):
    mat = {}

    def maxRevenueForFirstPlayer(a, b):
        if a > b: return 0
        if (a,b) not in mat:
            maxRevenueA = coins[a] + min(maxRevenueForFirstPlayer(a+2, b),maxRevenueForFirstPlayer(a+1, b-1))
            maxRevenueB = coins[b] + min(maxRevenueForFirstPlayer(a, b-2), maxRevenueForFirstPlayer(a+1, b-1))
            mat[(a,b)] = max(maxRevenueB, maxRevenueA)

        return mat[(a,b)]

    return maxRevenueForFirstPlayer(0, len(coins)-1)


# coins = [10,25,5,1,10,5]
coins = [25,5,10,5,10,5,10,25,1,25,1,25,1,25,5,10]
print pickUpCoins(coins)
