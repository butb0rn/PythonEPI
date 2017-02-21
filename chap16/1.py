def hanoi(n, source, helper, target):
    # print "hanoi(", n, source, helper, target, ") called"
    if n > 0:
        hanoi(n-1, source, target, helper)
        if source[0]:
            disk = source[0].pop()
            # print "moving " + str(disk) + " from " + source[1] + " to " +target[1]
            target[0].append(disk)
        hanoi(n-1, helper, source, target)


source = ([4,3,2,1], "source")
target = ([], "target")
helper = ([], "helper")
hanoi(len(source[0]), source, helper, target)
print source, helper, target
