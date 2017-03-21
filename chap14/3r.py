class Name(object):
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __ne__(self, other):
        return not (self.first == other.first and self.last == other.last)

def eliminateDups(arr):
    idx = 0
    arr = sorted(arr, key=lambda x: x.first)
    for i in range(1,len(arr)):
        if arr[idx] != arr[i]:
            arr[idx+1] = arr[i]
            idx += 1

    return arr[:idx]


arr = [Name("Ian","Bell"), Name("David","Gower"), Name("David","Gower"),Name("David","Gower"), Name("Ian","Botham"),Name("David","Gower"), ]

print [(name.first, name.last) for name in eliminateDups(arr)]
