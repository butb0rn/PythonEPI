class Item(object):
    def __init__(self, w, v):
        self.weight = w
        self.value = v

def findOptimumSub(items, capacity):
    mat = [[ -1 for j in range(capacity+1)] for i in range(len(items)+1)]
    def optHelper(itemIdx, capacity):
        if itemIdx < 0: return 0
        if mat[itemIdx][capacity] == -1:
            withoutCurItem = optHelper(itemIdx-1, capacity)
            withCurItem =  items[itemIdx].value + optHelper(itemIdx-1, capacity-items[itemIdx].weight) if items[itemIdx].weight <= capacity else 0

            mat[itemIdx][capacity] = max(withCurItem, withoutCurItem)

        return mat[itemIdx][capacity]

    return optHelper(len(items)-1, capacity)

items = [Item(5, 60), Item(3, 50), Item(4, 70), Item(2, 30)]

print findOptimumSub(items, 5)
