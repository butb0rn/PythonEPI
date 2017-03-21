def longestContainedRange(l):
    unprocessedEntries = set(l)
    maxIntervalSize = 0

    while unprocessedEntries:
        element = unprocessedEntries.pop()
        print element

        lowerBound = element - 1
        while lowerBound in unprocessedEntries:
            unprocessedEntries.discard(lowerBound)
            lowerBound -= 1

        upperBound = element + 1
        while upperBound in unprocessedEntries:
            unprocessedEntries.discard(upperBound)
            upperBound += 1

        maxIntervalSize = max(maxIntervalSize, upperBound - lowerBound -1)

    return maxIntervalSize


# l = [3,-2,7,9,8,1,2,0,-1,5,8]
l = [3,-2,5,5,5,1,2,0,-1,5,5,5,6,7,8,10,11,4,9]
print longestContainedRange(l)
